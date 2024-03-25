# Import modules
import pygame
import sys
from pygame.locals import *
import random

# Declare constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 500
TARGET_WIDTH_HEIGHT = 180
N_PIXELS_TO_MOVE = 3
RECT_X = 0
RECT_Y = 0
RECT_CHANGE_X = 11
RECT_CHANGE_Y = 11
RECT_SIZE_X = 100
RECT_SIZE_Y = 100


# Initialize pygame
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


# Gameloop
while True:
    # Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the window
    window.fill(BLACK)

    # Drawing primitives
    # Line
    pygame.draw.line(
        window,      # the surface where 
        (255, 0, 0), # color
        (10, 10),    # start position
        (100, 30),   # end position
        4            # width
    )

    # Circle
    pygame.draw.circle(
        surface = window,
        color = (0, 255, 0),
        center = (100, 300),
        radius = 50,
        width = 0
    )

    # Rectangle
    pygame.draw.rect(
        window,
        (100, 0, 0),
        (250, 150, 100, 50),
        0
    )

    # Ellipse
    pygame.draw.ellipse(
        window,
        (100, 100, 0),
        (250, 250, 80, 40),
        11
    )

    pygame.draw.aaline(
        window,
        (155, 155, 155),
        (1,10),
        (500, 90),
    )

    pygame.draw.rect(
        window,
        (0, 0, 255),
        (RECT_X, RECT_Y, RECT_SIZE_X, RECT_SIZE_Y),
    )

    RECT_X, RECT_Y = RECT_X + RECT_CHANGE_X, RECT_Y + RECT_CHANGE_Y

    if RECT_Y + RECT_SIZE_Y >= WINDOW_HEIGHT or RECT_Y <= 0:
        RECT_CHANGE_Y = -RECT_CHANGE_Y
    if RECT_X + RECT_SIZE_X >= WINDOW_WIDTH or RECT_X <= 0:
        RECT_CHANGE_X = -RECT_CHANGE_X

    # Update the window
    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)


