import pygame

class Game():
    def __init__(self):
        """
        Set basic configuration for a game that can be always accessed.
        """
        self.screen = {
            "width": 240,
            "height": 240,
        }

        self.bg_colour = (255, 255, 255)

        self.active = False

        self.reset_keys()

    def start(self):
        self.active = True

    def stop(self):
        self.active = False

    def reset_keys(self):
        self.keys = {
            "left": False,
            "right": False,
            "up": False,
            "down": False,
        }

class Object():
    def __init__(self, game):
        self.pos = [0, 0]

        self.game = game

        self.image = None

    def update(self, dt):
        """
        """

    def draw(self, surface):
        """
        """
        if self.image:
            surface.blit(
                self.image,
                self.pos
            )

class Wall(Object):
    def __init__(self, game):
        super().__init__(game)

        self.image = pygame.image.load('Sprite-0002.png')

    @staticmethod
    def create_wall(game, x, y):
        obj = Wall(game)

        obj.pos[0] = x
        obj.pos[1] = y

        return obj


class Character(Object):
    def __init__(self, game):
        super().__init__(game)

        self.health = 100
        self.speed = 24

    def set_position(self, x, y):
        self.pos[0] = x
        self.pos[1] = y

    def get_position(self):
        return int(self.pos[0]), int(self.pos[1])

    def move(self, x, y=0):
        self.pos[0] += x
        self.pos[1] += y


class Player(Character):
    """
    """
    def __init__(self, game):
        super().__init__(game)

        # Setup player's image
        self.image = pygame.image.load('Sprite-0001.png')

    def update(self, dt):
        if self.game.keys["left"] and dt:
            self.pos[0] -= int(self.speed * dt / 100)
            if self.pos[0] < 0:
                self.pos[0] = 0
        elif self.game.keys["right"] and dt:
            self.pos[0] += int(self.speed * dt / 100)
            if self.pos[0] > self.game.screen["width"] - 32:
                self.pos[0] = self.game.screen["width"] - 32

        if self.game.keys["up"] and dt:
            self.pos[1] -= int(self.speed * dt / 100)
            if self.pos[1] < 0:
                self.pos[1] = 0
        elif self.game.keys["down"] and dt:
            self.pos[1] += int(self.speed * dt / 100)
            if self.pos[1] > self.game.screen["height"] - 32:
                self.pos[1] = self.game.screen["height"] - 32


class Enemy(Character):
    """
    """

class Zombie(Enemy):
    def __init__(self, game):
        super().__init__(game)
        self.speed = 10

class FastZombie(Zombie):
    def __init__(self, game):
        super().__init__(game)
        self.speed = 24
        self.health = 40

