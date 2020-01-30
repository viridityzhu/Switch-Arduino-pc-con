from NSController import Controller

# last pokemon box should be a empty box, the target/last map destination should be the Day Care in Wild Area
# last X menu item should be "Map", egg should be ready to pick
# Empty your party, and on your bike

ctr = Controller()
cycle = 20			# Egg cycle
hatchingtime = -1	# Hatching time in second (18 to prevent freezing)

## Prepare
# ctr.quit_app()
# ctr.pause(5)
# ctr.enter_app()
# ctr.pause(15)
# ctr.A()
# ctr.pause(10)
# ctr.X()
# ctr.pause(1)
# ctr.d()
# ctr.B()
# ctr.pause(2)

for i in range(6):
	for j in range(5):
		ctr.buttondelay = 0.1
		# Fly to Day Care in Wild Area
		ctr.X()
		ctr.pause(1)
		ctr.A()
		ctr.pause(2.5)
		ctr.A()
		ctr.pause(0.5)
		ctr.A()
		ctr.pause(5)

		# Go back to Day Care
		ctr.ls_d(0.7)
		ctr.ls_r(0.2)
		ctr.pause(0.5)

		print(f"Picking {i * 5 + j + 1}th egg(s)")
		ctr.A()
		ctr.pause(0.4)
		ctr.A()
		ctr.pause(0.4)
		ctr.A()
		ctr.pause(3)
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

		if j != 0:
			for cnt in range(hatchingtime):
				ctr.B()
				ctr.pause(0.9)

	for c in range(cycle * 2):
		ctr.ls_d(0.5)
		ctr.B()
		ctr.ls_r(0.5)
		ctr.ls_u(0.6)
		ctr.ls_l(0.5)

	for cnt in range(hatchingtime):
		ctr.B()
		ctr.pause(0.9)

	# Put babies in the box
	ctr.buttondelay = 0.1
	ctr.X()
	ctr.pause(1)
	ctr.r()
	ctr.u()
	ctr.A()
	ctr.pause(2)
	ctr.R()
	ctr.pause(2)
	ctr.l()
	ctr.d()
	ctr.Y()
	ctr.Y()
	ctr.A()
	ctr.d()
	ctr.d()
	ctr.d()
	ctr.d()
	ctr.A()
	ctr.r()
	ctr.d()
	ctr.d()
	ctr.d()
	ctr.d()
	ctr.A()
	ctr.pause(0.5)
	ctr.A()
	ctr.pause(0.5)
	ctr.B()
	ctr.B()
	ctr.pause(2)
	ctr.B()
	ctr.pause(1.5)

	# Back to "map" and quit
	ctr.d()
	ctr.l()
	ctr.B()
	ctr.pause(1.5)

ctr.close()