# Import modules
import pygame
import sys
from pygame.locals import *
import random
from Ball import Ball
from constants import *
from SimplуButton_04 import SimpleButton
from simpleText import SimpleText


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

simpleButton = SimpleButton(
    window,
    (190, 50),
    BASE_PATH / IMAGES_FOLDER / "play_button.png",
    BASE_PATH / IMAGES_FOLDER / "play_button_pushed.png"
)

simpleText = SimpleText(
    window,
    (180, 212),
    "Score: 12180",
    "white"
)
greeting_txt = SimpleText(
    window,
    (380, 312),
    "Hi",
    "white"
)

entrance_txt = SimpleText(
    window,
    (250, 282),
    "WELLCOME",
    "white"
)

# Main gameloop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pass
        
        if simpleButton.handleEvent(event):
             pass

    if GAME_ACTIVE:
        for ball in ball_list:
            ball.update()

    window.fill(BLACK)

    
    for ball in ball_list:
        ball.draw()

    simpleButton.draw()
    simpleText.draw()
    greeting_txt.draw()
    entrance_txt.draw()




    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)

    