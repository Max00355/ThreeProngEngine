import utils
import physics
import util_functions

class Enemy:
    def update(self):
        for enemy in utils.enemies:
            collide = physics.move(0, utils.gravity, enemy)
            distance = util_functions.distance(enemy.x, utils.player.x, enemy.y, utils.player.y)
            if distance < 100:
                if utils.player.x < enemy.x:
                    collide = physics.move(-3, 0, enemy)
                else:
                    collide = physics.move(3, 0, enemy)
