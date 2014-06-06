import pygame
from pygame.locals import *
import utils
import sys
import json
import pickle
import os
import player as player_

def main():
    screen = utils.screen
    
    xc = yc = 0
    for y in xrange(utils.resolution[1] / utils.size):
        for x in xrange(utils.resolution[0] / utils.size):
            utils.collision_map.append({"object":pygame.Rect(xc, yc, utils.size,utils.size), "color":(255,255,255)}) 
            xc += utils.size
        xc = 0
        yc += utils.size

    if os.path.exists(sys.argv[1]):
        data = json.loads(pickle.loads(open(sys.argv[1], 'rb').read()))
        for on, x in enumerate(data['map']):
            utils.collision_map.append({"object":pygame.Rect(data['map'][on][0], data['map'][on][1], utils.size,utils.size), "color":(0,0,0)}) 
    
        if data['player']:
            utils.player = pygame.Rect(data['player'][0], data['player'][1], utils.size,utils.size)

    clock = pygame.time.Clock()
    modes = ["block", "player", "object", "enemy", "endpoint", "erase"]
    mode_on = 0
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 25)
    



    # Initalize objects that interact with world

    Player = player_.Player()    


    while True:
        clock.tick(35)
        mode = modes[mode_on]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_s:
                    map_ = []
                    for x in utils.collision_map:
                        if x['color'] == (0, 0, 0):
                            map_.append((x['object'].x, x['object'].y))
                    print 'Saved'
                    if utils.player:
                        data = json.dumps({"map":map_, "player":[utils.player.x, utils.player.y], "enemies":utils.enemies, "objects":utils.objects, "endpoints":utils.endpoints})
                    else:
                        data = json.dumps({"map":map_, "player":None, "enemies":utils.enemies, "objects":utils.objects})
                    with open(sys.argv[1], 'wb') as file:
                        file.write(pickle.dumps(data))
                    map_ = None
                
                if event.key == K_m:

                    if mode_on == len(modes) - 1:
                        mode_on = 0
                    else:
                        mode_on += 1
                    
                if event.key == K_SPACE:
                    utils.camerax = utils.cameray = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == "block":
                    pos = pygame.mouse.get_pos()
                    for wall in utils.collision_map:
                        if wall['object'].collidepoint(pos[0] + utils.camerax, pos[1] + utils.cameray):
                            wall['color'] = (0,0,0)
            
                            utils.collision_map.append({"object":pygame.Rect(wall['object'].x, wall['object'].y, utils.size,utils.size), "color":(255,255,255)})
                            break 

                if mode == "player":
                    pos = pygame.mouse.get_pos()
                    utils.player = pygame.Rect(pos[0] + utils.camerax, pos[1] + utils.cameray, utils.size,utils.size)
                
                if mode == "erase":
                    pos = pygame.mouse.get_pos()
                    for wall in utils.collision_map:
                        if wall['color'] == (0,0,0):
                            if wall['object'].collidepoint(pos[0] + utils.camerax, pos[1] + utils.cameray):
                                wall['color'] = (255,255,255)
                                break

        key = pygame.key.get_pressed()

        # This moves the camera around the edit field, we have to also move each individual grid block so that we can keep adding blocks to other places.

        if key[K_RIGHT]:
            for x in utils.collision_map:
                if x['color'] == (255,255,255):
                    x['object'].x += 5

            utils.camerax += 5
        if key[K_LEFT]:
            for x in utils.collision_map:
                if x['color'] == (255,255,255):
                    x['object'].x -= 5
            utils.camerax -= 5
        if key[K_DOWN]:
            for x in utils.collision_map:
                if x['color'] == (255,255,255):
                    x['object'].y += 5
            utils.cameray += 5
        if key[K_UP]:
            for x in utils.collision_map:
                if x['color'] == (255,255,255):
                    x['object'].y -= 5
            utils.cameray -= 5

        screen.fill((255,255,255))

        for x in utils.collision_map:
            if x['color'] == (255,255,255):
                pygame.draw.rect(screen, x['color'], x['object'])

        for x in utils.collision_map:
            if x['color'] == (0,0,0):
                pygame.draw.rect(screen, x['color'], pygame.Rect(x['object'].x - utils.camerax, x['object'].y - utils.cameray, utils.size,utils.size))

        if utils.player: 
            pygame.draw.rect(screen, (0,255,255), pygame.Rect(utils.player.x - utils.camerax, utils.player.y - utils.cameray, utils.size,utils.size))
        screen.blit(font.render(mode, -1, (0,0,0)), (10, 10))
        
        
        
        
        # Update objects on screen
        
        
        Player.update()    
        
        
        pygame.display.update()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "You need to specify a map file: python edit.py <map.lvl>"
    else:

        main()
