# Import modules
import pygame
import sys
from pygame.locals import *
import random
import pathlib
from Ball import *

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
ball_image: pygame.Surface = pygame.image.load(BASE_PATH / IMAGES_FOLDER / "ball.png")
target: pygame.Surface = pygame.image.load(BASE_PATH / IMAGES_FOLDER / "plain.png")
bounceSound = pygame.mixer.Sound(BASE_PATH / SOUNDS_FOLDER / "pingPong.wav")
pygame.mixer.music.load(BASE_PATH / SOUNDS_FOLDER / "bgMusic.wav")
pygame.mixer.music.play(-1, 0.0)

# Initialize variables
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)
xSpeedBall = 15
ySpeedBall = 15


# Create a target rect
target_rect = pygame.Rect(
    TARGET_X,
    TARGET_Y,
    TARGET_WIDTH_HEIGHT,
    TARGET_WIDTH_HEIGHT - 158
)
ball_rect = ball_image.get_rect()


# Main gameloop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pass

    




    ball_rect.left += xSpeedBall
    ball_rect.top -= ySpeedBall


    window.fill(BLACK)


    # keyPressedTuple = pygame.key.get_pressed()
    # aIsDown = keyPressedTuple[pygame.K_a]
    # dIsDown = keyPressedTuple[pygame.K_d]
    # wIsDown = keyPressedTuple[pygame.K_w]
    # sIsDown = keyPressedTuple[pygame.K_s]

    # if aIsDown:
    #     ball_x -= N_PIXELS_TO_MOVE

    # if dIsDown:
    #     ball_x += N_PIXELS_TO_MOVE

    # if wIsDown:
    #     ball_y -= N_PIXELS_TO_MOVE

    # if sIsDown:
    #     ball_y += N_PIXELS_TO_MOVE
    
    if ball_rect.left < 0 or ball_rect.right >= WINDOW_WIDTH:
        xSpeedBall = -xSpeedBall
        bounceSound.play()

    if ball_rect.bottom >= WINDOW_HEIGHT or ball_rect.top < 0:
        ySpeedBall = -ySpeedBall
        bounceSound.play()


    window.blit(
        ball_image,
        ball_rect
    )

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)

    