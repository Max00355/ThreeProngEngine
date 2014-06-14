import utils
import physics
import util_functions

class Enemy:
    def update(self):
        for enemy in utils.enemies:
            enemy = utils.enemies[0]
            collide = physics.move(0, 5, enemy)
            distance = util_functions.distance(enemy.x, utils.player.x, enemy.y, utils.player.y)
            if distance < 50:
                if utils.player.x < enemy.x:
                    collide = physics.move(-1, 0, enemy)
                else:
                    collide = physics.move(1, 0, enemy)
