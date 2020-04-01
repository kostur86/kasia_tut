#!env python3
"""
Simple script to draw circle on a screen.

To exit program press Ctrl+C in a terminal.

Tasks:
    1. Draw rectangle using this function:
        pygame.draw.rect(Surface, colour, Rectangle)
                            ↑       ↑         ↑
                            │       │         └─── Rectangle dimensions as a
                            │       │              list - (x of left corner,
                            │       │                      y of let corner,
                            │       │                      width, height)
                            │       └───────────── Colour of a rectangle as a
                            │                      list - (red, green, blue)
                            └───────────────────── Surface (canvas) to draw
                                                   on

    2. Learn how coordinate system works in PyGame - draw a circle at (0, 0)
       location, draw circle in each corner of a screen (SCREEN_SIZE, 0),
       (0, SCREEN_SIZE), (SCREEN_SIZE, SCREEN_SIZE)

    3. Draw a caterpillar using multiple green circles (body and nose) and
       blue circle as an eye. No legs or mouth at the moment.
"""
import pygame

# As long as this variable is True game will be running
active = True

# Some global variables
SCREEN_SIZE = 128
CIRCLE_DIMM = int(SCREEN_SIZE / 2 / 2)  # What size is the circle?
BKG_COLOUR = (255, 255, 255)  # White
CIRCLE_COLOUR = (0, 0, 255)  # Blue

def main():
    """
    This is main function - it will be executed only explicitly, like this:
        import main
        main.main()

    or when executing script from command line:
        python3 main.py
    """
    # Initialize PyGame library - this is required by any program that is
    # using PyGame. It have to be done before any function from pygame library
    # is called.
    pygame.init()

    # Set up the drawing window of a exact size, it returns a canvas (called
    # surface) that you can draw on - pass it to some functions or use it's
    # methods.
    screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])

    # This is main loop of a game.
    while active:
        # Fill whole window with a solid colour.
        screen.fill(BKG_COLOUR)

        # Draw a solid blue circle in the center
        pygame.draw.circle(
            screen,  # Where to draw circle (surface, context or canvas)
            CIRCLE_COLOUR,  # Colour of circle
            (int(SCREEN_SIZE / 2), int(SCREEN_SIZE / 2)),  # Location of a
                # center of a circle - (x, y), have to be integer (num of
                # points from start of coordinate system)
            CIRCLE_DIMM  # Radius of a circle
        )

        # All things in pygame are being drawn in buffer so you want see them
        # till you "flip" the display.
        # Execute this every time you want to show everything you drawn on a
        # Surface
        pygame.display.flip()


if __name__ == '__main__':
    # When executing script from command line start main function
    main()
