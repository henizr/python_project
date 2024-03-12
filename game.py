import pygame
from pygame.locals import *
import sys
from pathlib import Path

BASE_PATH = str(Path(__file__).resolve().parent)
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# ball image
ballImage = pygame.image.load(BASE_PATH + r"\img\ball.png")

while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # filling color
    window.fill(BLACK)

    # creating an image
    window.blit(ballImage, (100, 250))

    # updating game
    pygame.display.update()
    # setting chastota
    clock.tick(FRAMES_PER_SECOND)