import pygame

class SpriteSheet():
    def __init__(self, image, x, y):
        self.sheet = image
        self.width = 24
        self.height = 24
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x,y)  

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame*width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)   
        return image

    

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 10
        elif key[pygame.K_RIGHT]:
            self.rect.x += 10
        elif key[pygame.K_UP]:
            pass

        
