from Utilitys import *
clear()
world = get_world_size()
go_to_cords(world // 2, world // 2)
def prep():
	high_point = get_pos_z() + 5
	go_to_cords(0,0)
	for j in range(get_world_size()):
		for i in range(get_world_size()):
			while get_ground_type() != Grounds.Loam and get_pos_z() > high_point - 3:
				dig()
			if get_pos_z() > high_point:
				high_point = get_pos_z()
			move(North)
		move(East)

def get_max_height():
	found_top = False
	while not found_top:
		max_height = get_pos_z()
		for j in range(get_world_size()):
			for i in range(get_world_size()):
				if max_height <= get_pos_z() and get_ground_type() == Grounds.Loam:
					max_height == get_pos_z()
					found_top = True
				else:
					if get_ground_type() != Grounds.Loam and get_hardness() < 5 :
						dig()
				move(North)
			move(East)
	return max_height

def change_implantable(h):
	min_height = get_pos_z()
	go_to_cords(0,0)
	for j in range(get_world_size()):
		for i in range(get_world_size()):
			if get_ground_type() != Grounds.Loam and min_height < get_pos_z():
				dig()
			if get_ground_type() != Grounds.Loam:
				place(Grounds.Dirt)
				if min_height > get_pos_z():
					min_height == get_pos_z()
			move(North)
		move(East)

while get_ground_type() != Grounds.Loam:
	dig()
prep()
for i in range(5):
	get_max_height()
#change_implantable()