import pygame
import math
import os

# Variables
resolution = (800, 600)
screen = pygame.display.set_mode(resolution) # Set the main screen here so that every module has access to it
player = None # Player object set at run time (described by a JSON file)
enemies = [] # Enemies set at run time (Also described by a JSOn file, the number is determined by the map)
objects = [] # Objects set at run time (boxes, items, etc, described by a JSON file)
camerax = cameray = 0 # Camera variables
collision_map = [] # This is a list of walls that the user can collide into set at run time
speed = 5
gravity = 5

# Userful functions

def distance(x1 ,x2, y1, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def loader(path):
    image = pygame.image.load(path)
    return image.convert_alpha()
