## rename to Utilitys
from Constents import *

# ----- Movement/nav -----

def at_world_edge(edge_to_check = None):
	world = get_world_size() - 1
	if edge_to_check == North:
		return get_pos_y() == world
	elif edge_to_check == East:
		return get_pos_x() == world
	elif edge_to_check == South:
		return get_pos_y() == 0
	elif edge_to_check == West:
		return get_pos_x() == 0

def go_to_x(tx,can_wrap = True, step = False):
	x = get_pos_x()

	if get_pos_x() == tx:
		return

	if can_wrap:
		world = get_world_size()
		x1 = ((x - tx) % world) # left
		x2 = ((tx - x) % world) # right
		if x1 >= x2:
			d = East
		else:
			d = West
	else:
		if x < tx:
			d = East
		else:
			d = West
			
	if step:
		move(d)
	else:
		while get_pos_x() != tx:
			move(d)
	
def go_to_y(ty,can_wrap = True, step = False):
	y = get_pos_y()

	if get_pos_y() == ty:
		return

	if can_wrap:
		world = get_world_size()
		y1 = ((y - ty) % world) # down
		y2 = ((ty - y) % world) # up
		if y1 >= y2:
			d = North
		else:
			d = South
	else:
		if y < ty:
			d = North
		else:
			d = South
			
	if step:
		move(d)
	else:
		while get_pos_y() != ty:
			move(d)

def go_to_z(z,filler = Grounds.Dirt):
	target = z
	while target > get_pos_z():
		place(filler)
	while target < get_pos_z():
		dig()

def go_to_cords(x_or_tuple,y = None,z = None):
	includes_z = False
	
	if y == None:
		if len(x_or_tuple) > 2:
			includes_z = True
			target_x,target_y,target_z = x_or_tuple
		else:
			target_x,target_y = x_or_tuple
	else:
		if z == None:
			target_x = x_or_tuple
			target_y = y
		else:
			includes_z = True
			target_x = x_or_tuple
			target_y = y
			target_z = z
			
	while get_pos_x() != target_x or get_pos_y() != target_y:
		if get_pos_x() != target_x:
			go_to_x(target_x,True,True)
		if get_pos_y() != target_y:
			go_to_y(target_y,True,True)
	if includes_z:
		go_to_z(target_z)

def get_pos(z = False):
	if z:
		return (get_pos_x(),get_pos_y(),get_pos_z())
	else:
		return (get_pos_x(),get_pos_y())

def opposite(dir):
	opposite = {North:South,South:North,East:West,West:East}
	return opposite[dir]

def move_steps(dir, step_count):
	for i in range(step_count):
		move(dir)

def move_to_neighbor(target):
	x, y = pos()
	tx, ty = target
	if tx == x and ty == y + 1:
		move(North)
	elif tx == x + 1 and ty == y:
		move(East)
	elif tx == x and ty == y - 1:
		move(South)
	elif tx == x - 1 and ty == y:
		move(West)

def get_distance(c,t,can_wrap = False):
	if c == t:
		return 0
	
	if can_wrap:
		world = get_world_size()
		d1 = ((c - t) % world) # down
		d2 = ((t - c) % world) # up
		return min(d1,d2)
	else:
		return abs(c - t)
		
def get_manhattan(target,can_wrap = False):
	x,y = get_pos()
	tx,ty = target
	return get_distance(x,tx,can_wrap) + get_distance(y,ty,can_wrap)

# ----- farming -----

def harvest_on_ready():
	while not can_harvest():
		pass
	harvest()

def ensure_ground(p):

	if p not in PLANTABLE:
		return

	if get_ground_type() in CAN_GROW[p]:
		return
	
	if p == Entities.Rice:
		while get_ground_type() != Grounds.Clay:
			dig()
	else:
		if get_ground_type() not in TILLABLE:
			dig()
			place(Grounds.Grassland)
		if get_ground_type() not in CAN_GROW[p]:
			till()

def auto_plant(p):
	ensure_ground(p)
	plant(p)

def water_tile():
	w = ceil((WATER_TARGET - get_water()) / 0.25)
	if get_water() < WATER_TARGET and num_items(Items.Water) >= w:
		use_item(Items.Water,w)

def farm(tbp):
	if get_entity_type():
		harvest_on_ready()
	
	auto_plant(tbp)
	water_tile()

# ----- Mining -----

def flatten_to_level(l,filler = Grounds.Dirt):
	while get_pos_z() != l:
		if get_pos_z() > l:
			dig()

def flatten_to_block():
	pass

def will_collapse(dir):
	pass

def get_mean_height():
	pass

# ----- Scanner -----

def check_surrounding_for(block):
	pass

def map_row_cords(request_info):
	pass

def map_column_cords(request_info):
	pass

def map_world_cords(request_info):
	pass

def map_row_state(request_info):
	pass

def map_column_state(request_info):
	pass

def map_world_state(request_info):
	pass

def format_data_map(map):
	pass

def on_same_height(hight_map,dir):
	pass
	
# ----- Drone Management -----

def summon_swarm(func,args):
	pass

def arg_parser():
	pass

def wait_all():
	pass

def wait_all_advance(list_of_drones):
	pass

def act_tile():
	pass

def act_row(f,invert = False):
	pass

def act_column(f,invert = False):
	pass


def act_world(func):
	pass

def check_for_command():
	pass

def check_break():
	pass

#----- missing py functions -----

def round(value):
	if value >= 0:
		return (value + 0.5) // 1
	else:
		return (value - 0.5) // 1

def floor(value):
	if value >= 0:
		return value // 1
	else:
		return ((value * -1) // 1) * -1
		

def ceil(value):
	if value <= 0:
		return value // 1
	else:
		return ((value * -1) // 1) * -1

def copy_list():
	pass

def clamp():
	pass
