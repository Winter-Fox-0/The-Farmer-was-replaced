from Utilitys import *
clear()

def work():
	while True:
		if can_harvest():
			harvest()
		if get_pos_x() % 2 == get_pos_y() % 2:
			plant(Entities.tree)
		else:
			plant(Entities.Bush)
		water_tile()
		move(North)
		
for i in range(get_world_size() - 1):
	spawn_drone(work)
	move(East)
work()
	