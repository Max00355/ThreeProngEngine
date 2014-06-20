import physics
import utils
import util_functions

class Object:
    def update(self):
        for object in utils.objects:
            physics.move(0, utils.gravity, object);
            distance = util_functions.distance(object['object'].x, utils.player['object'].x, object['object'].y, utils.player['object'].y) 
            if distance <= 20.8:
                if utils.lastmove == "right":
                    physics.move(utils.speed, 0, object)
                elif utils.lastmove == "left":
                    physics.move(-utils.speed, 0, object)

            # The object doesn't really do anything right now, it is just a moveable wall.
