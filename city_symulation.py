import time
import random
import numpy as np
import os
import variables
import event_functions

# energy ---> generates overall energy consumes people to work
# housing ---> consumes energy produces people
# lesure ---> consumes enery and production
# production ---> consumes energy and people makes stuff

def generator(shape_of_world: list):
    kinds_of_tiles = ['energy', 'housing', 'production', 'lesure']
    world = []
    for i in range(shape_of_world[0]):
        x = [kinds_of_tiles[random.randint(0, 3)]
             for i in range(shape_of_world[1])]
        world.append(x)
    return np.array(world)

def space_and_time(turns, shape):
    world = generator(shape)
    for x in range(turns):

        print('')
        print('turn ',x+1, ' beginns!!!')

        event_functions.event_generator(world)

        print('')
        print('population: ',variables.population)
        print('production: ',variables.production)
        print('energy: ',variables.energy)
        print('happines: ',variables.happines)
        print('')

        time.sleep(2)
        os.system('clear')

    print('')
    print(world)
    print('')

space_and_time(20, [3, 3])

#implement selector with elements goes first
#implement absolute counter function
#implement proximity bonus function