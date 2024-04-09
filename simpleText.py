import pygame
from pygame.locals import *


class SimpleText:
    def __init__(
            self,
            window,
            location,
            value,
            text_color
    ) -> None:
        pygame.font.init()
        self.window = window
        self.location = location
        self.font = pygame.font.SysFont(None, 30)
        self.text_color = text_color
        self.text = None
        self.text_surface = None
        self.set_value(value)

    def set_value(self, new_text):
        if self.text == new_text:
            return
        
        self.text = new_text
        self.text_surface = self.font.render(
            self.text,
            True,
            self.text_color
        )

    def draw(self):
        self.window.blit(self.text_surface, self.location)