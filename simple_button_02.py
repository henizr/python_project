import pygame
from pygame.locals import *
from collections import namedtuple


class SimpleButton():
    STATE_IDLE = 'idle'
    STATE_ARMED = 'armed'
    STATE_DISARMED = 'disarmed'

    def __init__(
            self,
            window: pygame.Surface,
            location,
            img_up,
            img_down,
    ) -> None:
        self.window = window
        self.location = location
        self.surface_up = pygame.image.load(img_up)
        self.surface_down = pygame.image.load(img_down)
        self.rect = self.surface_up.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

        self.state = SimpleButton.STATE_IDLE


    def handleEvent(self, event_object):
        if event_object.type not in (
            MOUSEMOTION,
            MOUSEBUTTONUP,
            MOUSEBUTTONDOWN
        ):
            return False
        
        event_point_in_button_rect = self.rect.collidepoint(event_object.pos)

        
        print("collide")

        if self.state == SimpleButton.STATE_IDLE:
            if event_object.type == MOUSEBUTTONDOWN and event_point_in_button_rect:
                self.state = SimpleButton.STATE_ARMED

        if self.state == SimpleButton.STATE_ARMED:
            if event_object.type == MOUSEBUTTONUP and event_point_in_button_rect:
                self.state = SimpleButton.STATE_IDLE
                return True
            
        return False

    def draw(self):
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surface_down, self.location)
        else:
            self.window.blit(self.surface_up, self.location)