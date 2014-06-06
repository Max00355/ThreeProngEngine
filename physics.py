import utils

# This is the collision engine, all game objects will be passed through this module.

def move(x, y, obj):
    # Moves the object and returns the final x and y coordinnate that it will move

    if isinstance(obj, dict):
        obj = obj['object']
    walls = utils.collision_map
    enemies = utils.enemies
    objects = utils.objects
    if not obj: # For edit mode
        return
    obj.x += x
    obj.y += y

    for wall in walls:
        if "color" in wall:
            if wall['color'] != (0,0,0): # Occurs only in edit mode, we don't want to collide with the grid.
                continue
        if "object" in wall:
            wall = wall['object'] # Occurs in edit mode
        
        for wall in walls:
            if isinstance(wall, dict):
                if wall['color'] != (0,0,0):
                    continue
                wall = wall['object']
            if wall.colliderect(obj):
                if x > 0: # Moving right
                    obj.x -= x
                if x < 0: # Moving left
                    obj.x -= x
                if y > 0: # Moving down
                    obj.y -= y
                    utils.onground = True
                if y < 0: # Moving up
                    obj.y -= y

                return "wall"


    for enemy in enemies:
        if "object" in enemy:
            enemy = enemy['object']
        if enemy.colliderect(obj):
            collidewith = "enemy"
            if x > 0:
                obj.x -= x
            
            if x < 0:
                obj.x += x

            if y > 0:
                obj.y -= y

            if y < 0:
                obj.y += y
            
            return collidewith
        
    for object_ in objects:
        if "object" in object_:
            object_ = object_['object'] 
        if object_.collide(obj):
            collidewith = "object"
            if x > 0:
                obj.x -= x
            
            if x < 0:
                obj.x += x
            
            if y > 0:
                obj.y -= y

            if y < 0:
                obj.y += y
           
            return collidewith


    return None
