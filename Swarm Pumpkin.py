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
	if bl == tr:
		harvest()
		

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
	while True:
		main()
	