# Import modules
import pygame
import sys
from pygame.locals import *
import random
import pathlib

# Declare constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 150
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 300
TARGET_Y = 10
TARGET_WIDTH_HEIGHT = 250
N_PIXELS_TO_MOVE = 10
BASE_PATH = pathlib.Path(__file__).resolve().parent
IMAGES_FOLDER = pathlib.Path("img").resolve()
SOUNDS_FOLDER = pathlib.Path("sounds").resolve()

# Initializing the environment
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


# Load assets
pygame.mixer.music.load(BASE_PATH / SOUNDS_FOLDER / "bgMusic.wav")
pygame.mixer.music.play(-1, 0.0)

# Initialize variables



# Main gameloop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pass

    







    window.fill(BLACK)

    pygame.draw.line(
        window,
        (100, 100, 150),
        (30, 30),
        (20, 60),
        10
    )

    pygame.draw.circle(
        window,
        (200, 200, 100),
        (250, 50),
        100,
        1
    )





    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)

    