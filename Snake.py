from Utilitys import *
from Snake_paths import six_path
length = 1
	
def snake_move(i):
	global length
	target_x,target_y = i
	if target_x != get_pos_x():
		if target_x > get_pos_x():
			move(East)
		else:
			move(West)
	elif target_y != get_pos_y():
		if target_y > get_pos_y():
			move(North)
		else:
			move(South)
	if get_entity_type() == Entities.Apple:
		length += 1
		quick_print(length)
clear()
set_world_size(6)
while True:
	change_hat(Hats.Gold_Hat)
	go_to_cords(0,0)
	length = 1
	change_hat(Hats.Dinosaur_Hat)
	while length < (get_world_size() ** 2):
		for i in six_path:
			snake_move(six_path[i])