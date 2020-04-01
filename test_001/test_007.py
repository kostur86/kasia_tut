#!env python3
"""
Object in the world.

Tasks:
    1. Make player character to stop on the walls.
"""
import pygame
from pygame import K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_DOWN, QUIT
from library_007 import Game, Player, Wall

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

            elif event.key == K_UP:
                game.keys["up"] = True

            elif event.key == K_DOWN:
                game.keys["down"] = True


        # Did the user hit a key?
        if event.type == pygame.KEYUP:

            if event.key == K_LEFT:
                game.keys["left"] = False

            elif event.key == K_RIGHT:
                game.keys["right"] = False

            elif event.key == K_UP:
                game.keys["up"] = False

            elif event.key == K_DOWN:
                game.keys["down"] = False

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

    # Create few walls
    walls = [
        Wall.create_wall(game, 0, 0),
        Wall.create_wall(game, 120, 120),
    ]

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

        for wall in walls:
            wall.draw(screen)

        # Flip the display
        pygame.display.flip()

        # Time passed since last call of tick()
        dt = clock.tick(60)


if __name__ == '__main__':
    # When executing script from command line start main function
    main()
