import random # for generating of the random  numbers
import sys    # for the exit the programme
import pygame # for the pygame module
from pygame.locals import * # pygame special variabls


# Declearing the Global Variabls

FPS = 32
SCREENWIDTH = 289
SCREENHIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHIGHT))
GROUNDY = SCREENHIGHT * 0.8
GAME_IMAGES = {}
GAME_SOUNDS = {}
PLAYER = 'Gallary/images/bird.png'
BACKGROUND = 'Gallary/images/background.png'
PIPE = 'Gallary/images/bamboo.png'









if __name__ == '__main__':
    # This is the main body of the function
    pygame.init() #inicilize the pygame function.
    FPSCLOCK = pygame.time.clock()
