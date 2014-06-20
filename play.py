import json
import pickle
import sys
import pygame
from pygame.locals import *
import utils
import player as player_
import enemy as enemy_
import object as object_
import util_functions

def load_collision_map(level):

    with open(level, 'rb') as file:
        data = json.loads(pickle.loads(file.read()))
    if data['player']: 
        utils.player = {"object":pygame.Rect(data['player'][0], data['player'][1], utils.size, utils.size), "state":"standing"} # Setup player

    utils.collision_map = []
    utils.enemies = []
    utils.objects = []
    utils.endpoints = []

    for m in data['map']: # Set up collision map
        utils.collision_map.append(pygame.Rect(m[0], m[1], utils.size, utils.size))


########################## LOAD CUSTOM MODULES ###############################################

    for x in data['enemies']: # Setup enemies
        utils.enemies.append({"object":pygame.Rect(x[0], x[1], utils.size, utils.size), "state":"standing"})

    for x in data['objects']: # setup objects
        utils.objects.append({"object":pygame.Rect(x[0], x[1], utils.size, utils.size), "state":"standing"})
   
    for x in data['endpoints']:
        utils.endpoints.append(pygame.Rect(x[0], x[1], utils.size, utils.size))

##############################################################################################


def run():

    screen = utils.screen
    pygame.display.set_caption(utils.title)


    ### Defining Objects ###

    Player = player_.Player()
    Enemy = enemy_.Enemy()
    Object = object_.Object()

    ########################

    ### Point objects toward module json file ###

    modules = {


        Player:"modules/player.json",
        Enemy:"modules/enemy.json",
        Object:"modules/object.json",
    }

 
    ##############################################


    # Load modules
    for x in modules:
        modules[x] = json.loads(open(modules[x]).read())
    for module in modules: # Preloads all images
        for m in modules[module]:
            if modules[module][m] != "Rect":
                for num, n in enumerate(modules[module][m]):
                    modules[module][m][num] = {"image":pygame.image.load(n['image']).convert_alpha(), "times":n['times']}

    utils.map_ = util_functions.load_map_module()
    utils.map_on = utils.map_['first'] # Thee is a field in the module called "first" that defines the first "level" or screen.
    load_collision_map(utils.map_on) # This will load a level, in the future this will check if there is a saved file somewhere and load the map from there
    clock = pygame.time.Clock()

    if utils.camera_on: # This will center the camera on the player
        utils.camerax = (utils.player['object'].x / (utils.resolution[0] / 2)) - utils.resolution[0] / 3
        utils.cameray = (utils.player['object'].y / (utils.resolution[1] / 2)) - utils.resolution[1] / 6

    while True:
        clock.tick(35)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
       
        screen.fill(utils.background_fill)
        
        if utils.map_[utils.map_on]['background'] == "Rect":
            for x in utils.collision_map:
                pygame.draw.rect(screen, (0,0,0), x)
        else:
            # Draw map file
            screen.blit(util_functions.loader(utils.map_[utils.map_on]['background']), (0 - utils.camerax, 0 - utils.cameray))


        if utils.player['object']: 
            if modules[Player][utils.player['state']] == "Rect":
                pygame.draw.rect(screen, (0, 255,255), pygame.Rect(utils.player['object'].x - utils.camerax, utils.player['object'].y - utils.cameray, utils.size, utils.size))
            else:
                module = modules[Player]
                # Load images instead of block
                blitState(utils.player, module)


############# DRAW CUSTOM MODULES ########################

# These are the custom modules that you want to appear on the screen as you play

        for enemy in utils.enemies:
            if modules[Enemy][enemy['state']] == "Rect":
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(enemy['object'].x - utils.camerax, enemy['object'].y - utils.cameray, utils.size, utils.size))
            else:
                # Load images instead 
                # {"img":<image dir>, "times":4}
                pass
        
        for object__ in utils.objects:
            if modules[Object]['standing'] == "Rect":
                pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(object__['object'].x - utils.camerax, object__['object'].y - utils.cameray, utils.size, utils.size))

##########################################################

        # Update sprites, add your sprite's update function here

        Player.update()
        Enemy.update()
        Object.update()

        ##########################################################
        pygame.display.update()


def blitState(obj, module):
    screen = utils.screen
    for x in module[obj['state']]:
        for y in range(x['times']):
            screen.blit(x['image'], (obj['object'].x - utils.camerax, obj['object'].y - utils.cameray))

if __name__ == "__main__":
    run()


