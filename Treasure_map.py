from Utilitys import *
clear()
while True:
	while not Grounds.Basalt == get_ground_type():
		dig()
	
	def flatten():
			for j in range(get_world_size()):
				while get_pos_z() > depth:
					dig()
				move(North)
	#drones = []
	depth = get_pos_z()
	#for i in range(get_world_size()):
		#if num_drones() < max_drones():
			#drones.append(spawn_drone(flatten))
		#else:
			#flatten()
		#move(East)
	#for i in drones:
		#wait_for(i)
		
	go_to_cords(measure())
	
	while get_pos_z() + 1 > depth:
		dig()
	
	list = measure()
	
	dir_dict = {"S":South,"N":North,"W":West,"E":East}
	
	for i in list:
		if i == "D":
			dig()
		else:
			move(dir_dict[i])
		harvest()