import pygame

class Ball():
    def __init__(
            self, 
            window, 
            windowWidth, 
            windowHeight,
            image: pygame.Surface
            ) -> None:
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.image = image

        # Getting the ball rect
        rect = self.image.get_rect()
