import sys
import time
import json
import uos
import machine 
from micropython import const

def sqrt(x, epsilon=1e-10):
    guess = x / 2.0

    op_limit = 5
    while abs(guess * guess - x) > epsilon and op_limit:
        guess = (guess + x / guess) / 2.0
        op_limit -= 1

    return guess

def abs(x):
  return x if x >= 0 else -x

def rand(size=4):
    return int.from_bytes(uos.urandom(size), "big")

def map(x, min_i, max_i, min_o, max_o):
    return (x - min_i) * (max_o - min_o) / (max_i - min_i) + min_o


def WDT(timeout):
    return machine.WDT(0, timeout)


class ANSIEC:
    class FG:
        BLACK = "\u001b[30m"
        RED = "\u001b[31m"
        GREEN = "\u001b[32m"
        YELLOW = "\u001b[33m"
        BLUE = "\u001b[34m"
        MAGENTA = "\u001b[35m"
        CYAN = "\u001b[36m"
        WHITE = "\u001b[37m"
        
        @classmethod
        def rgb(cls, r, g, b): return "\u001b[38;2;{};{};{}m".format(r, g, b)

    class BG:
        BLACK = "\u001b[40m"
        RED = "\u001b[41m"
        GREEN = "\u001b[42m"
        YELLOW = "\u001b[43m"
        BLUE = "\u001b[44m"
        MAGENTA = "\u001b[45m"
        CYAN = "\u001b[46m"
        WHITE = "\u001b[47m"
        
        @classmethod
        def rgb(cls, r, g, b): return "\u001b[48;2;{};{};{}m".format(r, g, b)

    class OP:
        RESET = "\u001b[0m"
        BOLD = "\u001b[1m"
        UNDER_LINE = "\u001b[4m"
        REVERSE = "\u001b[7m"
        CLEAR = "\u001b[2J"
        CLEAR_LINE = "\u001b[2K"
        UP = "\u001b[1A"
        DOWN = "\u001b[1B"
        RIGHT = "\u001b[1C"
        LEFT = "\u001b[1D"
        NEXT_LINE = "\u001b[1E"
        PREV_LINE = "\u001b[1F"
        TOP = "\u001b[0;0H"
        
        @classmethod
        def to(cls, row, colum):
            return "\u001b[{};{}H".format(row, colum)

class SlipUart:
    SLIP_END = const(b'\xC0')		# dec: 192
    SLIP_ESC = const(b'\xDB')		# dec: 219
    SLIP_ESC_END = const(b'\xDC')	# dec: 220
    SLIP_ESC_ESC = const(b'\xDD')	# dec: 221
    
    @classmethod
    def read(cls):        
        started = False
        skip= False
        data = b''
        while True:
            char = sys.stdin.buffer.read(1)
            if not skip:
                if char == cls.SLIP_END:
                    if not started:
                        started = True
                    else:                                  
                        data.replace(cls.SLIP_ESC + cls.SLIP_ESC_END, cls.SLIP_END).replace(cls.SLIP_ESC + cls.SLIP_ESC_ESC, cls.SLIP_ESC)        
                        break
                else:
                    if not started:
                        skip = True
                    else:
                        data += char
            else:
                if char == cls.SLIP_END:
                    skip = False
        
        return json.loads(data.decode()) 
                        
    @classmethod
    def write(cls, value):   
        data = bytes(json.dumps(value).encode())
        sys.stdout.buffer.write(cls.SLIP_END + data.replace(cls.SLIP_ESC, cls.SLIP_ESC + cls.SLIP_ESC_ESC).replace(cls.SLIP_END, cls.SLIP_ESC + cls.SLIP_ESC_END) + cls.SLIP_END)

            
class Led():
    def __init__(self):
        self.__led = machine.Pin(9, machine.Pin.OUT, value=1)
    
    def on(self):
        self.__led.value(0)
        
    def off(self):
        self.__led.value(1)
    
    def state(self):
        return not self.__led.value()


class Battery(machine.ADC):
    def __init__(self):
        super().__init__(2)

    def read(self):
        return round(((super().read() * 3.3 / 4095) * (3.2/2)), 1)


class Bright:
    __BH1750_ADDR = const(0x23)
    
    def __init__(self):
        self.__i2c = machine.I2C(1)
        
        self.__i2c.writeto(self.__BH1750_ADDR, bytes([0x01]))
        self.__i2c.writeto(self.__BH1750_ADDR, bytes([0x07]))
        
    def __del__(self):
        self.__i2c.writeto(self.__BH1750_ADDR, bytes([0x00]))

    def scan(self):
        return self.__BH1750_ADDR in self.__i2c.scan()
            
    def read(self):
        self.__i2c.writeto(self.__BH1750_ADDR, bytes([0x21]))
        time.sleep_ms(180)
            
        data = self.__i2c.readfrom(self.__BH1750_ADDR, 2)
        return round((data[0] << 8 | data[1]) / (1.2 * 2))
