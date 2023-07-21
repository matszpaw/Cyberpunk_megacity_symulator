import time
import random
import numpy as np
import os
import variables

kinds_of_tiles = ['energy', 'housing', 'production', 'lesure']



def event_generator(world):
    global variables.population, variables.energy, variables.production, variables.happines
    shape = np.shape(world)
    for row in range(shape[0]):
        for column in range(shape[1]):
            match world[row, column]:
                case 'lesure':
                    if variables.energy > 0 and variables.population > 0:
                        variables.energy = variables.energy-1
                        variables.production = variables.production-1
                        variables.population = variables.population-1
                        variables.happines = variables.happines+1
                        print('more happy!!!')
                    else:
                        print('not enough energy, production or population')
                        world[row, column] = kinds_of_tiles[random.randint(0,2)]
                case 'housing':
                    if variables.energy > 0:
                        variables.population = variables.population+1
                        variables.energy = variables.energy-1
                        print('more people!!!')
                    else:
                        print('not enough energy')
                        world[row, column] = 'energy'
                case 'production':
                    if variables.energy > 0 and variables.population > 0:
                        variables.energy = variables.energy-1
                        variables.production = variables.production+10
                        print('more stuff!!!')
                    else:
                        print('not enough energy')
                        world[row, column] = kinds_of_tiles[random.randint(0,1)]
                case 'energy':
                    if variables.population > 0:
                        variables.energy = variables.energy+1
                        variables.population = variables.population-1
                        print('more energy!!!')
                    else:
                        print('not enough people')
                        world[row, column] = 'housing'

#alternative event sistem system(when they fire )

def energy_turn(world):
    global variables.population, variables.energy, variables.production, variables.happines
    shape = np.shape(world)
    for row in range(shape[0]):
        for column in range(shape[1]):
            if world[row, column] == 'energy':
                if variables.population > 0:
                    variables.energy = variables.energy+1
                    variables.population = variables.population-1
                    print('more energy!!!')
                else:
                    print('not enough people')
                    world[row, column] = 'housing'
            else:
                pass
def housing_turn(world):
    global variables.population, variables.energy, variables.production, variables.happines
    shape = np.shape(world)
    for row in range(shape[0]):
        for column in range(shape[1]):
            if world[row, column] == 'energy':
                if variables.energy > 0 and variables.population > 0:
                    variables.energy = variables.energy-1
                    variables.production = variables.production+10
                    print('more stuff!!!')
                else:
                    print('not enough energy')
                    world[row, column] = kinds_of_tiles[random.randint(0,1)]
            else:
                pass

def production_turn(world):
    global variables.population, variables.energy, variables.production, variables.happines
    shape = np.shape(world)
    for row in range(shape[0]):
        for column in range(shape[1]):
            if world[row, column] == 'production':
                if variables.energy > 0 and variables.population > 0:
                    variables.energy = variables.energy-1
                    variables.production = variables.production+10
                    print('more stuff!!!')
                else:
                    print('not enough energy')
                    world[row, column] = kinds_of_tiles[random.randint(0,1)]
            else:
                pass

def lesure_turn(world):
    global variables.population, variables.energy, variables.production, variables.happines
    shape = np.shape(world)
    for row in range(shape[0]):
        for column in range(shape[1]):
            if world[row, column] == 'lesure':
                if variables.energy > 0 and variables.population > 0:
                    variables.energy = variables.energy-1
                    variables.production = variables.production-1
                    variables.population = variables.population-1
                    variables.happines = variables.happines+1
                    print('more happy!!!')
                else:
                    print('not enough energy, production or population')
                    world[row, column] = kinds_of_tiles[random.randint(0,2)]
            else:
                pass