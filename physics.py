import utils

# This is the collision engine, all game objects will be passed through this module.

def move(x, y, obj):
    # Moves the object and returns the final x and y coordinnate that it will move

    if isinstance(obj, dict):
        obj = obj['object']
    walls = utils.collision_map
    enemies = utils.enemies
    objects = utils.objects
    endpoints = utils.endpoints
    if not obj: # For edit mode
        return
    obj.x += x
    obj.y += y
    if utils.camera_on and obj == utils.player:
        utils.camerax += x
        utils.cameray += y
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
                    if obj == utils.player['object']:
                        utils.onground = True
                if y < 0: # Moving up
                    obj.y -= y
                

                return ("wall", x, y, wall)

######################################################## CUSTOM MODULE LOOPS ##############################################################

    """
    
        If nothing else is required but basic collision call collideit() and the function will take care of everything

        It is best to return a tuple so that the other modules know in which direction the object was moving.

    """


    for enemy in enemies:
        enemy = enemy['object']
        if enemy.colliderect(obj) and enemy != obj:
            collideit(x, y, obj) 
            return ("enemy", x, y, enemy)
        
    for object_ in objects: 
        object_ = object_['object']
        if object_.colliderect(obj) and obj != object_:
            collideit(x, y, obj) 
            return ("object", x, y, object_)


######################################################## END OF CUSTOM MODULE LOOPS #######################################################


    for endpoint in endpoints:
        if obj.colliderect(endpoint):
            return ("endpoint", x, y, endpoint)

    if utils.camera_on and obj == utils.player['object']:    
        utils.camerax += x                                                                                                                                                                             
        utils.cameray += y
    
    return None




def collideit(x, y, obj):
    
    if x > 0:
        obj.x -= x
            
    if x < 0:
        obj.x -= x

    if y > 0:
        obj.y -= y

    if y < 0:
        obj.y -= y                                                                                                                                                                             
    if utils.camera_on and obj == utils.player['object']:    
        utils.camerax -= x
        utils.cameray -= y

