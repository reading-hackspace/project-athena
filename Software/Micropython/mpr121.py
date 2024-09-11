from micropython import const
from time import sleep_ms

ADDRESS = const(0x5a)

class MPR121:    
    def __init__(self, i2c):
        self.i2c = i2c
        self.reset()
    
    def cmd(self, reg, value):
        self.i2c.writeto_mem(ADDRESS,reg,bytes([value]))
        
    def reset(self):
        self.cmd(0x80, 0x63)
        sleep_ms(1)
        self.cmd(0x5e, 0)
        self.set_thresholds(12,6)
        rst = [0x01,0x01,0x0e,0,0x01,0x05,0x01,0,0,0,0]
        for i in range(43, 54):
            self.cmd(i, rst[i-43])
        self.cmd(0x5b, 0)
        self.cmd(0x5c, 0x10)
        self.cmd(0x5d, 0x20)
        self.cmd(0x5e, 0x8f)
    
    def touched(self):
        self.cmd(0,0)
        lower = self.i2c.readfrom(ADDRESS, 2)
        return lower[0] + (lower[1]<<8)
                
    def set_thresholds(self, touch, release):
        for i in range(12):
            self.cmd(0x41 + 2*i, touch)
            self.cmd(0x42 + 2*i, release)