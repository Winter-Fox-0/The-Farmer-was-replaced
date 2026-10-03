clear()

def work():
	while True:
		if can_harvest():
			harvest()
		move(North)
		
for i in range(get_world_size() - 1):
	spawn_drone(work)
	move(East)
work()
	