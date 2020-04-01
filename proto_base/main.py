#!env python3
"""
Object in the world.

Tasks:
    1. Make player character to stop on the walls.
"""
import pygame
from library import Game, Player, Wall


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
    player.set_position(64, 32)

    # Create few walls
    for pos in [
            (0, 0),
            (0, 32),
            (0, 64),
            (0, 96),
            (32, 96),
            ]:
        game.add_object(Wall.create_wall(game, *pos))

    # Set up the drawing window
    screen = pygame.display.set_mode([game.screen["width"], game.screen["height"]])

    # Start measuring time
    clock = pygame.time.Clock()
    dt = clock.tick()

    game.start()
    while game.active:
        # Read any inputs from keyboard - this function will return False if
        # we supposed to stop game (closed window or pressed Esc)
        game.read_input()

        # If user stopped game do not draw this frame
        if not game.active:
            continue

        # Fill the background with white
        screen.fill(game.bg_colour)

        player.update(dt)
        player.draw(screen)

        for obj in game.all_objects:
            obj.draw(screen)

        # Flip the display
        pygame.display.flip()

        # Time passed since last call of tick()
        dt = clock.tick(60)


if __name__ == '__main__':
    # When executing script from command line start main function
    main()
