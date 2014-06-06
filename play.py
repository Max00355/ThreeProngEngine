import sys
import pygame
from pygame.locals import *
import utils
import player as player_
import json
import pickle

def load_collision_map(level):

    with open(level, 'rb') as file:
        data = json.loads(pickle.loads(file.read()))
    
    utils.player = pygame.Rect(data['player'][0], data['player'][1], utils.size, utils.size) # Setup player

    for x in data['map']: # Set up collision map
        utils.collision_map.append(pygame.Rect(x[0], x[1], utils.size, utils.size))

    for x in data['enemies']: # Setup enemies
        utils.enemies.append(pygame.Rect(x[0], x[1], utils.size, utils.size))

    for x in data['objects']: # setup objects
        utils.objects.append(pygame.Rect(x[0], x[1], utils.size, utils.size))
    
    return json.loads(open("modules/maps.json").read())

def run():

    screen = utils.screen
    Player = player_.Player()



    modules = {


        Player:"modules/player.json"

    }


    # Load modules
    for x in modules:
        modules[x] = json.loads(open(modules[x]).read())

    map_ = load_collision_map(utils.first_level) # This will load a level, in the future this will check if there is a saved file somewhere and load the map from there
    map_on = utils.first_level
    clock = pygame.time.Clock()

    while True:
        clock.tick(35)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
       
        screen.fill((255,255,255))

        if map_[map_on]['background'] == "Rect":
            for x in utils.collision_map:
                pygame.draw.rect(screen, (0,0,0), x)
        else:
            # Draw map file
            screen.blit(utils.loader(map_[map_on]['background']), (0 - utils.camerax, 0 - utils.cameray))

        if modules[Player]['standing'] == "Rect":
            pygame.draw.rect(screen, (0, 255,255), utils.player)
        else:
            # Load images instead of block
            pass


        # Update sprites

        Player.update()

        pygame.display.update()

if __name__ == "__main__":
    run()


