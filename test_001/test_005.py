#!env python3
"""
Use of Python classes.

Basic Python class knowledge is required.

Tasks:
    1. Add up-down movement (and diagonals).
"""
import pygame
from pygame import K_ESCAPE, K_LEFT, K_RIGHT, QUIT


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
        }

class Character():
    def __init__(self, game):
        """
        """
        self.health = 100
        self.speed = 24

        self.pos = [0, 0]

        self.game = game

        self.image = None

    def set_position(self, x, y):
        self.pos[0] = x
        self.pos[1] = y

    def get_position(self):
        return int(self.pos[0]), int(self.pos[1])

    def move(self, x, y=0):
        self.pos[0] += x
        self.pos[1] += y

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

def read_input(game):
    """
    Read user input and set game state.

    Args:
        game (Game): Current game state.

    Returns:
        bool: Should game still be running?
    """
    # Look at every event in the queue
    for event in pygame.event.get():

        # Did the user hit a key?
        if event.type == pygame.KEYDOWN:

            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                game.stop()

            elif event.key == K_LEFT:
                game.keys["left"] = True

            elif event.key == K_RIGHT:
                game.keys["right"] = True


        # Did the user hit a key?
        if event.type == pygame.KEYUP:

            if event.key == K_LEFT:
                game.keys["left"] = False

            elif event.key == K_RIGHT:
                game.keys["right"] = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            game.stop()


def main():
    """
    This is main function - it will be executed only explicitly, like this:
        import main
        main.main()

    or when executing script from command line:
        python3 main.py
    """
    global active

    # Initialize PyGame library
    pygame.init()

    game = Game()

    player = Player(game)
    player.set_position(32, 32)

    # Set up the drawing window
    screen = pygame.display.set_mode([game.screen["width"], game.screen["height"]])

    # Start measuring time
    clock = pygame.time.Clock()
    dt = clock.tick()

    game.start()
    while game.active:
        # Read any inputs from keyboard - this function will return False if
        # we supposed to stop game (closed window or pressed Esc)
        read_input(game)

        # If user stopped game do not draw this frame
        if not game.active:
            continue

        # Fill the background with white
        screen.fill(game.bg_colour)

        player.update(dt)
        player.draw(screen)

        # Flip the display
        pygame.display.flip()

        # Time passed since last call of tick()
        dt = clock.tick(60)


if __name__ == '__main__':
    # When executing script from command line start main function
    main()
