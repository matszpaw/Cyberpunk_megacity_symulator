kinds_of_tiles = ['lake','forest','meadows','marsh']
list_of_events = ['goblins','tresure','inn','wandering merchant']

def generator(shape_of_world:list):
    world = []
    for i in range(shape_of_world[0]):
        x = [kinds_of_tiles[random.randint(0,3)] for i in range(shape_of_world[1])]
        world.append(x)
    return np.array(world)

#def goblin_encouter(danger_lvl):
#def tresure(size):
