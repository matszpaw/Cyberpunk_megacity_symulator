import random
import numpy as np
#simple world generator


#this stuff will be in separate file
kinds_of_tiles = ['lake','forest','meadows','marsh']
list_of_events = ['goblins','tresure','inn','wandering merchant']

class land_feature:
    #when used transform string into object
    def __init__(self,tile_name:str,encounters_good:list,encounters_bad:list):
        self.tile_name = tile_name
        self.encounters_good = encounters_good
        self.encounters_bad = encounters_bad

    def make_tile(self,tile_name:str):
        if tile_name == 'meadows':
            self.encounters_bad.append(list_of_events)
            self.encounters_good.append(list_of_events)
        if tile_name == 'forest':
            self.encounters_bad.append(list_of_events)
            self.encounters_good.append(list_of_events)
        if tile_name == 'marsh':
            self.encounters_bad.append(list_of_events)
            self.encounters_good.append(list_of_events)
        if tile_name == 'lake':
            self.encounters_bad.append('fish')
            self.encounters_good.append('fish')

def ready_world_object(shape_of_world:list):
    world = []
    def row(z):
        row = []
        for i in range(z):
            row.append(land_feature(kinds_of_tiles[random.randint(0,3)],[],[]))
            row[i].make_tile(row[i].tile_name)
        return row
    for x in range(shape_of_world[1]):
        world.append(row(shape_of_world[0]))
    return np.array(world)

def generator(shape_of_world:list):
    world = []
    kinds_of_tiles = ['lake','forest','meadows','marsh']
    for i in range(shape_of_world[0]):
        x = [kinds_of_tiles[random.randint(0,3)] for i in range(shape_of_world[1])]
        world.append(x)
    return np.array(world)