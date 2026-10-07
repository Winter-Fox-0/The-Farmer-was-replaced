WORLD_SIZE = get_world_size() # breaks if world is changed after imported
WORLD_AREA = WORLD_SIZE * WORLD_SIZE
WORLD_CENTER = (WORLD_SIZE // 2, WORLD_SIZE // 2)
WORLD_MAX_COORD = WORLD_SIZE - 1


WATER_TARGET = 0.75

# all plantable Entities:
PLANTABLE = [Entities.Bamboo,Entities.Bush,Entities.Cactus,
Entities.Carrot,Entities.Grass,Entities.Pumpkin,
Entities.Rice,Entities.Sunflower,Entities.Tree]

# grounds Entities can grow on
CAN_GROW = {Entities.Bamboo:[Grounds.Dirt,Grounds.Perlite,Grounds.Soil],
Entities.Bush:[Grounds.Grassland,Grounds.Perlite,Grounds.Soil],
Entities.Cactus:[Grounds.Perlite,Grounds.Soil],
Entities.Carrot:[Grounds.Loam,Grounds.Soil],
Entities.Grass:[Grounds.Grassland,Grounds.Soil],
Entities.Pumpkin:[Grounds.Soil],
Entities.Rice:[Grounds.Clay],
Entities.Sunflower:[Grounds.Loam,Grounds.Soil],
Entities.Tree:[Grounds.Grassland,Grounds.Perlite,Grounds.Soil]}
# grounds that can be tilled
TILLABLE = [Grounds.Grassland,Grounds.Dirt,Grounds.Soil]