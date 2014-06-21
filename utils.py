import pygame

# Variables
resolution = (900, 600)
screen = pygame.display.set_mode(resolution) # Set the main screen here so that every module has access to it


#################### Custom module holding, add empty arrays or variables as they are needed for new moduels ########################################

player = {"object":None, "state":"standing"} # Player object set at run time (described by a JSON file)
endpoints = [] # This is the end of the level, it will then look at maps.json to see what to load next
enemies = [] # Enemies set at run time (Also described by a JSOn file, the number is determined by the map)
objects = [] # Objects set at run time (boxes, items, etc, described by a JSON file)




###### Static variables

camerax = cameray = 0 # Camera variables 
collision_map = [] # This is a list of walls that the user can collide into set at run time


##### Editable Fields ####

background_fill = (255,255,255)
speed = 5
gravity = 3
jump_speed = 10
jump_time_in_air = 0.15 # Seconds moving upward (determines how high the object will jump)
size = 16 # Size of blocks
title = "3 Prong Engine"
camera_on = False # This should only be True when there is a set background image, otherwise it won't look right

###########################################################

onground = False # To control graity and jumping
lastmove = "right"
jump = None # This is set to a base time when the player has the player jump
map_on = None # Current map file
map_ = None # Stores data of modules/maps.json

