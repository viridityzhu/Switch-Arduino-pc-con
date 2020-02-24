from NXController import Controller

# last X menu item should be "Map", egg should be ready to pick

ctr = Controller()
ctr.LS()
cycle = 20			# Egg cycle
slot = 4
N = 5

for i in range(N):
	ctr.buttondelay = 0.1
	# Fly to Day Care in Wild Area
	ctr.X()
	ctr.pause(1)
	ctr.A()
	ctr.pause(2.5)
	ctr.A()
	ctr.pause(0.5)
	ctr.A()
	ctr.pause(4.8)

	# Go back to Day Care
	ctr.ls_d(0.7)
	ctr.ls_r(0.2)
	ctr.pause(0.5)

	print(f"Picking {i + 1}th egg(s)")
	ctr.A()
	ctr.pause(1)
	ctr.A()
	ctr.pause(3)
	ctr.A()
	ctr.pause(2)
	ctr.A()
	ctr.pause(1.5)
	ctr.A()
	ctr.pause(2.2)
	for jj in range(slot):
		ctr.d()
	ctr.A()
	ctr.pause(2.5)
	ctr.A()
	ctr.pause(1.5)
	ctr.A()
	ctr.pause(0.1)

	# Move forward, remove the delay during hatching
	ctr.buttondelay = 0
	ctr.ls_u(3)
	ctr.ls_r(2)

	for c in range(cycle):
		ctr.ls_d(0.5)
		ctr.B()
		ctr.ls_r(0.5)
		ctr.ls_u(0.6)
		ctr.ls_l(0.5)

	slot = 1 if slot == 5 else slot + 1

ctr.close()