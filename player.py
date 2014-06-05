import utils
import physics

class Player:
    def update(self, x = 0, y = 0):
        # Any movement by player
        if x or y:
            x, y, collidewith = physics.move(x, y, utils.player)
            utils.player.x += x
            utils.player.y += y

        # Gravity

        x, y, collidewith = physics.move(0, utils.gravity, utils.player) 
        utils.player.y += y
