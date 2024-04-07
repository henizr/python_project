import pygame
import random
from constants import *

class Ball():
    def __init__(
            self, 
            window: pygame.Surface, 
            windowWidth, 
            windowHeight,
            image: str
            ) -> None:
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
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
        self.xSpeed = random.randrange(5, 50)
        self.ySpeed = random.randrange(5, 50)
    
    def update(self):
        self.x += self.xSpeed
        self.y += self.ySpeed

        if self.x > self.maxWidth or self.x < 0:
            self.xSpeed = -self.xSpeed
        if self.y > self.maxHeight or self.y < 0:
            self.ySpeed = -self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

