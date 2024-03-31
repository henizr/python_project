import pygame
import random
from constants import *

class Ball():
    def __init__(
            self,
            window: pygame.Surface,
            windowWidth: int,
            windowHeight: int,
            image: str)->None:
        
        self.window = window
        self.windowWidth = windowWidth
        self.windowWidth = windowWidth
        self.image = pygame.image.load(BASE_PATH / IMAGES_FOLDER / image)

        # Getting the ball rect
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        # Picking a random start point
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        # Choosing a random speed
        self.xSpeed = 5
        self.ySpeed = 4

    def update(self):
        pass

    def draw(self):
        pass
    