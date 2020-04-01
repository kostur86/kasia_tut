#!env python3
"""
Script that add listening of a user commands.

Script can now exit game! No need to press Ctrl + C any more - you can close
window or press Esc.

Tasks:
    1. Knowing that pygame.K_q stands for "Q" key swap displayed colour of
       the circle when user presses "Q".

    2. Program 4 different locations of a circle. When user press 1, 2, 3 or 4
       move circle to respective location.
"""
import pygame
from pygame import K_ESCAPE, QUIT


# As long as this variable is True game will be running
active = True

# Some global variables
SCREEN_SIZE = 128
CIRCLE_DIMM = int(SCREEN_SIZE / 2 / 2)
BKG_COLOUR = (255, 255, 255)  # White
CIRCLE_COLOUR = (0, 0, 255)  # Blue


def read_input():
    """
    Read user input and return state of running the game.

    If user press Esc or exit game window stop game main loop.

    Returns:
        bool: Should game still be running?
    """
    # Should we still run game after parsing all inputs?
    running = True

    # Look at every event in the queue
    for event in pygame.event.get():

        # Did the user hit a key?
        if event.type == pygame.KEYDOWN:  # Can you see the difference between
                                          # KEYDOWN and K_ESCAPE difference?

            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    return running


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

    # Set up the drawing window
    screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])

    while active:
        # Read any inputs from keyboard - this function will return False if
        # we supposed to stop game (closed window or pressed Esc)
        active = read_input()

        # If user stopped game do not draw this frame
        if not active:
            continue

        # Fill the background with white
        screen.fill(BKG_COLOUR)

        # Draw a solid blue circle in the center
        pygame.draw.circle(
            screen,  # Where to draw circle (context, canvas)
            CIRCLE_COLOUR,  # Colour of circle
            (int(SCREEN_SIZE / 2), int(SCREEN_SIZE / 2)),  # Location of a
                # center of a circle - (x, y), have to be integer (num of
                # points from start of coordinate system)
            CIRCLE_DIMM  # Radius of a circle
        )

        # Flip the display
        pygame.display.flip()


if __name__ == '__main__':
    # When executing script from command line start main function
    main()
