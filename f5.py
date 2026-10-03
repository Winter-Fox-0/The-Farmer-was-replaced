from Utilitys import *
#clear()
world = get_world_size()
go_to_cords(0,0)

def get_max_height():
	height = -34
	for j in range(get_world_size()):
		for i in range(get_world_size()):
			if get_ground_type() == Grounds.Rock:
				#dig()
				if get_ground_type() != Grounds.Loam:
					place(Grounds.Dirt)
			move(North)
		move(East)




get_max_height()
