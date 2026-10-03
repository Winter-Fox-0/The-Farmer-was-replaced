from Utilitys import *
clear()
set_world_size(5)
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)
			water_tile()
			move(North)
		move(East)
	def sort(dir):
		opposite = {North:South,East:West,South:North,West:East}
		opp_dir = opposite[dir]
		if dir == North or dir == South:
			while not get_pos_y() == get_world_size() - 1:
				move(dir)
				while measure(opp_dir) > measure() and not get_pos_y() == 0:
					swap(opp_dir)
					move(opp_dir)
			move(dir)
		else:
			while not get_pos_x() == get_world_size() - 1:
				move(dir)
				while measure(opp_dir) > measure() and not get_pos_x() == 0:
					swap(opp_dir)
					move(opp_dir)
			move(dir)
	for i in range(get_world_size()):
		sort(East)
		move(North)
	for i in range(get_world_size()):
		sort(North)
		move(East)
	harvest()