clear()
while(True):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_pos_x() % 2 == get_pos_y() % 2:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			move(North)
		move(East)
	