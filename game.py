import pygame
from pygame.locals import *
import sys
from pathlib import Path
import random

BASE_PATH = str(Path(__file__).resolve().parent)
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 400
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# ball image
ballImage = pygame.image.load(BASE_PATH + r"\img\ball.png")

ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(
    ballX,
    ballY,
    BALL_WIDTH_HEIGHT,
    BALL_WIDTH_HEIGHT
)

while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(
                    ballX,
                    ballY,
                    BALL_WIDTH_HEIGHT,
                    BALL_WIDTH_HEIGHT
                )

    # filling color
    window.fill(BLACK)

    # creating an image
    window.blit(ballImage, (ballX, ballY))

    # updating game
    pygame.display.update()
    # setting chastota
    clock.tick(FRAMES_PER_SECOND)