import random   
import sys 
import pygame
from pygame.locals import *

#Global VAr for the game 
window_width = 600
window_height = 499

#set geight and width of window 
window = pygame.display.set_mode((window_width,window_height))
elivation = window_height = 0.8
game_images = {}
framepersecond = 32

##FGET NEW IMAGES ONLINE FOR THIS PORTION 
pipeimage = 'images/pipe.png'
background_image = 'images/background.jpg'
player_image = 'images/player_image'
sealevel_image = 'images/base.jfif'
#########################################

##PRogram Starts
if __name__== "__main__":

    #Initalize modulas of pygame
    pygame.init()
    framepersecond_clock = pygame.time.Clock()

    #SET the titale on top of game window
    pygame.display.set_caption('CPSC-254-03 Game')

    #load al the images which we need in the game
    game_images['scoreimages'] = {
        pygame.image.load('images/0.png').convert_alpha(),
        pygame.image.load('images/1.png').convert_alpha(),
        pygame.image.load('images/2.png').convert_alpha(),
        pygame.image.load('images/3.png').convert_alpha(),
        pygame.image.load('images/4.png').convert_alpha(),        
        pygame.image.load('images/5.png').convert_alpha(),
        pygame.image.load('images/6.png').convert_alpha(),
        pygame.image.load('images/7.png').convert_alpha(),
        pygame.image.load('images/8.png').convert_alpha(),
        pygame.image.load('images/9.png').convert_alpha()            
    }
    ##include the images of the pipe, backgroundm player, and sealevel
    game_images['flappybird'] = pygame.image.load(birdplayer_image).convert_alpha()                  
    game_images['sea_level'] = pygame.image.load(sealevel_image).convert_alpha()
    game_images['background'] = pygame.image.load(background_image).convert_alpha()
    game_images['pipeimage'] = (pygame.transform.rotate(pygame.image.load(pipeimage)
                                                        .convert_alpha(),
                                                        180),
                                pygame.image.load(pipeimage).convert_alpha())

    print("welcome to our Project Game")
    print("Press space or enter to start the game")

    