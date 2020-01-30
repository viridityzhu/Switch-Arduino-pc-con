from NSController import Controller

ctr = Controller()
N = 30	# Number of Pokemon in the box

for i in range(N):
	print(f'{i+1}/{N}')
	ctr.A()
	ctr.pause(0.1)
	ctr.u()
	ctr.u()
	ctr.A()
	ctr.pause(1)
	ctr.u()
	ctr.A()
	ctr.pause(1.3)
	ctr.A()
	ctr.pause(0.1)
	ctr.r()
	ctr.pause(0.1)
	# Change row
	if i % 6 == 5:
		ctr.r()
		ctr.d()

ctr.close()