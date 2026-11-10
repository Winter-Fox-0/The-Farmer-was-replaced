from Utilitys import *

world = get_world_size()
clear()
go_to_cords(world // 2, world // 2)

def rice_prep():
	go_to_cords(0,0)
	summon_swarm(dig_to_block,[Grounds.Clay])

def rice_plant():
	go_to_cords(0,0)
	summon_swarm(farm,[Entities.Rice])

def harvest_rice():
	summon_swarm(harvest_on_ready)
	
while True:
	while get_ground_type() != Grounds.clay and get_ground_type() != Grounds.Dry_Rice_Terrace:
		dig()
	rice_prep()
	rice_plant()
	harvest_rice()
	go_to_cords(world // 2, world // 2)