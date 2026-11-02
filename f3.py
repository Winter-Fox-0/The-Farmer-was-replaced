from Utilitys import * 
def main():
	go_to_cords(0,0)
	for i in range(get_world_size()):
		move(East)
		if num_drones() < max_drones():
			spawn_drone(pl)
		else:
			pl()
	while num_drones() > 1:
		pass
	list = []
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			
			if get_entity_type() == Entities.Sunflower:
				list.append(((get_pos_x(),get_pos_y()),measure()))
			move(North)
		move(East)
	
		
def pl():
	for i in range(get_world_size()):
		if get_ground_type() == Grounds.Loam:
			plant(Entities.Sunflower)
			water_tile()
		move(North) 

main()