import utils
import physics
import util_functions

class Enemy:
    def update(self):
        for enemy in utils.enemies:
            collide = physics.move(0, utils.gravity, enemy)
            distance = util_functions.distance(enemy['object'].x, utils.player['object'].x, enemy['object'].y, utils.player['object'].y)
            if distance < 100:
                if utils.player['object'].x < enemy['object'].x:
                    collide = physics.move(-3, 0, enemy)
                else:
                    collide = physics.move(3, 0, enemy)
