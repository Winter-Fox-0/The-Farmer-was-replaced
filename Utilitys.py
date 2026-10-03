## rename to Utilitys
from Constents import *

# ----- Movement/nav -----

def at_world_edge(edge_to_check = None):
	if edge_to_check == North:
		return get_pos_y() == WORLD_MAX_COORD
	elif edge_to_check == East:
		return get_pos_x() == WORLD_MAX_COORD
	elif edge_to_check == South:
		return get_pos_y() == 0
	elif edge_to_check == West:
		return get_pos_x() == 0

def go_to_x(x,auto = True):
	world = get_world_size()
	target = x
	current_x = get_pos_x()
	Direction = None
	option_1 = ((current_x - target) % world)
	option_2 = ((target - current_x) % world)

	if option_1 >= option_2:
		Direction = East
	else:
		Direction = West

	if auto:
		while get_pos_x() != target:
			move(Direction)
	else:
		if get_pos_x() != target:
			move(Direction)

def go_to_y(y, auto = True):
	world = get_world_size()
	target = y
	current_y = get_pos_y()
	Direction = None
	option_1 = ((current_y - target) % world)
	option_2 = ((target - current_y) % world)

	if option_1 >= option_2:
		Direction = North
	else:
		Direction = South
	if auto:
		while get_pos_y() != target:
			move(Direction)
	else:
		if get_pos_y() != target:
			move(Direction)

def go_to_z(z,filler = Grounds.Dirt):
	target = z
	while target > get_pos_z():
		place(filler)
	while target < get_pos_z():
		dig()

def go_to_cords(x_or_tuple,y = None ,z = None):
	if y == None:
		target_x,target_y = x_or_tuple
	else:
		target_x = x_or_tuple
		target_y = y
	while get_pos_x() != target_x or get_pos_y() != target_y:
		if get_pos_x() != target_x:
			go_to_x(target_x,False)
		if get_pos_y() != target_y:
			go_to_y(target_y,False)

def get_pos(z = False):
	pass

def opposite(dir):
	pass

def move_steps():
	pass

def move_to_neighbor():
	pass

def get_manattan(target,can_wrap = False):
	pass

def warp_cord(x_or_tuple,y = None):
	pass

# ----- farming -----

def harvest_on_ready():
	while not can_harvest():
		pass
	harvest()

def replant():
	pass

def water_tile():
	while num_items(Items.Water) > 1 and get_water() < WATER_TARGET:
		use_item(Items.Water)

def ensure_ground():
	pass

# rename farm
def farm(tbp):
	terrain = {
	Entities.Bush:Grounds.Grassland,
	Entities.Cactus:Grounds.Soil,
	Entities.Carrot:Grounds.Soil,
	Entities.Grass:Grounds.Grassland,
	Entities.Pumpkin:Grounds.Soil,
	Entities.Sunflower:Grounds.Soil,
	Entities.Tree:Grounds.Grassland
	}
	if can_harvest():
		harvest()
	if get_ground_type() != terrain[tbp]:
		till()
	plant(tbp)
	water_tile()

# ----- Mining -----

def flatten_to_level():
	pass

def flatten_to_block():
	pass

def will_collapse(dir):
	pass

def get_mean_height():
	pass

# ----- Scanner -----

def ground_in_list(list):
	pass

def entity_in_list(list):
	pass

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

def act_row():
	pass

def act_column():
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

def copy_list():
	pass

def clamp():
	pass
