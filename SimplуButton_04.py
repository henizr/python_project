import pygame
from pygame.locals import *

class SimpleButton:
    """describes a simple button"""

    STATE_IDLE = "idle"
    STATE_ARMED = "armed"
    STATE_DISARMED = "disarmed"

    def __init__(
            self,
            window,
            location,
            img_up,
            img_down
    ) -> None:
        self.window = window
        self.location = location
        self.surface_up = pygame.image.load(img_up)
        self.surface_down = pygame.image.load(img_down)

        # Creating a rect
        self.rect = self.surface_up.get_rect()
        # Setting the coordinates
        self.rect[0] = location[0]
        self.rect[1] = location[1]

        # Setting default status
        self.state = SimpleButton.STATE_IDLE

    def handleEvent(self, event_obj: pygame.event.Event):
        # return
        """This method returns True if The user clicks on the button and False othetwise"""

        if event_obj.type not in (
            MOUSEMOTION,
            MOUSEBUTTONUP,
            MOUSEBUTTONDOWN
        ):
            return 
        
        # The collidepoint function returns True if mouse in the rect 
        event_point_in_button_rect = self.rect.collidepoint(1, 1)
        print(event_obj)
        print(2)
        if self.state == SimpleButton.STATE_IDLE:
            if (event_obj.type == MOUSEBUTTONDOWN) and event_point_in_button_rect:
                self.status = SimpleButton.STATE_ARMED

        elif self.status == SimpleButton.STATE_ARMED:
            if (event_obj.type == MOUSEBUTTONUP) and event_point_in_button_rect:
                self.state = SimpleButton.STATE_IDLE
                return True
            
            if (event_obj.type == MOUSEMOTION) and not event_point_in_button_rect:
                self.state == SimpleButton.STATE_ARMED

        elif self.state == SimpleButton.STATE_DISARMED:
            if event_point_in_button_rect:
                self.state = SimpleButton.STATE_ARMED
            elif event_obj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE


        return False

    def draw(self):
        # Draw the buttons current appearance to the window
        if self.state == SimpleButton.STATE_ARMED: 
            self.window.blit(
                self.surface_down,
                self.location
            )
        # idle or disarmed
        else:
            self.window.blit(
                self.surface_up,
                self.location
            )



