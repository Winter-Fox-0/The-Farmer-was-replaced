from Utilitys import *
clear()
set_world_size(8)
def farm_bamboo():
	move(North)
	till()
	plant(Entities.Bamboo)
	while True:
		for i in range(3):
			m = measure()
			move(South)
			for i in range(m - get_hover()):
				do_a_flip()
			hover(m)
			move(North)
		move(South)
		hover(1)
		move(North)
for y in range(4):
	for x in range(8):
		if num_drones() < max_drones():
			spawn_drone(farm_bamboo)
		else:
			farm_bamboo()
		move(East)
	go_to_x(0)
	move_steps(North,2)