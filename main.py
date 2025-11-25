import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

#adds the caption to the game window
pygame.display.set_caption("Jumpy Jump")


#declare global variables
WIDTH = 1000
HEIGHT = 800
FPS= 60
PLAYER_VEL = 5 #speed of player movement

window = pygame.display.set_mode((WIDTH, HEIGHT)) #creates the window for the game


def get_background(name): #name = colour of the background
    #run the code from the directory of the file to get the background image
    image = pygame.image.load(join("platformgame_assets","Backgrounds" ,name))
    _,_,width,height = image.get_rect()
    tiles = []
    for i in range (WIDTH // width +1):
        for j in range (HEIGHT // height +1):
            pos = (i*width, j*height) #position of the top left corner of each tile -- tuple
            tiles.append(pos)
    
    return tiles, image
            
def draw(window, background,bg_image):
    for tile in background:
        window.blit(bg_image, tile) #draws the background image at each tile position
    
    pygame.display.update() #update the display to show the drawn background
    

def main(window):
    pass
    # main game loop and logic will go here
    clock = pygame.time.Clock()
    background, bg_image = get_background("background_clouds.svg")

    run = True
    while run:
        clock.tick(FPS) #controls the frame rate of the game <60
        for event in pygame.event.get(): #set event to quit game
            if event.type == pygame.QUIT: 
                run = False
                break
        
        draw(window, background, bg_image)
    
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window) # calls the main function to start the game only when this file is run directly



