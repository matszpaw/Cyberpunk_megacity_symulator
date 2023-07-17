import random
import numpy as np
import lists_of_stuff as los
#simple world generator

class land_feature:
    def __init__(self,tile_name:str,encounters_good:list,encounters_bad:list):
        self.tile_name = tile_name
        self.encounters_good = encounters_good
        self.encounters_bad = encounters_bad

    def make_tile(self,tile_name:str):

        if tile_name == 'meadows':
            self.encounters_bad.append(los.list_of_events)
            self.encounters_good.append(los.list_of_events)
        if tile_name == 'forest':
            self.encounters_bad.append(los.list_of_events)
            self.encounters_good.append(los.list_of_events)
        if tile_name == 'marsh':
            self.encounters_bad.append(los.list_of_events)
            self.encounters_good.append(los.list_of_events)
        if tile_name == 'lake':
            self.encounters_bad.append('fish')
            self.encounters_good.append('fish')

def world_object_grid(shape_of_world:list):
    world = []
    def row(z):
        row = []
        for i in range(z):
            row.append(land_feature(los.kinds_of_tiles[random.randint(0,3)],[],[]))
            row[i].make_tile(row[i].tile_name)
        return row
    for x in range(shape_of_world[1]):
        world.append(row(shape_of_world[0]))
    return world


print(world_object_grid([2,2]))
#next ---> animate this stuff and fill with real encounters