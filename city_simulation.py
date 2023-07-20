import time
import random
import numpy as np

#cyberpunk city
#city symulation where disctricts optimalize their placment

#plans
#energy ---> generates overall energy consumes people to work
#housing ---> consumes energy produces people
#lesure ---> consumes enery and production
#production ---> consumes energy and people makes stuff

#global symulation variables
population = 0
energy = 1
production = 0
happines = 0

def generator(shape_of_world:list):
    world = []
    kinds_of_tiles = ['energy','housing','production','lesure']
    for i in range(shape_of_world[0]):
        x = [kinds_of_tiles[random.randint(0,3)] for i in range(shape_of_world[1])]
        world.append(x)
    return np.array(world)

def event_generator(world):
    shape = np.shape(world)
    global population,energy,production,happines
    for row in range(shape[0]):
        for column in range(shape[1]):
            match world[row,column]:
                case 'lesure':
                    if energy > 0 and population > 0:
                        energy = energy-1
                        happines = happines+1
                        print('more happy!!!')
                    else:
                        print('not enough energy')
                case 'housing':
                    if energy > 0:
                        population = population+1
                        energy = energy-1
                        print('more people!!!')
                    else:
                        print('not enough energy')
                case 'production':
                    if energy > 0 and population > 0:
                        energy = energy-1
                        production = production+1
                        print('more stuff!!!')
                    else:
                        print('not enough energy')
                case 'energy':
                    if population > 0:
                        energy = energy+1
                        population = population-1
                        print('more energy!!!')
        
def space_and_time(turns,shape):
    a = 0
    world = generator(shape)
    for x in range(turns):
        a = a + 1
        print('')
        print('turn ',a,' beginns!!!')
        event_generator(world)
        print('')
        print('population: ',population)
        print('energy: ',energy)
        print('production: ',production)
        print('happines: ',happines)
        time.sleep(1)

space_and_time(3,[3,3])