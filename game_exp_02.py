# Import modules
import pygame
import sys
from pygame.locals import *
import random
import pathlib

# Declare constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 150
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 300
TARGET_Y = 10
TARGET_WIDTH_HEIGHT = 250
N_PIXELS_TO_MOVE = 3
BASE_PATH = pathlib.Path(__file__).resolve().parent
IMAGES_FOLDER = pathlib.Path("img").resolve()

# Initializing the environment
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


# Load assets
ball_image: pygame.Surface = pygame.image.load(BASE_PATH / IMAGES_FOLDER / "ball.png")
target: pygame.Surface = pygame.image.load(BASE_PATH / IMAGES_FOLDER / "plain.png")

# Initialize variables
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)
print(ball_x, ball_y)

# Create a target rect
target_rect = pygame.Rect(
    TARGET_X,
    TARGET_Y,
    TARGET_WIDTH_HEIGHT,
    TARGET_WIDTH_HEIGHT - 158
)


while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
                ball_x -= 15
            if event.key == pygame.K_DOWN:
                print("down")
                ball_y += 15
                
            if event.key == pygame.K_RIGHT:
                print("right")
                ball_x += 15
            if event.key == pygame.K_UP:
                print("up")
                ball_y -= 15
    
    
    ball_rect = pygame.Rect(
        ball_x,
        ball_y,
        BALL_WIDTH_HEIGHT,
        BALL_WIDTH_HEIGHT
    )

    if ball_rect.colliderect(target_rect):
        print("collision!")

    window.fill(BLACK)

    window.blit(
        target,
        (
            TARGET_X,
            TARGET_Y
        )
    )
    window.blit(
        ball_image,
        (
            ball_x,
            ball_y
        )
    )

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)

    