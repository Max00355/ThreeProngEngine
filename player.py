import utils
import physics
from pygame.locals import *
import pygame
import time

class Player:
    def update(self):
        # Let's set the camera

        utils.camerax = utils.player[0]
        
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

        # Gravity
        if not utils.jump: 
            collidewith = physics.move(0, utils.gravity, utils.player) 
        
        else:
            if time.time() - utils.jump >= utils.jump_time_in_air:
                utils.jump = None
            else:
                collidewith = physics.move(0, -utils.jump_speed, utils.player)
