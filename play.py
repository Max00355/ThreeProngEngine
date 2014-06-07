import json
import pickle
import sys
import pygame
from pygame.locals import *
import utils
import player as player_
import util_functions

def load_collision_map(level):

    with open(level, 'rb') as file:
        data = json.loads(pickle.loads(file.read()))
    
    utils.player = pygame.Rect(data['player'][0], data['player'][1], utils.size, utils.size) # Setup player

    utils.collision_map = []
    utils.enemies = []
    utils.objects = []
    utils.endpoints = []

    for m in data['map']: # Set up collision map
        utils.collision_map.append(pygame.Rect(m[0], m[1], utils.size, utils.size))

    for x in data['enemies']: # Setup enemies
        utils.enemies.append(pygame.Rect(x[0], x[1], utils.size, utils.size))

    for x in data['objects']: # setup objects
        utils.objects.append(pygame.Rect(x[0], x[1], utils.size, utils.size))
   
    for x in data['endpoints']:
        utils.endpoints.append(pygame.Rect(x[0], x[1], utils.size, utils.size))


def run():

    screen = utils.screen
    pygame.display.set_caption(utils.title)


    ### Defining Objects ###

    Player = player_.Player()

    ########################

    ### Point objects toward module json file ###

    modules = {


        Player:"modules/player.json"

    }



    ##############################################


    # Load modules
    for x in modules:
        modules[x] = json.loads(open(modules[x]).read())
    
    utils.map_ = util_functions.load_map_module()
    utils.map_on = utils.map_['first'] # Thee is a field in the module called "first" that defines the first "level" or screen.
    load_collision_map(utils.map_on) # This will load a level, in the future this will check if there is a saved file somewhere and load the map from there
    clock = pygame.time.Clock()

    while True:
        clock.tick(35)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
       
        screen.fill((255,255,255))
        
        if utils.map_[utils.map_on]['background'] == "Rect":
            for x in utils.collision_map:
                pygame.draw.rect(screen, (0,0,0), x)
        else:
            # Draw map file
            screen.blit(util_functions.loader(utils.map_[utils.map_on]['background']), (0 - utils.camerax, 0 - utils.cameray))


        ##################### Custom modules here ###################


        if modules[Player]['standing'] == "Rect":
            pygame.draw.rect(screen, (0, 255,255), utils.player)
        else:
            # Load images instead of block
            pass


        # Update sprites, add your sprite's update function here

        Player.update()

        pygame.display.update()

if __name__ == "__main__":
    run()


