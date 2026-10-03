from Utilitys import *

def flatten(depth):
	for i in range(get_world_size()):
		while get_pos_z() > depth:
			dig()
		move(North)
def main():
	clear()
	jump(Unlocks.Dynamite)
	while not get_ground_type() == Grounds.Dynamite:
		dig()
	height = get_pos_z()
	for i in range(get_world_size()):
		if num_drones() < max_drones():
			spawn_drone(flatten, height)
		else:
			flatten(height)
		move(East)
	go_to_cords(15,15)
	while num_drones() > 1:
		pass
	dig()
	check()
	go_to_cords(0,31)
			
def check():
	commands = [West,South,East,East,North,North,West,West]
		
	for i in commands:
		move(i)
		if get_ground_type() == Grounds.Dynamite:
			dig()
			if measure() == 0:
				check()
	move(East)
	move(South)
	
main()
	