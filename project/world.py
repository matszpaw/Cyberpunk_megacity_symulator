import random
import numpy as np
#simple world generator

def generator(shape_of_world:list):
    world = []
    kinds_of_tiles = ['lake','forest','meadows','marsh']
    for i in range(shape_of_world[0]):
        x = [kinds_of_tiles[random.randint(0,3)] for i in range(shape_of_world[1])]
        world.append(x)
    return np.array(world)

test = generator([2,2])
print(test)





