from Utilitys import *

world = get_world_size()
clear()
go_to_cords(world // 2, world // 2)

def rice_prep():
	go_to_cords(0,0)
	for j in range(get_world_size()):
		for i in range(get_world_size()):
			while get_ground_type() != Grounds.clay:
				dig()
			move(North)
		move(East)

def rice_plant():
	go_to_cords(0,0)
	for j in range(get_world_size()):
		for i in range(get_world_size()):
			plant(Entities.Rice)
			move(North)
		move(East)

def harvest_rice():
	for j in range(get_world_size()):
		for i in range(get_world_size()):
			while not can_harvest():
				pass
			harvest()
			move(North)
		move(East)
	
while True:
	while get_ground_type() != Grounds.clay and get_ground_type() != Grounds.Dry_Rice_Terrace:
		dig()
	rice_prep()
	rice_plant()
	harvest_rice()
	go_to_cords(world // 2, world // 2)