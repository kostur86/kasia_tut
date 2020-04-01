import pygame
from pygame import K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_DOWN, QUIT

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

        self.all_objects = []

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

    def add_object(self, obj):
        if obj not in self.all_objects:
            self.all_objects.append(obj)

    def remove_object(self, obj):
        if obj in self.all_objects:
            self.all_objects.remove(obj)

    def read_input(self):
        """
        Read user input and set game state.

        Returns:
            bool: Should game still be running?
        """
        # Look at every event in the queue
        for event in pygame.event.get():

            # Did the user hit a key?
            if event.type == pygame.KEYDOWN:

                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    self.stop()

                elif event.key == K_LEFT:
                    self.keys["left"] = True

                elif event.key == K_RIGHT:
                    self.keys["right"] = True

                elif event.key == K_UP:
                    self.keys["up"] = True

                elif event.key == K_DOWN:
                    self.keys["down"] = True


            # Did the user hit a key?
            if event.type == pygame.KEYUP:

                if event.key == K_LEFT:
                    self.keys["left"] = False

                elif event.key == K_RIGHT:
                    self.keys["right"] = False

                elif event.key == K_UP:
                    self.keys["up"] = False

                elif event.key == K_DOWN:
                    self.keys["down"] = False

            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                self.stop()

class Object():
    def __init__(self, game):
        self.game = game

        self.image = None
        self.pos = [0, 0]
        self.size = [0, 0]
        self.params = {
            "blocking": True,
        }

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

    def over(self, obj, new_pos=None):
        if new_pos is None:
            new_pos = self.pos

        if (
                not (new_pos[0] + self.size[0] <= obj.pos[0] or new_pos[0] >= obj.pos[0] + obj.size[0]) and
                not (new_pos[1] + self.size[1] <= obj.pos[1] or new_pos[1] >= obj.pos[1] + obj.size[1])
            ):
            return True
        return False


class Wall(Object):
    def __init__(self, game):
        super().__init__(game)

        self.image = pygame.image.load('img/wall_001.png')
        self.size = [32, 32]

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
        self.image = pygame.image.load('img/player_base.png')
        self.size = [32, 32]

    def _move(self, dx, dy):
        new_pos = (
            self.pos[0] + dx,
            self.pos[1] + dy,
        )

        if (
                new_pos[0] <= 0 or new_pos[0] + self.size[0] >= self.game.screen["width"] or
                new_pos[1] <= 0 or new_pos[1] + self.size[1] >= self.game.screen["height"]
            ):
            return self.pos

        for obj in self.game.all_objects:
            if self.over(obj, new_pos):
                return self.pos

        return new_pos

    def update(self, dt):
        if self.game.keys["left"] and dt:
            self.pos = self._move(-int(self.speed * dt / 100), 0)
        elif self.game.keys["right"] and dt:
            self.pos = self._move(int(self.speed * dt / 100), 0)

        if self.game.keys["up"] and dt:
            self.pos = self._move(0, -int(self.speed * dt / 100))
        elif self.game.keys["down"] and dt:
            self.pos = self._move(0, int(self.speed * dt / 100))


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

