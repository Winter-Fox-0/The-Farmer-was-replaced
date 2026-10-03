from Utilitys import *
poly = Entities.Carrot
pass1 = [3,11,19,27]
pass2 = [7,15,23,31]

def poly_farm(c):
	go_to_cords(c)
	while not can_harvest() and get_entity_type() != None:
		if poly != Entities.Bush:
			use_item(Items.Fertilizer)
			use_item(Items.Weird_Substance)
			pass
		else:
			pass
	harvest()
	farm(poly)
	if get_companion() != None:
		comp,cords = get_companion()
		go_to_cords(cords)
		farm(comp)
def a_farm(c):
	while True:
		poly_farm(c)

def prep():
	while get_pos_y() < get_world_size() - 1:
		till()
		move(North)
	till()
		
clear()
	
for i in range(get_world_size()-1):
	spawn_drone(prep)
	move(East)
prep()
	



for x in pass1:
	for y in pass1:
		spawn_drone(a_farm,(x,y))

for x in pass2:
	for y in pass2:
		spawn_drone(a_farm,(x,y))
		
a_farm((31,31))
	
	