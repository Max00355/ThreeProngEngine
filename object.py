import physics
import utils

class Object:
    def update(self):
        for object in utils.objects:
            physics.move(0, utils.gravity, object);
            
            # The object doesn't really do anything right now, it is just a moveable wall.
