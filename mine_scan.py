from Utilitys import *
world = get_world_size()
go_to_cords(0,world -1)
board = []
for i in range(world):
	temp = []
	for i in range(world):
		move(East)
		info = measure()
		if info != None:
			temp.append(info)
		else:
			temp.append("?")
	board.append(temp)
	move(South)
for i in board:
	temp = ""
	for l in i:
		temp += str(l) 
	quick_print(temp)