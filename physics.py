import utils

# This is the collision engine, all game objects will be passed through this module.

def move(x, y, obj):
    # Moves the object and returns the final x and y coordinnate that it will move
    
    move_x = move_y = 0
    move_x += x
    move_y += y
    walls = utils.collision_map
    enemies = utils.enemies
    objects = utils.objects

    for wall in walls:
        if "color" in wall:
            if wall['color'] != (0,0,0): # Occurs only in edit mode, we don't want to collide with the grid.
                continue
        if "object" in wall:
            wall = wall['object'] # Occurs in edit mode
        if wall.colliderect(obj):
            collidewith = "wall"
            if x > 0:
                move_x -= x

            if x < 0:
                move_x += x
            
            if y > 0:
                move_y -= y

            if y < 0:
                move_y += y

            return (move_x, move_y, collidewith)


    for enemy in enemies:
        if "object" in enemy:
            enemy = enemy['object']
        if enemy.colliderect(obj):
            collidewith = "enemy"
            if x > 0:
                move_x -= x
            
            if x < 0:
                move_x += x

            if y > 0:
                move_y -= y

            if y < 0:
                move_y += y
            
            return (move_x, move_y, collidewith)
        
    for object_ in objects:
        if "object" in object_:
            object_ = object_['object'] 
        if object_.collide(obj):
            collidewith = "object"
            if x > 0:
                move_x -= x
            
            if x < 0:
                move_x += x
            
            if y > 0:
                move_y -= y

            if y < 0:
                move_y += y
            
            return (move_x, move_y, collidewith)

    return (move_x, move_y, None)
