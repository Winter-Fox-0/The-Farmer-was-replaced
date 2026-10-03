from Utilitys import *
min_x = 0
max_x = get_world_size()
min_y = 0
max_y = get_world_size()
jump(Unlocks.Iron)

def reset():
	global min_x
	global max_x
	global min_y
	global max_y
	min_x = 0
	max_x = get_world_size()
	min_y = 0
	max_y = get_world_size()
	


	
list = [North,East,South,West]
opp= {North:South,East:West,South:North,West:East}
def iron_in_range():
	for i in list:
		if get_ground_type(i) == Grounds.Iron:
			return True
	if get_ground_type() == Grounds.Iron:
		return True
	else:
		return False

def unearth():
	for i in range(get_world_size()):
		while not get_ground_type() == Grounds.Rock:
			dig()
		move(North)

for i in range(10):
	goal = prospect_iron()
	print(goal)
	reset()
	count = 0
	while goal != None:
		if goal == East:
			min_x = get_pos_x()
			go_to_x((max_x + min_x) // 2)
			count += 1
		elif goal == West:
			max_x = get_pos_x()
			go_to_x((max_x + min_x) // 2)
			count += 1
		if goal == North:
			min_y = get_pos_y()
			go_to_y((max_y + min_y) // 2)
			count += 1
		elif goal == South:
			max_y = get_pos_y()
			count += 1
			go_to_y((max_y + min_y) // 2)
		if count > 20:
			reset()
		goal = prospect_iron()
		print(goal)
	if num_items(Items.Coal) < 1:
		break 
	while not get_ground_type() == Grounds.Iron:
		dig()
	 
	while iron_in_range():
		for i in list:	
			if get_ground_type(i) == Grounds.Iron:
				move(i)
				dig()
				move(opp[i])
		if get_ground_type() == Grounds.Iron:
			dig()