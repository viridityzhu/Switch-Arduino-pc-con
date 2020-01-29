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

    def write(self,msg):
        self.ser.write(f'{msg}\r\n'.encode('utf-8'));

    def release(self):
        self.ser.write(b'RELEASE\r\n');

    # negative or zero duration to hold the button
    def send(self, msg, duration = 0.1):
        if self.printout:
            print(msg)
        self.write(msg);
        if duration > 0:
            sleep(duration)
            self.release();
            sleep(self.buttondelay)

    def pause(self,duration):
        sleep(duration)

    def close(self):
        self.release();
        sleep(0.5)
        self.ser.close()
        print('Connection closed!')

    # Botton
    def A(self,duration = 0.1):
        self.send('Button A',duration)

    def B(self,duration = 0.1):
        self.send('Button B',duration)

    def X(self,duration = 0.1):
        self.send('Button X',duration)

    def Y(self,duration = 0.1):
        self.send('Button Y',duration)

    def L(self,duration = 0.1):
        self.send('Button L',duration)

    def R(self,duration = 0.1):
        self.send('Button R',duration)

    def ZL(self,duration = 0.1):
        self.send('Button ZL',duration)

    def ZR(self,duration = 0.1):
        self.send('Button ZR',duration)

    def p(self,duration = 0.1):
        self.send('Button PLUS',duration)

    def m(self,duration = 0.1):
        self.send('Button MINUS',duration)

    def h(self,duration = 0.1):
        self.send('Button HOME',duration)

    def c(self,duration = 0.1):
        self.send('Button CAPTURE',duration)

    # DPAD
    def l(self,duration = 0.1):
        self.send('HAT LEFT',duration)

    def u(self,duration = 0.1):
        self.send('HAT TOP',duration)

    def r(self,duration = 0.1):
        self.send('HAT RIGHT',duration)

    def d(self,duration = 0.1):
        self.send('HAT BOTTOM',duration)

    # LEFT STICK
    def ls_l(self,duration = 0.1):
        self.send('LX MIN',duration)

    def ls_r(self,duration = 0.1):
        self.send('LX MAX',duration)

    def ls_d(self,duration = 0.1):
        self.send('LY MAX',duration)

    def ls_u(self,duration = 0.1):
        self.send('LY MIN',duration)

    # RIGHT STICK
    def rs_l(self,duration = 0.1):
        self.send('RX MIN',duration)

    def rs_r(self,duration = 0.1):
        self.send('RX MAX',duration)

    def rs_d(self,duration = 0.1):
        self.send('RY MAX',duration)

    def rs_u(self,duration = 0.1):
        self.send('RY MIN',duration)

    # Multiple Keypresses
    def LR(self,duration = 0.1):
        self.L(-1)
        self.R(-1)
        if duration > 0:
            sleep(duration)
            self.release();
            sleep(self.buttondelay)

    # DPAD_UP + B + X
    def AccessBackupSave(self,duration = 0.1):
        self.u(-1)
        self.B(-1)
        self.X(-1)
        if duration > 0:
            sleep(duration)
            self.release();
            sleep(self.buttondelay)

    # other functions
    def quit_app(self):
        self.h()
        sleep(0.5)
        self.X()
        self.A()

    def enter_app(self):
        self.A()
        sleep(1)
        self.A()