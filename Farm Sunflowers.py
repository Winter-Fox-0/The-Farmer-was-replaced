from Utilitys import * 
clear()
set_world_size(10)
while(True):
	list = []
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Sunflower)
			tap()
			water_tile()
			list.append(((get_pos_x(),get_pos_y()),measure()))
			move(North)
		move(East)
	quick_print(list)
	c = 15
	while len(list) > 0:
		for tile in list[:]:
			cords,q = tile
			if q == c:
				go_to_cords(cords)
				while not can_harvest():
					do_a_flip()
				harvest()
				tap()
		c -= 1
		if c < 7:
			break
		quick_print(list)
	go_to_cords(0,0)
				
	