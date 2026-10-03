from Utilitys import *
clear()

def main():
	drones = []
	for i in range(get_world_size() - 1):
		move(East)
		drones.append(spawn_drone(swarm_plant))
	move(East)
	swarm_plant()
	go_to_cords(get_world_size() - 1,get_world_size() - 1)
	for i in drones:
		wait_for(i)
	tr = measure()
	go_to_cords(0,0)
	bl = measure()
		

def swarm_plant():
	for i in range(get_world_size()):
		move(North)
		if get_ground_type() != Grounds.soil:
			till()
		if can_harvest():
			harvest()
		plant(Entities.Pumpkin)
		water_tile()
	bad = check_Tiles()
	while len(bad) > 0:
		bad = Fix_holes(bad)
		
def check_Tiles():
	bad = []
	for i in range(get_world_size()):
		if not can_harvest():
			bad.append(get_pos_y())
		move(North)
	return bad
	
def Fix_holes(bad):
	new = []
	for i in bad:
		go_to_y(i)
		if can_harvest():
			pass
		else:
			plant(Entities.Pumpkin)
			new.append(i)
	return new
if __name__ == "__main__":
	main()
	go_to_cords(0,0)
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			use_item(Items.Weird_Substance)
			move(North)
		move(East)
	directions = [North,East,South,West]
	for dir in directions:
		for i in range(get_world_size() - 1):
			move(dir)
			if not ((get_pos_x() == 0 or get_pos_x() == get_world_size() - 1) and (get_pos_y() == 0 or get_pos_y() == get_world_size() - 1)):
				use_item(Items.Fertilizer)
	harvest()	
	