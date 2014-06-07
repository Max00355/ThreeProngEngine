import math
import json
import pygame
import utils
import play

def distance(x1 ,x2, y1, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def loader(path):
    image = pygame.image.load(path)
    return image.convert_alpha()

def next_map():
    data = utils.map_[utils.map_on]
    play.load_collision_map(data['next'])
    utils.map_on = data['next']
    return data['next']
