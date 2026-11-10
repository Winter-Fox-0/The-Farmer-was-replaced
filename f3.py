from Utilitys import * 
def main():
	set_world_size(8)
	Prep_advanced_soil(Grounds.Loam,False)
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
	count = 15
	for c in range(9):
		for i in list:
			if i[1] == count:
				go_to_cords(i[0])
				harvest()
		count -= 1
	
		
def pl():
	for i in range(get_world_size()):
		farm(Entities.Sunflower)
		move(North) 

main()