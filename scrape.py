def unearth():
	for i in range(get_world_size()):
		if not get_ground_type() == Grounds.Dynamite:
			dig()
		move(North)

for i in range(8):
	drone_list = []
	for i in range(get_world_size()):
		if max_drones() > num_drones():
			drone_list.append(spawn_drone(unearth))
			move(East)
		else:
			unearth()
			move(East)
	for i in drone_list:
		wait_for(i)