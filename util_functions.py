import math
import json
import pygame
import utils
import play
import json

def load_map_module():
    return json.loads(open("modules/maps.json").read())

def distance(x1 ,x2, y1, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def loader(path):
    image = pygame.image.load(path)
    return image.convert_alpha()

def next_map():
    data = utils.map_[utils.map_on]
    play.load_collision_map(data['next'])
    utils.map_on = data['next']
    if utils.camera_on: # This will center the camera on the player
        utils.camerax = (utils.player.x / (utils.resolution[0] / 2)) - utils.resolution[0] / 3
        utils.cameray = (utils.player.y / (utils.resolution[1] / 2)) - utils.resolution[1] / 6
    return data['next']
