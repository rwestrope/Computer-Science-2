import pygame
from pygame.locals import *
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

screen_width = 1152
screen_height = 648

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Texas Hold 'Em")

bg = pygame.image.load('img/poker_bg.jpg')

card_values = {
    '2_of_clubs': pygame.image.load('img/2_of_clubs.png'),
    '2_of_diamonds': pygame.image.load('img/2_of_diamonds.png'),
    '2_of_hearts': pygame.image.load('img/2_of_hearts.png'),
    '2_of_spades': pygame.image.load('img/2_of_spades.png'),
    '3_of_clubs': pygame.image.load('img/3_of_clubs.png'),
    '3_of_diamonds': pygame.image.load('img/3_of_diamonds.png'),
    '3_of_hearts': pygame.image.load('img/3_of_hearts.png'),
    '3_of_spades': pygame.image.load('img/3_of_spades.png'),
    '4_of_clubs': pygame.image.load('img/4_of_clubs.png'),
    '4_of_diamonds': pygame.image.load('img/4_of_diamonds.png'),
    '4_of_hearts': pygame.image.load('img/4_of_hearts.png'),
    '4_of_spades': pygame.image.load('img/4_of_spades.png'),
    '5_of_clubs': pygame.image.load('img/5_of_clubs.png'),
    '5_of_diamonds': pygame.image.load('img/5_of_diamonds.png'),
    '5_of_hearts': pygame.image.load('img/5_of_hearts.png'),
    '5_of_spades': pygame.image.load('img/5_of_spades.png'),
    '6_of_clubs': pygame.image.load('img/6_of_clubs.png'),
    '6_of_diamonds': pygame.image.load('img/6_of_diamonds.png'),
    '6_of_hearts': pygame.image.load('img/6_of_hearts.png'),
    '6_of_spades': pygame.image.load('img/6_of_spades.png'),
    '7_of_clubs': pygame.image.load('img/7_of_clubs.png'),
    '7_of_diamonds': pygame.image.load('img/7_of_diamonds.png'),
    '7_of_hearts': pygame.image.load('img/7_of_hearts.png'),
    '7_of_spades': pygame.image.load('img/7_of_spades.png'),
    '8_of_clubs': pygame.image.load('img/8_of_clubs.png'),
    '8_of_diamonds': pygame.image.load('img/8_of_diamonds.png'),
    '8_of_hearts': pygame.image.load('img/8_of_hearts.png'),
    '8_of_spades': pygame.image.load('img/8_of_spades.png'),
    '9_of_clubs': pygame.image.load('img/9_of_clubs.png'),
    '9_of_diamonds': pygame.image.load('img/9_of_diamonds.png'),
    '9_of_hearts': pygame.image.load('img/9_of_hearts.png'),
    '9_of_spades': pygame.image.load('img/9_of_spades.png'),
    '10_of_clubs': pygame.image.load('img/10_of_clubs.png'),
    '10_of_diamonds': pygame.image.load('img/10_of_diamonds.png'),
    '10_of_hearts': pygame.image.load('img/10_of_hearts.png'),
    '10_of_spades': pygame.image.load('img/10_of_spades.png'),
    'ace_of_clubs': pygame.image.load('img/ace_of_clubs.png'),
    'ace_of_diamonds': pygame.image.load('img/ace_of_diamonds.png'),
    'ace_of_hearts': pygame.image.load('img/ace_of_hearts.png'),
    'ace_of_spades': pygame.image.load('img/ace_of_spades.png'),
    'jack_of_clubs': pygame.image.load('img/jack_of_clubs.png'),
    'jack_of_diamonds': pygame.image.load('img/jack_of_diamonds.png'),
    'jack_of_hearts': pygame.image.load('img/jack_of_hearts.png'),
    'jack_of_spades': pygame.image.load('img/jack_of_spades.png'),
    'king_of_clubs': pygame.image.load('img/king_of_clubs.png'),
    'king_of_diamonds': pygame.image.load('img/king_of_diamonds.png'),
    'king_of_hearts': pygame.image.load('img/king_of_hearts.png'),
    'king_of_spades': pygame.image.load('img/king_of_spades.png'),
    'queen_of_clubs': pygame.image.load('img/queen_of_clubs.png'),
    'queen_of_diamonds': pygame.image.load('img/queen_of_diamonds.png'),
    'queen_of_hearts': pygame.image.load('img/queen_of_hearts.png'),
    'queen_of_spades': pygame.image.load('img/queen_of_spades.png'),
    'black_joker': pygame.image.load('img/black_joker.png'),
    'red_joker': pygame.image.load('img/red_joker.png'),
    'back': pygame.image.load('img/back.png')
}




class Card(pygame.sprite.Sprite):
    def __init__(self, suit, value, front, back):
        print('card')



if __name__ == '__main__':

    run = True
    while run:

        screen.blit(bg, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

pygame.quit()