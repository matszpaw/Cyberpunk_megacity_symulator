import time
import random
import numpy as np

#real time simulation on second discrite stuff happens
#the function is checking trhu the list on every turn

#global variables ---> use them to manipulate simulation
population = 0

list_of_forest_events = {

}
list_of_lake_events = {

}
list_of_marsh_events = {

}
list_of_meadows_events = {

}

def generator(shape_of_world:list):
    world = []
    kinds_of_tiles = ['forest','lake','meadows','marsh']
    for i in range(shape_of_world[0]):
        x = [kinds_of_tiles[random.randint(0,3)] for i in range(shape_of_world[1])]
        world.append(x)
    return np.array(world)

def event_generator(world):
    for tile in world:
        match tile:
            case 'forest':
                #add resources * peoples
                print()
            case 'lake':
                print()
            case 'meadows':
                print()
            case 'marsh':
                print()
        
def space_and_time(n):
    a = 0
    world = generator(2,2)
    #prints number of diffrent tiles
    #print map of the world in matplotlib
    for x in range(n):
        a = a + 1
        print('turn ',a,' beginns!!!')
        #function checks every tile and does one of 
        time.sleep(1)





ticker(5)