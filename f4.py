from Utilitys import *
go_to_cords(0,0)

def main():
	drones = []
	for i in range(get_world_size() - 1):
		move(East)
		if num_drones() < max_drones(): 
			drones.append(spawn_drone(swarm_plant))
		else:
			swarm_plant()
	move(East)
	swarm_plant()
	go_to_cords(get_world_size() - 1,get_world_size() - 1)
	for i in drones:
		wait_for(i)
	move(East)
	drones2 = []
	for i in range(get_world_size()):
		move(North)
		drones2.append(spawn_drone(sort,East))
	sort(East)
	go_to_cords(0,0)
	for i in drones2:
		wait_for(i)
	harvest()
		

def swarm_plant():
	for i in range(get_world_size()):
		move(North)
		if get_ground_type() != Grounds.Soil and get_ground_type() != Grounds.Perlite:
			till()
		if can_harvest():
			harvest()
		plant(Entities.Cactus)
		water_tile()
	sort(North)
		
def sort(dir):
		opposite = {North:South,East:West,South:North,West:East}
		opp_dir = opposite[dir]
		if dir == North or dir == South:
			while not get_pos_y() == get_world_size() - 1:
				move(dir)
				while measure(opp_dir) > measure() and not get_pos_y() == 0:
					swap(opp_dir)
					move(opp_dir)
			move(dir)
		else:
			while not get_pos_x() == get_world_size() - 1:
				move(dir)
				while measure(opp_dir) > measure() and not get_pos_x() == 0:
					swap(opp_dir)
					move(opp_dir)
			move(dir)
			
			
if __name__ == "__main__":
	while True:
		main()
	