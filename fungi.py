from Utilitys import *
clear()
jump(Unlocks.Mushrooms)
for i in range(get_world_size()):
	if num_drones() < max_drones():	
		spawn_drone(act_column,dig_to_block,[Grounds.Mushroom])
	else:
		act_column(dig_to_block,[Grounds.Mushroom])
	move(East)
go_to_cords(0,0)
while num_drones() > 1:
	pass
dig()
while Grounds.Mushroom == get_ground_type():
	for i in range(get_world_size() // 2):
		for i in range(get_world_size() - 1):
			move(North)
			push(South)
		move(East)
		push(West)
		for i in range(get_world_size() - 1):
			move(South)
			push(North)
		move(East)
		push(West)
