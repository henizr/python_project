import pygame

class SimpleText:
    'Describes a simple button'
    def __init__(
            self,
            window: pygame.Surface,
            location: tuple,
            value: str,
            text_color: str
    ) -> None:
        pygame.font.init()
        self.window = window
        self.location = location
        self.font = pygame.font.SysFont(None, 30)
        self.text_color = text_color
        self.text: str = None
        self.text_surface: pygame.Surface = None
        self.set_value(value)


    def set_value(self, new_text: str) -> None:
        if self.text == new_text:
            return
        
        self.text = new_text
        self.text_surface = self.font.render(
            self.text,
            True,
            self.text_color
        )
    
    def draw(self) -> None:
        self.window.blit(
            self.text_surface,
            self.location
        )