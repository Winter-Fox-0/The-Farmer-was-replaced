from Utilitys import *

def main():
	hit_clay = False
	go_to_y(0)
	spots = [1,4,7,10,13,18,21,24,27,30]
	for i in spots:
		go_to_x(i)
		if get_ground_type() == Grounds.Clay:
			hit_clay = True
		spawn_drone(command)
	do_a_flip()
	if hit_clay:
		check_for_break(True)
		while num_drones() > 1:
			do_a_flip()

def command():
	found = False
	quit = False
	while True:
		if get_ground_type() == Grounds.Clay:
			if check_for_break(True):
					break
			else:
				while num_drones() > 1:
					pass
				quit = True
				break
		wait_for_drone_count(10)
		for i in range(get_world_size()):
			if ground_in_list([Grounds.Grassland,Grounds.Dirt]):
				dig()
				tap()
			if check_surrounding(Grounds.Coal):
				if check_for_break(True):
					break
				else:
					while num_drones() > 1:
						pass
					found = True
					break
							
			move(North)
		do_a_flip()
		if check_for_break():
			break
		else:
			spawn_drone(waiter)
	if found:
		spawn_drone(harvest)
	elif quit:
		spawn_drone(main)
	elif get_ground_type() == Grounds.Clay:
		pass

def ground_in_list(l):
	ground = get_ground_type()
	for i in l:
		if i == ground:
			return True
	return False

def wait_for_drone_count(c) -> Bool:
	while num_drones() < c + 1:
		pass
	while num_drones() > c:
		pass

def waiter():
	move(North)
	do_a_flip()

def check_for_break(create = False):
	here = create_cords()
	go_to_cords(0,0)
	if get_ground_type() == Grounds.Red_Block:
		go_to_cords(here)
		return True
	else:
		if create:
			place(Grounds.Red_Block)
		go_to_cords(here)
		return False
		
def harvest():
	flatten()
	if get_ground_type() != Grounds.Coal:
		temp()
	go_to_center()
	while get_ground_type(South) == Grounds.Coal:
		move(South)
	mine_main()
	while num_drones() > 1:
		pass
	main()

def flatten():
	height = get_pos_z()
	home = create_cords()
	go_to_cords(0,0)
	for i in range(get_world_size()):
		if num_drones() < max_drones():
			spawn_drone(level,height)
		else:
			level(height)
		move(East)
	go_to_cords(home)
	while num_drones() > 1:
		pass

def level(h):
	for i in range(get_world_size()):
		while get_pos_z() > h:
			dig()
		move(North)

def check_surrounding(check_for):
	Directions = [North,East,South,West]
	if get_ground_type() == check_for:
		return True
	for i in Directions:
		if get_ground_type(i) == check_for:
			return True
	return False
	
def create_cords():
	return (get_pos_x(),get_pos_y())
	
def temp():
	Directions = [North,East,South,West]
	for i in Directions:
		if get_ground_type(i) == Grounds.Coal:
			move(i)
			return

def mine_east(script):
		spawned= False
		move(East)
		while get_ground_type() == Grounds.Coal:
			if get_ground_type(East) == Grounds.Coal and not spawned:
				spawn_drone(mine_east,mine_east)
				spawned = True
			dig()
			tap()
			place(Grounds.Dirt)
			move(North)
			
def mine_west(script):
	spawned = False
	move(West)
	while get_ground_type() == Grounds.Coal:
		if get_ground_type(West) == Grounds.Coal and not spawned:
			spawn_drone(mine_west,mine_west)
			spawned = True
		dig()
		tap()
		place(Grounds.Dirt)
		move(North)	

def mine_main():
	spawned_east = False
	spawned_west = False
	while get_ground_type() == Grounds.Coal:
		if get_ground_type(East) == Grounds.Coal and not spawned_east:
			spawn_drone(mine_east,mine_east)
			spawned_east = True
		if get_ground_type(West) == Grounds.Coal and not spawned_west:
			spawn_drone(mine_west,mine_west)
			spawned_west = True
		dig()
		tap()
		place(Grounds.Dirt)
		move(North)

def go_to_center():
	while get_ground_type(East) == Grounds.Coal:
		move(East)
	max = get_pos_x()
	while get_ground_type(West) == Grounds.Coal:
		move(West)
	min = get_pos_x()
	go_to_x((max + min) // 2)
	
if __name__ == "__main__":
	clear()
	main()