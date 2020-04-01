#!env python3
"""
Move a sprite in a window.

Tasks:
    1. Move a sprite to left when left arrow is pressed (K_LEFT) and right
       when right arrow (K_RIGHT). Note that there are two types of key events
       pygame.KEYDOWN and pygame.KEYUP.
       If this is too difficult please see next script.
    2. With that change can you stop sprite from moving outside of the screen?
"""
import pygame
from pygame import K_ESCAPE, QUIT


# As long as this variable is True game will be running
active = True

# Some global variables
SCREEN_SIZE = 128
BKG_COLOUR = (255, 255, 255)  # White
SPRITE_SPEED = 5

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

    # Start measuring time
    clock = pygame.time.Clock()
    clock.tick()

    sprite_y = 32

    while active:
        # Time passed since last call of tick()
        dt = clock.tick()

        # Read any inputs from keyboard - this function will return False if
        # we supposed to stop game (closed window or pressed Esc)
        active = read_input()

        # If user stopped game do not draw this frame
        if not active:
            continue

        # Fill the background with white
        screen.fill(BKG_COLOUR)

        # How far we want to move object this turn
        # We determine how far to move object base on how much time passed
        # since last framw
        if dt:
            dmove = SPRITE_SPEED / dt / 1000
        else:
            dmove = 0

        # Draw an image
        my_img = pygame.image.load('Sprite-0001.png')
        sprite_y = sprite_y + dmove
        screen.blit(my_img, (32, sprite_y))

        # Flip the display
        pygame.display.flip()


if __name__ == '__main__':
    # When executing script from command line start main function
    main()
