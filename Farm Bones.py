clear()
while True:
	change_hat(Hats.Dinosaur_Hat)
	count = 1
	
	
	def snake_move(Dir):
		
		if get_entity_type() == Entities.Apple:
			global count
			count += 1
			quick_print(count)
		move(Dir)
	
	while count < (get_world_size() ** 2):
		while can_move(North):
			snake_move(North)
		while can_move(East):
			snake_move(East)
		while can_move(South):
			snake_move(South)
			if get_pos_y() % 2 == 0:
				while get_pos_x() > 1 and can_move(West):
					snake_move(West)
			else:
				while can_move(East):
					snake_move(East)
		snake_move(West)