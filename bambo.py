clear()
move(North)
till()
while True:
	plant(Entities.Bamboo)
	h = measure()
	move(South)
	for i in range(h):
		if h > get_pos_z():
			place(Grounds.Dirt)
		elif h < get_pos_z():
			dig()
		if i > 0:
			do_a_flip()
	move(North)