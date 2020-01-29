from NSController import Controller

ctr = Controller(); 
## Or use your serial port if you have many
# ctr = Controller('/dev/tty.usbserial-AO0099VT'); 
ctr.A()
ctr.close()