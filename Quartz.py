from Utilitys import *
clear()
jump(Unlocks.Quartz)
depth = get_pos_z()
while num_items(Items.Iron) >= 4:
	dA = prospect_quartz()
	move(East)
	dB = prospect_quartz()
	move(West)
	move(North)
	dC = prospect_quartz()
	move(South)
	place(Grounds.Blue_Block)
	dD = prospect_quartz()
	dig()
	
	dx = (round((dA*dA - dB*dB + 1) / 2)) % get_world_size()
	dy = (round((dA*dA - dC*dC + 1) / 2)) % get_world_size()
	dz = round((dA*dA - dD*dD + 1) / 2)
	
	go_to_cords(dx,dy)
	
	
	
	for i in range(abs(dz)+1):
		dig()
	while get_ground_type() == Grounds.Quartz:
		dig()
	while depth > get_pos_z():
		place(Grounds.Red_Block)

	
	
