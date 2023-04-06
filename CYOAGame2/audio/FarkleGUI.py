import pygame
from sys import exit


pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Dice Roll Simulator")

background_image = pygame.image.load('graphics/background2.png')
game_font = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
roll_message = game_font.render("press SPACEBAR to start rolling", True, (255, 235, 193))
is_rolling = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #This key will return False or True depending on if the spacebar has or hasn't been pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and is_rolling is False:
        #start rolling
        pass
    else:
        if is_rolling:
            #showing rolling animation
            pass
        else:
            #showing a face of the die
            pass

    screen.blit(background_image, (0,0))
    screen.blit(roll_message, (50, 300))
    pygame.display.update()