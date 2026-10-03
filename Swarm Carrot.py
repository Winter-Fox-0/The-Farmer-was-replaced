clear()

def work():
	while True:
		if get_ground_type() != Grounds.Soil:
			till()
		if can_harvest():
			harvest()
		plant(Entities.Carrot)
		move(North)
		
for i in range(get_world_size() - 1):
	spawn_drone(work)
	move(East)
work()