# Import modules
import pygame
import sys
from pygame.locals import *
import random
from Ball import Ball
from constants import *


# Initializing the environment
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


# Load assets
target: pygame.Surface = pygame.image.load(BASE_PATH / IMAGES_FOLDER / "plain.png")
bounceSound = pygame.mixer.Sound(BASE_PATH / SOUNDS_FOLDER / "pingPong.wav")
pygame.mixer.music.load(BASE_PATH / SOUNDS_FOLDER / "bgMusic.wav")
pygame.mixer.music.play(-1, 0.0)



# Create a target rect
target_rect = pygame.Rect(
    TARGET_X,
    TARGET_Y,
    TARGET_WIDTH_HEIGHT,
    TARGET_WIDTH_HEIGHT - 158
)

ball_list: list = []

for i in range(5):
    # Creating a ball
    ball = Ball(
        window = window,
        windowWidth = WINDOW_WIDTH,
        windowHeight = WINDOW_HEIGHT,
        image = "ball.png"
    )
    ball_list.append(ball)


# Main gameloop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pass

    for ball in ball_list:
        ball.update()

    window.fill(BLACK)

    
    for ball in ball_list:
        ball.draw()



    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)

    