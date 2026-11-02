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
	home = get_pos()
	commands = get_command()
	for i in commands:
			move(i)
			if get_ground_type() == Grounds.Dynamite:
				dig()
				if measure() == 0:
					check()
	go_to_cords(home)

def get_command():
	
	if at_world_edge(North):
		if at_world_edge(East):
			return [West,South,East]
		elif at_world_edge(West):
			return [South,East,North]
		else:
			return [West,South,East,East,North]
	elif at_world_edge(South):
		if at_world_edge(East):
			return [West,East,North,West]
		elif at_world_edge(West):
			return [East,North,West]
		else:
			return [West,East,East,North,West,West]
	elif at_world_edge(East):
		return [West,South,East,North,North,West]
	elif at_world_edge(West):
		return [South,East,North,North,West]
	else:
		return [West,South,East,East,North,North,West,West]
		
		
		
main()
	