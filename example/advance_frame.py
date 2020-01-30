from NSController import Controller

ctr = Controller()
## Or use your serial port if you have many
# ctr = Controller('/dev/tty.usbserial-AO0099VT');

# Advance raid seed 3 times
for i in range (3):
	# enter the raid
	ctr.A()
	ctr.pause(2)

	# quit the game and go to settings
	ctr.h()
	ctr.pause(1)
	ctr.d()
	for i in range(4):
		ctr.r()
	ctr.A()
	ctr.d(2)
	ctr.r()
	for i in range(4):
		ctr.d()
	ctr.A()

	# change the date
	ctr.d(0.4) # Scroll down to bottom
	ctr.A()
	ctr.r()
	ctr.r()
	ctr.u()
	ctr.r(0.4)
	ctr.A()

	# enter the game, quit the raid
	ctr.h()
	ctr.pause(0.2)
	ctr.u()
	ctr.A()
	ctr.pause(1)
	ctr.B()
	ctr.pause(0.5)
	ctr.A()
	ctr.pause(4.5)

	# collect Watts
	ctr.A()
	ctr.pause(0.1)
	ctr.A()
	ctr.pause(0.1)
	ctr.A()
	ctr.pause(2)

ctr.close()