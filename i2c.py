#!/usr/bin/python

import time
import math
import smbus


# ============================================================================
# PCA9685 16 ͨ路 PWM 驱动控制
# ============================================================================

class PCA9685:
    # Registers/etc.
    __SUBADR1 = 0x02
    __SUBADR2 = 0x03
    __SUBADR3 = 0x04
#  模式和频率设置的地址位
    __MODE1 = 0x00
    __PRESCALE = 0xFE
#主要使用的PWM输出口的地址位
    __LED0_ON_L = 0x06
    __LED0_ON_H = 0x07
    __LED0_OFF_L = 0x08
    __LED0_OFF_H = 0x09


    __ALLLED_ON_L = 0xFA
    __ALLLED_ON_H = 0xFB
    __ALLLED_OFF_L = 0xFC
    __ALLLED_OFF_H = 0xFD
#初始化函数,这里是默认A0-A5是拉起,所以地址为0x40,debug选项是因为行命令运行python文件不能debug所以通过这种方式来检查程序
#运行的正确性,了解程序运行情况
    def __init__(self, address=0x40, debug=False):
        self.bus = smbus.SMBus(0) #设置总线,这里选择27和28引脚所以选择总线0
        self.address = address  #设置起始地址,后面会用到发送数据
        self.debug = debug
        if (self.debug):
            print("Reseting PCA9685")
        self.write(self.__MODE1, 0x00)

    def write(self, reg, value):
        "将8 位值写入指定的寄存器地址"
        self.bus.write_byte_data(self.address, reg, value)#只发送一个数据， value是数据
        if (self.debug):
            print("I2C: Write 0x%02X to register 0x%02X" % (value, reg))

    def read(self, reg):
        " I2C 器件读取无符号字节"
        result = self.bus.read_byte_data(self.address, reg)
        if (self.debug):
            print("I2C: Device 0x%02X returned 0x%02X from reg 0x%02X" % (self.address, result & 0xFF, reg))
        return result

    def setPWMFreq(self, freq):
        "设置 PWM 频率"
        prescaleval = 25000000.0  # 25MHz
        prescaleval /= 4096.0  # 12-bit
        prescaleval /= float(freq)
        prescaleval -= 1.0
        if (self.debug):
            print("Setting PWM frequency to %d Hz" % freq)
            print("Estimated pre-scale: %d" % prescaleval)
        prescale = math.floor(prescaleval + 0.5)
        if (self.debug):
            print("Final pre-scale: %d" % prescale)

        oldmode = self.read(self.__MODE1);
        newmode = (oldmode & 0x7F) | 0x10  # sleep 保证PWM都关闭的情况下，sleep端口
        self.write(self.__MODE1, newmode)  # go to sleep
        self.write(self.__PRESCALE, int(math.floor(prescale)))
        self.write(self.__MODE1, oldmode)
        time.sleep(0.005)
        self.write(self.__MODE1, oldmode | 0x80)

    def setPWM(self, channel, on, off):
        "设置单个 PWM 通道,channel=通道位"
        self.write(self.__LED0_ON_L + 4 * channel, on & 0xFF)
        self.write(self.__LED0_ON_H + 4 * channel, on >> 8)
        self.write(self.__LED0_OFF_L + 4 * channel, off & 0xFF)
        self.write(self.__LED0_OFF_H + 4 * channel, off >> 8)
        if (self.debug):
            print("channel0: %d  LED_ON: %d LED_OFF: %d" % (channel, on, off))

    def setServoPulse(self, channel, pulse):
        "设置伺服脉冲,PWM频率必须设置为50HZ"
        pulse = pulse * 4096 / 20000  # PWM频率为50HZ，周期为20000us 
        self.setPWM(channel, 0, pulse)

    def open(self, pulse):
        pwm.setServoPulse(15, 0)
        time.sleep(0.5)
        pwm.setServoPulse(0, pulse)
    def close(self,channel,pulse):
        pwm.setServoPulse(0, 0)
        time.sleep(0.5)
        pwm.setServoPulse(15, pulse)
        time.sleep(1)
        pwm.setServoPulse(15, 0)

if __name__ == '__main__':

    pwm = PCA9685(0x40, debug=True)
    pwm.setPWMFreq(50)
    while True:
        # setServoPulse(2,2500)

        for i in range(500, 2500, 10):
            pwm.setServoPulse(0, i)
            time.sleep(0.02)

        for i in range(2500, 500, -10):
            pwm.setServoPulse(0, i)
            time.sleep(0.02)