import serial
import asyncio


class BT:
    def __init__(self):
        self.ser = None
        self.text = None

    def bt_serial(self):
        self.ser = serial.Serial('COM8', 9600, 8, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=8)
        if self.ser.isOpen():
            return True
        else:
            self.ser.close()

    def write_one(self):
        self.ser.write(b'1')
        text = self.ser.readline().decode()
        print(text)

    def write_zero(self):
        self.ser.write(b'0')
        text = self.ser.readline().decode()
        print(text)

    def disconect(self):
        self.ser.close()

    async def read(self):
        # await asyncio.sleep(1)
        await asyncio.sleep(0.1)
        self.ser.write(b'3')
        text = self.ser.readline().decode()
        if text != '\r\n':
            print(text)
            text = text.replace('\r', '')
            text = text.replace('\n', '')
            self.text = text
        elif text == '':
            self.text = text

    async def calibrate(self):
        self.ser.write(b'4')