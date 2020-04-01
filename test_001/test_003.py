#!env python3
"""
Draw a sprite in a PyGame window.
"""
import pygame
from pygame import K_ESCAPE, QUIT


# As long as this variable is True game will be running
active = True

# Some global variables
SCREEN_SIZE = 128
BKG_COLOUR = (255, 255, 255)  # White


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
        if event.type == pygame.KEYDOWN:

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

        # Draw an image
        my_img = pygame.image.load('Sprite-0001.png')
        screen.blit(my_img, (32, 32))

        # Flip the display
        pygame.display.flip()


if __name__ == '__main__':
    # When executing script from command line start main function
    main()
