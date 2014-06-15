import utils
import physics
from pygame.locals import *
import pygame
import time
import util_functions

class Player:
    def update(self):
        # Let's set the camera

        # Any movement by player
        x = y = 0
        key = pygame.key.get_pressed()
        if key[K_d]:
            x = utils.speed
            utils.lastmove = "right"
        if key[K_a]:
            x = -utils.speed
            utils.lastmove = "left"
        if key[K_w] and utils.onground:
            utils.onground = False
            utils.jump = time.time()
            
        if x or y:
            collidewith = physics.move(x, y, utils.player) 
            if collidewith:
                if collidewith[0] == "endpoint":
                    util_functions.next_map()
            
                if collidewith[0] == "object":
                    collidewith[3].x += collidewith[1]
                    collidewith[3].y += collidewith[2]

        # Gravity

        if not utils.jump: 
            collidewith = physics.move(0, utils.gravity, utils.player) 
        
        else:
            if time.time() - utils.jump >= utils.jump_time_in_air:
                utils.jump = None
            else:
                collidewith = physics.move(0, -utils.jump_speed, utils.player)
