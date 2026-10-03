from Helpers import *
from Constents import *
mushrooms = []
height_map = []
Go_to_cords(0,WORLD_MAX_COORD)
for i in range(WORLD_SIZE):
	m = []
	h = []
	for j in range(WORLD_SIZE):
		m.append(measure())
		h.append(get_pos_z())
		move(East)
	mushrooms.append(m)
	height_map.append(h)
	move(South)

quick_print("map")
quick_print(mushrooms)
quick_print("heights")
quick_print(height_map)
		
		