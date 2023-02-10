import pygame
import os
import dino_class as dino

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#game window
pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dino Survival")

sprite_sheet_image = pygame.image.load("dino.png").convert_alpha()
sprite_sheet = dino.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)


player = pygame.Rect((300, 250, 50, 50))


frame_0 = sprite_sheet.get_image(0, 24, 24, 3, BLACK)
frame_1 = sprite_sheet.get_image(1, 24, 24, 3, BLACK)
frame_2 = sprite_sheet.get_image(2, 24, 24, 3, BLACK)
frame_3 = sprite_sheet.get_image(3, 24, 24, 3, BLACK)
frame_4 = sprite_sheet.get_image(4, 24, 24, 3, BLACK)       

animation_list = []
animation_steps = [4, 6, 3, 4]
action = 3
last_update = pygame.time.get_ticks()
animation_cooldown = 75
frame = 0
step_counter = 0

#animation steps tells how many frames are in each animation
#it will pull the number of times to iterate, and store those frames in the temp list
#since the step counter isn't reset, we keep counting from where we left off
#this stores each different animation as a seperate sublist in the master animation_list

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 24, 24, 3, BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)
    



#game loop
run = True
while run:
#event handler

    screen.fill(BG)
    
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame +=1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    screen.blit(animation_list[action][frame], (0, 0))

    

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                frame = 0
            if event.key == pygame.K_UP and action < len(animation_list) -1:
                action += 1
                frame = 0

    pygame.display.update()


pygame.quit()
