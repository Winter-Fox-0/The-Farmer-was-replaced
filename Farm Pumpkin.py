from Utilitys import *
clear()
while True:
	dead = []
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Pumpkin)
			water_tile()
			move(North)
		move(East)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if not can_harvest():
				dead.append((get_pos_x(),get_pos_y()))
				plant(Entities.Pumpkin)
			move(North)
		move(East)		
	done = False
	while not done:
		checked = []
		for i in dead:
			go_to_cords(i)
			if not can_harvest():
				plant(Entities.Pumpkin)
				checked.append(i)
		if len(checked) == 0:
			done = True
		dead = checked
	go_to_cords(0,0)
	harvest()	