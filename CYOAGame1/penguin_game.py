import pygame
import os
import penguin_class as hero

os.chdir(os.path.dirname(os.path.abspath(__file__)))


pygame.init()
screen_width = 800
screen_height = 600
background = pygame.image.load("img/arctic_bg.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))



screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Penguin Adventure")

penguin = pygame.image.load("img/hero-1.png")
penguin = pygame.Surface(penguin.get_size())




run = True
while run:

    screen.blit(background, (0, 0))
    
    screen.blit(penguin, (100, 100))
    

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        penguin.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        penguin.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        penguin.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        penguin.move_ip(0, 1)
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()
