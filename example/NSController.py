#!/usr/bin/env python3
import serial
import serial.tools.list_ports
from time import sleep

class Controller:
    def __init__(self,serial_port = None,printout = False):
        if serial_port is None:
            serial_port = Controller.find_port()
        self.ser = serial.Serial(serial_port, 9600)
        self.buttondelay = 0.15
        self.printout = printout

    @staticmethod
    def find_port():
        ports = [
            p.device
            for p in serial.tools.list_ports.comports()
            if p.vid is not None and p.pid is not None
        ]
        if not ports:
            raise IOError('No device found')
        if len(ports) > 1:
            print('Found multiple devices, using the first')
        print(f'Using port: {ports[0]}')
        return ports[0]

    def send(self, msg, duration=0.1):
        if self.printout:
            print(msg)
        self.ser.write(f'{msg}\r\n'.encode('utf-8'));
        sleep(duration)
        self.ser.write(b'RELEASE\r\n');
        sleep(self.buttondelay)

    def write(self,msg):
        self.ser.write(f'{msg}\r\n'.encode('utf-8'));

    def pause(self,duration):
        sleep(duration)

    def close(self):
        sleep(0.5)
        self.ser.close()
        print('Connection closed!')

    # Botton
    def A(self):
        self.send('Button A')

    def B(self):
        self.send('Button B')

    def X(self):
        self.send('Button X')

    def Y(self):
        self.send('Button Y')

    def L(self):
        self.send('Button L')

    def R(self):
        self.send('Button R')

    def ZL(self):
        self.send('Button ZL')

    def ZR(self):
        self.send('Button ZR')

    def p(self):
        self.send('Button PLUS')

    def m(self):
        self.send('Button MINUS')

    def h(self):
        self.send('Button HOME')

    def c(self):
        self.send('Button CAPTURE')

    def l(self):
        self.send('HAT LEFT')

    def u(self):
        self.send('HAT TOP')

    def r(self):
        self.send('HAT RIGHT')

    def d(self):
        self.send('HAT BOTTOM')

    # LEFT STICK
    def ls_l(self,duration):
        self.send('LX MIN',duration)

    def ls_r(self,duration):
        self.send('LX MAX',duration)

    def ls_d(self,duration):
        self.send('LY MAX',duration)

    def ls_u(self,duration):
        self.send('LY MIN',duration)

    # RIGHT STICK
    def rs_l(self,duration):
        self.send('RX MIN',duration)

    def rs_r(self,duration):
        self.send('RX MAX',duration)

    def rs_d(self,duration):
        self.send('RY MAX',duration)

    def rs_u(self,duration):
        self.send('RY MIN',duration)

    # DPAD
    def d_l(self,duration):
        self.send('HAT LEFT',duration)

    def d_r(self,duration):
        self.send('HAT RIGHT',duration)

    def d_d(self,duration):
        self.send('HAT BOTTOM',duration)

    def d_u(self,duration):
        self.send('HAT TOP',duration)

    # Multiple Keypressing
    def LR(self,duration = 0.1):
        self.write('Button L');
        self.write('Button R');
        sleep(duration)
        self.ser.write(b'RELEASE\r\n');
        sleep(self.buttondelay)


    # DPAD_UP + B + X
    def AccessBackupSave(self):
        self.write('HAT TOP');
        self.write('Button B');
        self.write('Button X');
        sleep(0.1)
        self.ser.write(b'RELEASE\r\n');
        sleep(self.buttondelay)

    #Multi
    def quit_app(self):
        self.h()
        sleep(0.5)
        self.X()
        self.A()

    def enter_app(self):
        self.A()
        sleep(1)
        self.A()