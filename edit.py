import pygame
from pygame.locals import *
import utils
import sys
import json
import pickle
import os

def main():
    screen = utils.screen
    utils.player = None

    pygame.display.set_caption("Edit")

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

        if data['objects']:
            for x in data['objects']:
                utils.objects.append(pygame.Rect(x[0], x[1], utils.size, utils.size))

        if data['enemies']:
            for x in data['enemies']:
                utils.enemies.append(pygame.Rect(x[0], x[1], utils.size, utils.size))

        if data['endpoints']:
            for x in data['endpoints']:
                utils.endpoints.append(pygame.Rect(x[0], x[1], utils.size, utils.size))


    clock = pygame.time.Clock()
    modes = ["block", "player", "object", "enemy", "endpoint", "object", "erase"]
    mode_on = 0
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 25)
    

    while True:
        clock.tick(35)
        mode = modes[mode_on]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_s:
                    map_ = []
                    enemies = []
                    objects = []
                    endpoints = []

                    for m in utils.collision_map:
                        if m['color'] == (0, 0, 0):
                            map_.append((m['object'].x, m['object'].y))

                    for e in utils.enemies:
                        enemies.append((e.x, e.y))

                    for o in utils.objects:
                        objects.append((o.x, o.y))

                    for end in utils.endpoints:
                        endpoints.append((end.x, end.y))
                    print 'Saved'
                    if utils.player:
                        data = json.dumps({"map":map_, "player":[utils.player.x, utils.player.y], "enemies":enemies, "objects":objects, "endpoints":endpoints})
                    else:
                        data = json.dumps({"map":map_, "player":None, "enemies":enemies, "objects":objects, "endpoints":endpoints})
                    with open(sys.argv[1], 'wb') as file:
                        file.write(pickle.dumps(data))
                    map_ = enemies = objects = endpoints = None
                     
                if event.key == K_m:

                    if mode_on == len(modes) - 1:
                        mode_on = 0
                    else:
                        mode_on += 1
                    
                if event.key == K_SPACE:
                    utils.camerax = utils.cameray = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if mode == "block":
                    for wall in utils.collision_map:
                        if wall['object'].collidepoint(pos[0] + utils.camerax, pos[1] + utils.cameray):
                            wall['color'] = (0,0,0)
            
                            utils.collision_map.append({"object":pygame.Rect(wall['object'].x, wall['object'].y, utils.size,utils.size), "color":(255,255,255)})
                            break 

                elif mode == "player":
                    for wall in utils.collision_map:
                        if wall['object'].collidepoint(pos[0] + utils.camerax, pos[1] + utils.cameray):
                            utils.player = pygame.Rect(wall['object'].x + utils.camerax, wall['object'].y + utils.cameray, utils.size, utils.size)

                elif mode == "erase":
                    for wall in utils.collision_map:
                        if wall['color'] != (255,255,255):
                            if wall['object'].collidepoint(pos[0] + utils.camerax, pos[1] + utils.cameray):
                                wall['color'] = (255,255,255)
                                break

                    for point in utils.endpoints:
                        if point.collidepoint(pos[0] + utils.camerax, pos[1] + utils.cameray):
                            utils.endpoints.remove(point)
                            break
                    
                    for object_ in utils.objects:
                        if object_.collidepoint(pos[0] + utils.camerax, pos[1] + utils.cameray):
                            utils.objects.remove(object_)
                            break

                    for enemy in utils.enemies:
                        if enemy.collidepoint(pos[0] + utils.camerax, pos[1] + utils.cameray):
                            utils.enemies.remove(enemy)
                            break
                    
                    if utils.player and utils.player.collidepoint(pos[0] + utils.camerax, pos[1] + utils.cameray):
                        utils.player = None

                elif mode == "endpoint":
                    for wall in utils.collision_map:
                        if wall['object'].collidepoint(pos[0] + utils.camerax, pos[1] + utils.cameray):
                            utils.endpoints.append(pygame.Rect(wall['object'].x + utils.camerax, wall['object'].y + utils.cameray, utils.size, utils.size))
       
                elif mode == "enemy":
                    for wall in utils.collision_map:
                        if wall['object'].collidepoint(pos[0] + utils.camerax, pos[1] + utils.cameray):
                            utils.enemies.append(pygame.Rect(wall['object'].x + utils.camerax, wall['object'].y + utils.cameray, utils.size, utils.size))

                elif mode == "object":
                    for wall in utils.collision_map:
                        if wall['object'].collidepoint(pos[0] + utils.camerax, pos[1] + utils.cameray):
                            utils.objects.append(pygame.Rect(wall['object'].x + utils.camerax, wall['object'].y + utils.cameray, utils.size, utils.size))


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
            if x['color'] == (255,255,255): # Draw grid
                pygame.draw.rect(screen, x['color'], x['object'])

        for x in utils.collision_map:
            if x['color'] == (0,0,0): # Draw wall
                pygame.draw.rect(screen, x['color'], pygame.Rect(x['object'].x - utils.camerax, x['object'].y - utils.cameray, utils.size,utils.size))
        
        for x in utils.enemies:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x.x - utils.camerax, x.y - utils.cameray, utils.size,utils.size)) 

        for x in utils.objects:
            pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(x.x - utils.camerax, x.y - utils.cameray, utils.size,utils.size))

        for x in utils.endpoints:
            pygame.draw.rect(screen, (0, 100, 255), pygame.Rect(x.x - utils.camerax, x.y - utils.cameray, utils.size,utils.size))

        for x in utils.enemies:
            pygame.draw.rect(screen, ( 255, 0, 0), pygame.Rect(x.x - utils.camerax, x.y - utils.cameray, utils.size, utils.size))


        if utils.player: 
            pygame.draw.rect(screen, (0,255,255), pygame.Rect(utils.player.x - utils.camerax, utils.player.y - utils.cameray, utils.size,utils.size))
        screen.blit(font.render(mode, -1, (0,0,0)), (10, 10))
        
        pygame.display.update()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "You need to specify a map file: python edit.py <map.lvl>"
    else:

        main()
