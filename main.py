import random # for generating of the random  numbers
import sys    # for the exit the programme
import pygame # for the pygame module
from pygame.locals import * # Pygame special Variables


# Declearing the Global Variables used inthe ga,e 

FPS = 32 # The Fps of the game for the image rendering 
SCREENWIDTH = 289 # set the width of the game screen 
SCREENHIGHT = 511 # set the hight of the game screen 
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHIGHT)) # setting a basic screen in the pygame 
GROUNDY = SCREENHIGHT * 0.8 # set the ground image according to the screen hight 
GAME_IMAGES = {} # All the game images in the Gallary folder 
GAME_SOUNDS = {} # All the Audio of the game in the gallary folder 
PLAYER = 'Gallary/images/bird.png' # Relative path of the player 
BACKGROUND = 'Gallary/images/background.png' # Relative path of the background 
PIPE = 'Gallary/images/bamboo.png' # Relativa path of the pipe image 

# Defining the functions

# This is the function for dispalying the welcome screen 
def welcomescreen():
    """
    This is the Welcome screen shows to the User untill he/she press a button.
    """
    playerx = int(SCREENWIDTH / 5) # x cordinate of the player
    playery = int((SCREENHIGHT - GAME_IMAGES['player'].get_height()) / 2) # y cordinate of the bird, and to center the image. 
    messagex = int((SCREENWIDTH - GAME_IMAGES['message'].get_width()) / 2) # show the message position at the x cordinate
    messagey = int(SCREENHIGHT * 0.13)
    basex = 0
    while True:
        # This will tell the user about their input they performed with the mouse or keyboard.
        for event in pygame.event.get():
            # if the user input the cross or ese key the game will stop.
            # for more about keys google pygame keys

            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # if the user enter  space or the arrow key, start the game for them

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP ):
                return
            else:
                # it will shows the Game welcome screen untill the defined keys are pressed 
                # Bliting means setting the Images according to the screen hight and weidth with the help of X and Y Cordinates 
                SCREEN.blit(GAME_IMAGES['background'], (0, 0))
                SCREEN.blit(GAME_IMAGES['player'], (playerx, playery))
                SCREEN.blit(GAME_IMAGES['message'], (messagex, messagey))
                SCREEN.blit(GAME_IMAGES['base'], (basex, GROUNDY))
                pygame.display.update() # This function will shows the actual bliting in the pygame, with the help of the function mentioned above 
                FPSCLOCK.tick(FPS) # This is the Fps controller of the screen FPS == Golbal variable we maintioned

# This is the function for generating the random pipes on the screen 
def GetRandomPipe():
    # generating the postion of the pipes on the screen (straight and 180 degree rotated )
    # Returns a dictionary with the random cordiantes of the pipes both straight and rotated 
    
    pipeHight = GAME_IMAGES['pipe'][0].get_hight() # getting the hight of the pipe image
    offSet = SCREENHIGHT/3 
    # Off set is a gap between the pipes by which the bird can flap 
    y2 = offSet + random.randrange(0, int(SCREENHIGHT - GAME_IMAGES['base'].get_hight() - (1.2 * offSet)))
    pipex = SCREENWIDTH + 10
    y1 = pipeHight - y2 + offSet
    # This is the list for the pipe cordinates generating by the pygame.
    pipe = [
        {'x': pipex, 'y': -y1 }, # This is for the upper pipe so the value of the Y cordinate is Negetive.
        {'x': pipex, 'y': y2 } # This is for the lower pipe
    ]
    # Returing the dictionary of the function A
    return pipe
    


# This is the function for the main game loop after pressing the arrow or space key

def maingame():
    score = 0 # Inicilize the score of the game 
    playerx = int(SCREENWIDTH/5) # setting the palyer position on the Game Screen 
    playery = int(SCREENWIDTH/2) # Settindg the Y position of the screen 
    basex = 0

    # Creat the random pipes for the bliting  on the screen both straight and 180 digree pipes 
    newPipe1 = GetRandomPipe()
    newPipe2 = GetRandomPipe()

    # This is the list of the upper pipes 
    upperpipes = [
        {'x':SCREENWIDTH+200, 'y': newPipe1[0]['y']},
        {'x':SCREENWIDTH+200+(SCREENWIDTH/2), 'y': newPipe2[1]['y']}
    ]

    # this is the list for teh lower pipe
    lowerpipes = [
        {'x':SCREENWIDTH+200, 'y': newPipe1[0]['y']},
        {'x':SCREENWIDTH+200+(SCREENWIDTH/2), 'y': newPipe2[1]['y']}
    ]

    # now this is the time to generate the velosity of the pipes and the palyer of the Game 
    pipeVelX = -4
    
    palyerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1
    
    
    playerFlappedAccv = -8 # Velosity while Flapping 
    playerFlapped = False  # It is true while the bird is Flapping 
    
    
    while True:
        
    
    
    




if __name__ == '__main__':
    # This is the main body of the function
    pygame.init() # initializing the pygame function.
    FPSCLOCK = pygame.time.Clock() # for controlling the frames of the Game 
    pygame.display.set_caption('Flappy Bird By Shubhajit') # initializing the name of the Game 
    #set the dictionary for the game images, keys are the name and values are the relative path of that image.
    GAME_IMAGES['numbers'] = (
        pygame.image.load('Gallary/images/0.png').convert_alpha(),
        pygame.image.load('Gallary/images/1.png').convert_alpha(),
        pygame.image.load('Gallary/images/2.png').convert_alpha(),
        pygame.image.load('Gallary/images/3.png').convert_alpha(),
        pygame.image.load('Gallary/images/4.png').convert_alpha(),
        pygame.image.load('Gallary/images/5.png').convert_alpha(),
        pygame.image.load('Gallary/images/6.png').convert_alpha(),
        pygame.image.load('Gallary/images/7.png').convert_alpha(),
        pygame.image.load('Gallary/images/8.png').convert_alpha(),
        pygame.image.load('Gallary/images/9.png').convert_alpha(),
    )

    GAME_IMAGES['message'] = pygame.image.load('Gallary/images/welcome.png').convert_alpha()
    GAME_IMAGES['base'] = pygame.image.load('Gallary/images/ground.png').convert_alpha()
    GAME_IMAGES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180), # for the 180 rotation of pipe
        pygame.image.load(PIPE).convert_alpha()
        )
    GAME_IMAGES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_IMAGES['player'] = pygame.image.load(PLAYER).convert_alpha()

    #set the Dictionary for the game sounds.
    # GAME_SOUNDS[] which i have to  downlode.




    # Starting the Game Loop of the program

    while True:
        welcomescreen() #Shows the welcome screen until the user press a button 
        maingame() # This is the main function for running of the Game




