from Utilitys import *

def main():
	clear()
	jump(Unlocks.Pyramid)
	uncover()
	while get_ground_type() != Grounds.Red_block:
		uncover()
	found_at = follow_path()
	level_to_sandstone()
	go_to_cords(found_at)
	steps = find_center()
	h = get_pos_z()
	for i in range(steps):
		move(South)
		move(West)
	repair(steps,h + 1)
	place(Grounds.Sand)
	do_a_flip()
	harvest()


def uncover():
	height = get_pos_z() - 1
	for i in range(WORLD_SIZE):
		if num_drones() < max_drones():
			spawn_drone(search, height)
		else:
			search(height)
		move(East)
	while num_drones() > 1:
		pass

def search(h):
	global found_at
	for i in range(WORLD_SIZE):
		while get_pos_z() > h and get_ground_type() != Grounds.Sand:
			dig()
		if get_ground_type() == Grounds.Sand:
			found_at = get_pos_x()
			go_to_cords(0,0)
			if get_ground_type() != Grounds.Red_block:
				place(Grounds.Red_block)
				go_to_x(found_at)
				place(Grounds.Blue_block)
			else:
				break
		move(North)
		
def dig_out(h):
	for i in range(WORLD_SIZE):
		while get_pos_z() > h and get_ground_type() != Grounds.Sand:
			dig()
		move(North)

def level(h):
	go_to_cords(0,0)
	for i in range(WORLD_SIZE):
		if num_drones() < max_drones():
			spawn_drone(dig_out, h)
		else:
			dig_out(h)
		move(East)
	while num_drones() > 1:
		pass

def follow_path():
	while get_ground_type() != Grounds.Blue_block:
		move(East)
	while get_ground_type() != Grounds.Sand:
		move(North)
	return (get_pos_x(),get_pos_y())

def level_to_sandstone():
	while get_ground_type() != Grounds.Limestone:
		dig()
	level(get_pos_z())

def find_center():
	while get_ground_type() == Grounds.Sand or get_ground_type() == Grounds.Limestone:
		move(West)
	move(East)
	left = get_pos_x()
	while get_ground_type() == Grounds.Sand or get_ground_type() == Grounds.Limestone:
		move(East)
	move(West)
	right = get_pos_x()
	center = (right + left) // 2
	go_to_x(center)
	while get_ground_type() == Grounds.Sand or get_ground_type() == Grounds.Limestone:
		move(South)
	move(North)
	down = get_pos_y()
	while get_ground_type() == Grounds.Sand or get_ground_type() == Grounds.Limestone:
		move(North)
	move(South)
	up = get_pos_y()
	height = right - center
	center = (center,(up + down)// 2)
	go_to_cords(center)
	return height

def lay_blocks(c,h):
	for i in range(c):
		while get_pos_z() < h:
			place(Grounds.Sand)
		move(North)
	while get_pos_z() < h:
			place(Grounds.Sand)


def repair(count,h):
	if count == 0:
		return
	for i in range(count * 2):
		spawn_drone(lay_blocks, count * 2,h)
		move(East)
	spawn_drone(lay_blocks, count * 2,h)
	for i in range(count * 2):
		move(West)
	move(North)
	move(East)
	while num_drones() > 1:
		pass
	repair (count - 1,h + 1)
	
if __name__ == "__main__":
	main()
