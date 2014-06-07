import pygame

# Variables
resolution = (800, 600)
screen = pygame.display.set_mode(resolution) # Set the main screen here so that every module has access to it
player = None # Player object set at run time (described by a JSON file)
endpoints = [] # This is the end of the level, it will then look at maps.json to see what to load next
enemies = [] # Enemies set at run time (Also described by a JSOn file, the number is determined by the map)
objects = [] # Objects set at run time (boxes, items, etc, described by a JSON file)
camerax = cameray = 0 # Camera variables
collision_map = [] # This is a list of walls that the user can collide into set at run time


##### Editable Fields ####

speed = 5
gravity = 3
jump_speed = 10
jump_time_in_air = 0.15 # Seconds moving upward
size = 16 # Size of blocks

###########################################################

onground = False
lastmove = "right" # To determine position of sprite image
jump = None
map_on = None
map_ = None # Stores data of modules/maps.json

