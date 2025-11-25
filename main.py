import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

#adds the caption to the game window
pygame.display.set_caption("Jumpy Jump")

#set background image/colour
#declare global variables
BG_COLOUR = (255,255,255) #RGB for white
WIDTH = 1000
HEIGHT = 800
FPS= 60
PLAYER_VEL = 5 #speed of player movement

window = pygame.display.set_mode((WIDTH, HEIGHT)) #creates the window for the game

def main(window):
    pass
    # main game loop and logic will go here
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS) #controls the frame rate of the game <60
        for event in pygame.event.get(): #set event to quit game
            if event.type == pygame.QUIT: 
                run = False
                break
    
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window) # calls the main function to start the game only when this file is run directly



