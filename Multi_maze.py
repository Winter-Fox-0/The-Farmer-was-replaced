from Utilitys import *
# ----------------------------------------
# A* Maze Solver for Reused Mazes
# ----------------------------------------
dirs = [North, East, South, West]
offsets = {
	North: (0, 1),
	East:  (1, 0),
	South: (0, -1),
	West:  (-1, 0)
}
# Map format:
# maze[(x,y)] = [north,east,south,west]
maze = {}
change_log = []

def pos():
	return (get_pos_x(), get_pos_y())

def neighbor(p, direction):
	x, y = p
	dx, dy = offsets[direction]
	return (x + dx, y + dy)

def scan_tile():
	x, y = pos()
	current_data = [
		can_move(North),
		can_move(East),
		can_move(South),
		can_move(West)
	]
	if (x, y) in maze:
		old = maze[(x, y)]
		if old != current_data:
			dir_names = ["North", "East", "South", "West"]
			entry = "(" + str(x) + "," + str(y) + "):"
			for i in range(4):
				if old[i] != current_data[i]:
					if current_data[i]:
						state = "opened" 
					else:
						state = "closed"
					entry = entry + " " + dir_names[i] + " " + state + ","
			change_log.append(entry)
	maze[(x, y)] = current_data

def move_to_neighbor(target):
	x, y = pos()
	tx, ty = target
	if tx == x and ty == y + 1:
		move(North)
	elif tx == x + 1 and ty == y:
		move(East)
	elif tx == x and ty == y - 1:
		move(South)
	elif tx == x - 1 and ty == y:
		move(West)

# ----------------------------------------
# Explore maze and build map
# ----------------------------------------
def dfs_map(previous=None):
	scan_tile()
	if get_entity_type() == Entities.Treasure:
		return
	current = pos()
	for i in range(4):
		if not maze[current][i]:
			continue
		nxt = neighbor(current, dirs[i])
		if nxt == previous:
			continue
		if nxt not in maze:
			move(dirs[i])
			dfs_map(current)
			move(dirs[(i + 2) % 4])

# ----------------------------------------
# A* Search
# ----------------------------------------
def heuristic(a, b):
	ax, ay = a
	bx, by = b
	dx = ax - bx
	if dx < 0:
		dx = -dx
	dy = ay - by
	if dy < 0:
		dy = -dy
	return dx + dy

def astar(start, goal):
	open_set = [start]
	came_from = {}
	g = {start: 0}
	f = {start: heuristic(start, goal)}
	while len(open_set) > 0:
		current = open_set[0]
		for node in open_set:
			if f[node] < f[current]:
				current = node
		if current == goal:
			path = [current]
			while current in came_from:
				current = came_from[current]
				path.insert(0, current)
			return path
		open_set.remove(current)
		exits = maze[current]
		for i in range(4):
			if not exits[i]:
				continue
			nxt = neighbor(current, dirs[i])
			tentative = g[current] + 1
			if nxt not in g or tentative < g[nxt]:
				came_from[nxt] = current
				g[nxt] = tentative
				f[nxt] = tentative + heuristic(nxt, goal)
				if nxt not in open_set:
					open_set.append(nxt)
	return None

# ----------------------------------------
# Follow a path
# ----------------------------------------
def follow_path(path):
	for i in range(1, len(path)):
		move_to_neighbor(path[i])
		scan_tile()

# ----------------------------------------
# Reuse loop
# ----------------------------------------
def farm_maze(repeats):
	dfs_map()
	for i in range(repeats):
		target = measure()
		if target == None:
			break
		route = astar(pos(), target)
		if route != None:
			follow_path(route)
		use_item(
			Items.Weird_Substance,
			8 * 2**(num_unlocked(Unlocks.Mazes)-1)
		)
		tap()
	harvest()
points = [(28,28),(28,20),(28,12),(28,3),
(20,28),(20,20),(20,12),(19,3),
(12,28),(12,20),(12,12),(11,3),
(3,28),(3,20),(3,12),(3,3)]

def main(c):
	while True:
		go_to_cords(c)
		do_a_flip()
		plant(Entities.Bush)
		use_item(Items.Weird_Substance,8 * 2**(num_unlocked(Unlocks.Mazes)-1))
		farm_maze(300)
	
clear()
for x in points:
	spawn_drone(main,x)
		

