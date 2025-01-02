import os
import sys
import glob
import time
import re
import platform
import threading
import posixpath
import ast
import textwrap
import binascii

import click
import dotenv
import serial

from genlib.ansiec import ANSIEC


try:
    stdout = sys.stdout.buffer
except AttributeError:
    stdout = sys.stdout

#--------------------------------------------------------------

def windows_full_port_name(portname):
    m = re.match(r"^COM(\d+)$", portname)
    if m and int(m.group(1)) < 10:
        return portname
    else:
        return "\\\\.\\{0}".format(portname)

def is_port(port):
    if platform.system() == "Windows":
        port = windows_full_port_name(port)
            
    try:
        with serial.Serial(port, 115200, timeout=1) as ser:
            ser.write(b'\x03') # Ctrl + C(b'\x03') --> interrupt any running program
            ser.read_all().decode('utf-8') # >>>
            ser.write(b'\x02') # Ctrl + B(b'\x02') --> enter normal repl, ref: Ctrl + D(b'\x04') --> soft reset, 
            time.sleep(0.1)
            response = ser.read_all().decode('utf-8').strip()

            if 'MicroPython' in response:
                s = response.find("MicroPython") + len("MicroPython")
                e = response.find('Type "help()"')
                return response[s:e].strip()
    except (OSError, serial.SerialException):
        pass
    
    return None

def scan():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]    
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    color_tbl = (ANSIEC.FG.BRIGHT_YELLOW, ANSIEC.FG.BRIGHT_GREEN, ANSIEC.FG.BRIGHT_BLUE)
    color_pos = 0    
    
    for port in ports:
        descript = is_port(port)
        if descript:
            print(color_tbl[color_pos] + f"{port}" + ANSIEC.OP.RESET + f" ({descript})")
            color_pos = (color_pos + 1) % len(color_tbl)

def stdout_write_bytes(b):
    b = b.replace(b"\x04", b"")
    stdout.write(b)
    stdout.flush()

#--------------------------------------------------------------

class Board:
    BUFFER_SIZE = 32

    def __init__(self, port, baudrate=115200, wait=0):     
        delayed = False

        if platform.system() == "Windows":
            port = windows_full_port_name(port)

        for attempt in range(wait + 1):
            try:
                self.serial = serial.Serial(port, baudrate, inter_byte_timeout=0.1)
                break
            except (OSError, IOError): 
                if wait == 0:
                    continue
                if attempt == 0:
                    sys.stdout.write(f"Waiting {wait} seconds for board ")
                    delayed = True
            time.sleep(1)
            sys.stdout.write('.')
            sys.stdout.flush()
        else:
            if delayed:
                print('')
            raise BaseException('failed to access ' + port)
        if delayed:
            print('')
        
        self.__init_repl()

    def __init_repl(self):
        self.serial_reader_running = None
        self.serial_out_put_enable = True
        self.serial_out_put_count = 0

    def close(self):
        self.serial.close()

    def read_until(self, min_num_bytes, ending, timeout=10, data_consumer=None):
        data = self.serial.read(min_num_bytes)
        if data_consumer:
            data_consumer(data)
        timeout_count = 0
        while True:
            if data.endswith(ending):
                break
            elif self.serial.in_waiting > 0:
                new_data = self.serial.read(1)
                data = data + new_data
                if data_consumer:
                    data_consumer(new_data)
                timeout_count = 0
            else:
                timeout_count += 1
                if timeout is not None and timeout_count >= 100 * timeout:
                    break
                time.sleep(0.01)
        return data

    def enter_raw_repl(self):
        self.serial.write(b'\r\x03\x03') # ctrl-C twice: interrupt any running program

        n = self.serial.in_waiting
        while n > 0:
            self.serial.read(n)
            n = self.serial.in_waiting

        self.serial.write(b'\r\x01') # ctrl-A: enter raw REPL
        data = self.read_until(1, b'raw REPL; CTRL-B to exit\r\n>')
        if not data.endswith(b'raw REPL; CTRL-B to exit\r\n>'):
            print(data)
            raise BaseException('could not enter raw repl')

        self.serial.write(b'\x04') # ctrl-D: soft reset
        data = self.read_until(1, b'soft reboot\r\n')
        if not data.endswith(b'soft reboot\r\n'):
            print(data)
            raise BaseException('could not enter raw repl')

        data = self.read_until(1, b'raw REPL; CTRL-B to exit\r\n')
        if not data.endswith(b'raw REPL; CTRL-B to exit\r\n'):
            print(data)
            raise BaseException('could not enter raw repl')

    def exit_raw_repl(self):
        self.serial.write(b'\r\x02') # ctrl-B: enter friendly REPL

    def _follow_write(self, echo):        
        try:
            import msvcrt
            def getkey():
                return msvcrt.getch()

            def putkey(ch):
                if ch == b'\r':
                    ch = b'\n'
                msvcrt.putch(ch)
                
        except ImportError:
            import sys, tty, termios
            def getkey():
                fd = sys.stdin.fileno()
                old = termios.tcgetattr(fd)
                try:
                    tty.setraw(sys.stdin.fileno())
                    ch = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old)
                return ch
            
            def putkey(ch):
                sys.stdout.write(ch)
                sys.stdout.flush()
        
        while True:
            ch = getkey()
            if ch == b'\x03': # Ctrl + C
                os._exit(0)
            if echo:
                putkey(ch)
            self.serial.write(ch)

    def follow(self, timeout, data_consumer=None, input_stat=None):
        if input_stat[1]:
            threading.Thread(target=self._follow_write, args=(input_stat[0],), daemon=True).start()
        
        data = self.read_until(1, b'\x04', timeout=timeout, data_consumer=data_consumer)
        if not data.endswith(b'\x04'):
            raise BaseException('timeout waiting for first EOF reception')
        data = data[:-1]

        data_err = self.read_until(1, b'\x04', timeout=timeout)
        if not data_err.endswith(b'\x04'):
            raise BaseException('timeout waiting for second EOF reception')
        data_err = data_err[:-1]

        return data, data_err

    def exec_raw_no_follow(self, command):            
        if isinstance(command, bytes):
            command_bytes = command
        else:
            command_bytes = bytes(command, encoding='utf8')

        data = self.read_until(1, b'>')
        if not data.endswith(b'>'):
            raise BaseException('could not enter raw repl')

        for i in range(0, len(command_bytes), 256):
            self.serial.write(command_bytes[i:min(i + 256, len(command_bytes))])
            time.sleep(0.01)
        self.serial.write(b'\x04')

        data = self.read_until(1, b'OK')
        if not data.endswith(b'OK'):
            raise BaseException('could not exec command')

    def exec_raw(self, command, timeout=None, data_consumer=None, input_stat=None):
        self.exec_raw_no_follow(command)
        return self.follow(timeout, data_consumer, input_stat)

    def exec_(self, command, stream_output=False, echo_on=False):
        data_consumer = None
        if stream_output or echo_on:
            data_consumer = stdout_write_bytes
        ret, ret_err = self.exec_raw(command, data_consumer=data_consumer, input_stat=(stream_output, echo_on))
        if ret_err:
            raise BaseException('exception', ret.decode('utf-8'), ret_err.decode('utf-8'))
        return ret
    
    def execfile(self, filename, stream_output=False, echo_on=False):
        with open(filename, 'r+b') as f:
            pyfile = f.read()
        return self.exec_(pyfile, stream_output, echo_on)
    
    def _exec_command(self, command):
        self.enter_raw_repl()
        try:
            out = self.exec_(textwrap.dedent(command))
        except BaseException as ex:
            raise ex
        self.exit_raw_repl()
        return out

    def run(self, filename, stream_output=False, echo_on=False):
        self.enter_raw_repl()
        if not stream_output and not echo_on:       # -n
            with open(filename, "rb") as infile:        # Running without io stream
                self.exec_raw_no_follow(infile.read())
        elif not stream_output and echo_on:         # -in
            self.execfile(filename, False, True)        # Echo off
        elif stream_output and echo_on:             #-i
            self.execfile(filename, True, True)         # Echo on            
        else:                                       # default
            self.execfile(filename, False, True)        # Echo off
        self.exit_raw_repl()

    def __repl_serial_to_stdout(self):        
        def hexsend(string_data=''):
            import binascii
            hex_data = binascii.unhexlify(string_data)
            return hex_data

        try:
            data = b''
            while self.serial_reader_running:
                count = self.serial.in_waiting
                if count == 0:
                    time.sleep(0.01)
                    continue

                if count > 0:
                    try:
                        data += self.serial.read(count)

                        if len(data) < 20:
                            try:
                                data.decode()
                            except UnicodeDecodeError:
                                continue

                        if data != b'':
                            if self.serial_out_put_enable and self.serial_out_put_count > 0:
                                if platform.system() == 'Windows':   
                                    sys.stdout.buffer.write(data.replace(b"\r", b""))
                                else:
                                    sys.stdout.buffer.write(data)
                                    
                                sys.stdout.buffer.flush()
                        else:
                            self.serial.write(hexsend(data))

                        data = b''
                        self.serial_out_put_count += 1

                    except:
                        return
        except KeyboardInterrupt:
            if serial != None:
                serial.close()
                
    def repl(self):
        self.serial_reader_running = True
        self.serial_out_put_enable = True
        self.serial_out_put_count = 1

        self.read_until(1, b'\x3E\x3E\x3E', timeout=1) # read prompt >>>

        repl_thread = threading.Thread(target=self.__repl_serial_to_stdout, daemon=True, name='REPL')
        repl_thread.start()

        if platform.system() == 'Windows':   
            import msvcrt as getch
        else:
            import getch
            
        serial.write(b'\r') # Update prompt
        
        count = 0
        
        while True:
            char = getch.getch()
        
            if char == b'\x16': # Ctrl + V(\x16) to Ctrl + C(\x03)
                char = b'\x03'

            count += 1
            if count == 1000:
                time.sleep(0.01)
                count = 0

            if char == b'\x07':
                self.serial_out_put_enable = False
                continue

            if char == b'\x0F':
                self.serial_out_put_enable = True
                self.serial_out_put_count = 0
                continue

            if char == b'\x00' or not char:
                continue

            if char == b'\x18':   # Ctrl + X to exit repl mode
                self.serial_reader_running = False
                self.serial.write(b' ')
                time.sleep(0.01)
                print('')
                break

            self.serial.write(b'\r' if char == b'\n' else char)
           
    def fs_get(self, filename):
        command = f"""
            import sys
            import ubinascii
            with open('{filename}', 'rb') as infile:
                while True:
                    result = infile.read({self.BUFFER_SIZE})
                    if result == b'':
                        break
                    len = sys.stdout.write(ubinascii.hexlify(result))
        """
        out = self._exec_command(command)
        return binascii.unhexlify(out)

    def fs_ls(self, dir="/"):
        if not dir.startswith("/"):
            dir = "/" + dir
        #if dir.endswith("/"):
        #    dir = dir[:-1]
            
        command = f"""
            import os
            def listdir(dir):
                if dir == '/':                
                    return sorted([dir + f for f in os.listdir(dir)])
                else:
                    return sorted([dir + '/' + f for f in os.listdir(dir)])
            print(listdir('{dir}'))
        """
        out = self._exec_command(command)
        return ast.literal_eval(out.decode("utf-8"))
            
    def fs_is_dir(self, path):
        command = f"""
            vstat = None
            try:
                from os import stat
            except ImportError:
                from os import listdir
                vstat = listdir
            def ls_dir(path):
                if vstat is None:
                    return stat(path)[0] & 0x4000 != 0
                else:
                    try:
                        vstat(path)
                        return True
                    except OSError as e:
                        return False
            print(ls_dir('{path}'))
        """
        out = self._exec_command(command)
        return ast.literal_eval(out.decode("utf-8"))

    def fs_mkdir(self, dir):       
        command = f"""
            import os
            def mkdir(dir):
                parts = dir.split(os.sep)
                dirs = [os.sep.join(parts[:i+1]) for i in range(len(parts))]
                check = 0
                for d in dirs:
                    try:
                        os.mkdir(d)
                    except OSError as e:
                        check += 1
                        if "EEXIST" in str(e):
                            continue
                        else:
                            return False
                return check < len(parts)
            print(mkdir('{dir}'))
        """        
        out = self._exec_command(command)
        return ast.literal_eval(out.decode("utf-8"))

    def fs_putdir(self, local, remote, callback=None):        
        for parent, child_dirs, child_files in os.walk(local, followlinks=True):
            remote_parent = posixpath.normpath(posixpath.join(remote, os.path.relpath(parent, local)))
           
            try:
                self.fs_mkdir(remote_parent)
            except:
                pass
        
            for filename in child_files:
                with open(os.path.join(parent, filename), "rb") as infile:
                    remote_filename = posixpath.join(remote_parent, filename)
                    data = infile.read()

                    total_size = os.path.getsize(os.path.join(parent, filename))                 
                    if callback:
                        th = threading.Thread(target=callback, args=(remote_filename, total_size), daemon=True)
                        th.start()
                        
                    self.fs_put(data, remote_filename)
                    
                    if callback:
                        th.join() 

    def fs_put(self, local_data, remote, callback=None):
        self.enter_raw_repl()
        try:
            self.exec_(f"f = open('{remote}', 'wb')")
        except BaseException as e:
            if "EEXIST" in str(e):
                self.exit_raw_repl()
                self.fs_rm(remote)
                self.fs_put(local_data, remote, callback)
            return

        size = len(local_data)
        if callback:
            th = threading.Thread(target=callback, args=(remote, size), daemon=True)
            th.start()
            
        for i in range(0, size, self.BUFFER_SIZE):
            chunk_size = min(self.BUFFER_SIZE, size - i)
            chunk = repr(local_data[i : i + chunk_size])
            if not chunk.startswith("b"):
                chunk = "b" + chunk
            self.exec_(f"f.write({chunk})")
        
        self.exec_("f.close()")
        self.exit_raw_repl()
        
        if callback:
            th.join() 

    def fs_rm(self, filename):
        command = f"""
            import os
            os.remove('{filename}')
        """
        self._exec_command(command)

    def fs_rmdir(self, dir):
        command = f"""
            import os
            def rmdir(dir):
                os.chdir(dir)
                for f in os.listdir():
                    try:
                        os.remove(f)
                    except OSError:
                        pass
                for f in os.listdir():
                    rmdir(f)
                os.chdir('..')
                os.rmdir(dir)
            rmdir('{dir}')
        """
        self._exec_command(command)

    def fs_format(self, type):
        if type == "lopy":
            command = """ 
                import os
                os.fsformat('/flash')
            """
        elif type == "xbee3":
            command = """
                import os
                os.format()
            """
        elif type == "pico2":
            command = """
                import os
                import rp2
                bdev = rp2.Flash()
                os.VfsFat.mkfs(bdev)
            """
        else:
            return False
        
        self._exec_command(command)
        return True


#--------------------------------------------------------------

config = dotenv.find_dotenv(filename=".xnode", usecwd=True)
if config:
    dotenv.load_dotenv(dotenv_path=config)


_board = None
_type = None
_root_fs = None

@click.group()
@click.option(
    "--sport",
    "-s",
    envvar="SERIAL_PORT",
    required=True,
    type=click.STRING,
    help="Serial port name for connected board.",
    metavar="SPORT",
)
@click.option(
    "--baud",
    '-b',
    envvar="SERIAL_BAUD",
    default=115200,
    type=click.INT,
    help="Baud rate for the serial connection (default 115200).",
    metavar="BAUD",
)
@click.option(
    "--type",
    '-t',
    envvar="DEVICE_TYPE",
    default='xbee3',
    type=click.STRING,
    help="Device type",
    metavar="TYPE",
)
def xkit(sport, baud, type):
    global _board, _type, _root_fs

    if is_port(sport):
        _board = Board(sport, baud)
        _type = type.lower().strip()
    else:
        print("Board is not connected to " + ANSIEC.FG.BRIGHT_RED + f"{sport}" + ANSIEC.OP.RESET)
        print("Please check the ports with the scan command and try again.")
        raise click.Abort()
    
    if _type == 'xbee3':
        _root_fs = "/flash/"
    elif _type == 'pico2':
        _root_fs = "/"
    else:    
        print("The device type " + ANSIEC.FG.BRIGHT_RED + f"{_type}" + ANSIEC.OP.RESET + " is not supported.")
        raise click.Abort()
    
@xkit.command()
@click.argument("remote_file")
@click.argument("local_file", type=click.File("wb"), required=False)
def get(remote_file, local_file):
    try:
        contents = _board.fs_get(remote_file)
    
        if local_file is None:
            print(contents.decode("utf-8"))
        else:
            local_file.write(contents)
    except BaseException:
        print("The file " + ANSIEC.FG.BRIGHT_RED + f"{remote_file}" + ANSIEC.OP.RESET + " does not exist.")
    
@xkit.command()
@click.argument("dir")
def mkdir(dir):
    if _board.fs_mkdir(dir):
        print(f"{dir} is " + ANSIEC.FG.BRIGHT_GREEN + "created." + ANSIEC.OP.RESET)
    else:
        print(f"{dir} is " + ANSIEC.FG.BRIGHT_RED + "already exists." + ANSIEC.OP.RESET)

@xkit.command()
@click.argument("dir", default="/")
def ls(dir):          
    try:
        for f in _board.fs_ls(dir):
            f_name = f.split("/")[-1]
            if _board.fs_is_dir(f):
                print(f"{f_name}")
            else:
                print(ANSIEC.FG.BRIGHT_BLUE + f_name + ANSIEC.OP.RESET)
    except BaseException:
        print("The path " + ANSIEC.FG.BRIGHT_RED + "does not exist." + ANSIEC.OP.RESET)
                
def show_waiting(remote_filename, total_size):
    copied_size = 0
    bar_length = 40
    print(ANSIEC.FG.BRIGHT_BLUE + remote_filename + ANSIEC.OP.RESET, flush=True)
    while True:
        progress = min(copied_size / total_size, 1.0)    
        block = int(round(bar_length * progress))
        bar = "#" * block + "-" * (bar_length - block)
        print(ANSIEC.OP.left() + f"[{bar}] {int(progress * 100)}%", end="", flush=True)
        if progress >= 1.0:
            break
        time.sleep(0.1)
        if _type == 'xbee3':
            copied_size += (115200 // 8 // 100) * 0.8
        elif _type == 'pico2':
            copied_size += (115200 // 8 // 100) * 2
                    
    print(flush=True)

@xkit.command()
@click.argument("local", type=click.Path(exists=True))
@click.argument("remote", required=False)
def put(local, remote):
    if remote is None:
        remote = os.path.basename(os.path.abspath(local))
    else:
        try:
            if _board.fs_is_dir(remote):
                remote = remote + "/" + os.path.basename(os.path.abspath(local))
        except BaseException:
            pass
        
    if os.path.isdir(local):
        _board.fs_putdir(local, remote, show_waiting)
    else:
        with open(local, "rb") as infile:        
            _board.fs_put(infile.read(), remote, show_waiting)
    
@xkit.command()
@click.argument("remote")
def rm(remote):
    if _board.fs_is_dir(remote):
        _board.fs_rmdir(remote)
    else:
        _board.fs_rm(remote)

@xkit.command()
@click.argument("local_file")
@click.option(
    "--no-stream",
    "-n",
    is_flag=True,
    help="Do not join input/output stream",
)
@click.option(
    "--input-echo-on",
    "-i",
    is_flag=True,
    help="Turn on echo for input",
)
def run(local_file, no_stream, input_echo_on):
    try:
        _board.run(local_file, not no_stream, input_echo_on)
    except IOError:
        click.echo(
            f"Failed to find or read input file: {local_file}", err=True
        )

@xkit.command()
def repl():
    print(ANSIEC.FG.MAGENTA + "Entering REPL mode. Press Ctrl + X to exit." + ANSIEC.OP.RESET)

    _board.repl()
    
@xkit.command()
def format():
    print("Formatting...")
    ret = _board.fs_format(_type)
    if ret:
        print(ANSIEC.OP.left() + "Formatting is complete!")
    else:
        print(ANSIEC.OP.left() + "The device type is not supported.")
    return ret

@xkit.command()
def init():    
    if not click.Context(format).invoke(format):
        return 
    
    lib_root = _root_fs + "/lib"

    local = os.path.join(os.path.dirname(__file__), "pop")
    remote = lib_root + "/xnode/pop"
    
    print("Installing the pop library on the board.")
    
    pycache_path = local + "\\__pycache__"
    import shutil
    if os.path.exists(pycache_path):
        shutil.rmtree(pycache_path)
    
    _board.fs_mkdir(lib_root)
    click.Context(put).invoke(put, local=local, remote=remote)
    
    print("The job is done!")


#--------------------------------------------------------------

def main():
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    
    if len(sys.argv) == 2 and sys.argv[1] == "scan":
        scan()
    else:    
        exit_code = xkit()
        sys.exit(exit_code)
	
if __name__ == '__main__':
    main()