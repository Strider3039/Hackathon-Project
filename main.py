import turtle
import pygame


background_color = (169, 169, 169)

# set screen size
screen = pygame.display.set_mode((800, 800))

#window name
pygame.display.set_caption("Sticker Maker")
screen.fill(background_color)

# update screen information
pygame.display.flip()

running = True

# window running loop
while running:

    for event in pygame.event.get():

        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False