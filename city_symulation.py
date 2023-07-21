import time
import random
import numpy as np
import os

# cyberpunk city
# city symulation where disctricts optimalize their placment

# energy ---> generates overall energy consumes people to work
# housing ---> consumes energy produces people
# lesure ---> consumes enery and production
# production ---> consumes energy and people makes stuff

# global symulation variables
population = 0
energy = 0
production = 0
happines = 0
#global population, energy, production, happines
kinds_of_tiles = ['energy', 'housing', 'production', 'lesure']

def generator(shape_of_world: list):
    world = []
    for i in range(shape_of_world[0]):
        x = [kinds_of_tiles[random.randint(0, 3)]
             for i in range(shape_of_world[1])]
        world.append(x)
    return np.array(world)


def event_generator(world):
    global population, energy, production, happines
    shape = np.shape(world)
    for row in range(shape[0]):
        for column in range(shape[1]):
            match world[row, column]:
                case 'lesure':
                    if energy > 0 and population > 0:
                        energy = energy-1
                        production = production-1
                        population = population-1
                        happines = happines+1
                        print('more happy!!!')
                    else:
                        print('not enough energy, production or population')
                        world[row, column] = kinds_of_tiles[random.randint(0,2)]
                case 'housing':
                    if energy > 0:
                        population = population+1
                        energy = energy-1
                        print('more people!!!')
                    else:
                        print('not enough energy')
                        world[row, column] = 'energy'
                case 'production':
                    if energy > 0 and population > 0:
                        energy = energy-1
                        production = production+10
                        print('more stuff!!!')
                    else:
                        print('not enough energy')
                        world[row, column] = kinds_of_tiles[random.randint(0,1)]
                case 'energy':
                    if population > 0:
                        energy = energy+10
                        population = population-1
                        print('more energy!!!')
                    else:
                        print('not enough people')
                        world[row, column] = 'housing'

def space_and_time(turns, shape):
    world = generator(shape)
    for x in range(turns):

        print('')
        print('turn ',x+1, ' beginns!!!')

        event_generator(world)

        print('')
        print('population: ',population)
        print('production: ',production)
        print('energy: ',energy)
        print('happines: ',happines)
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