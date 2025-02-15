import tkinter as tk
import pygame
from button import Button
import trace


# gets the root to the tkinter library
root = tk.Tk()

# gets user system screen width and height
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

backgroundColor = (169, 169, 169)

# set screen size
screen = pygame.display.set_mode((screenWidth / 2, screenHeight / 2))

#window name
pygame.display.set_caption("Sticker Maker")
screen.fill(backgroundColor)

# update screen information
pygame.display.flip()

running = True

# window running loop
while running:

    # a list of true or false bools based on if the key provided is pressed or not
    # updated ever iteration
    keys = pygame.key.get_pressed()
    tracing = keys[pygame.K_LSHIFT]

    for event in pygame.event.get():
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
        
    if keys[pygame.K_ESCAPE]:
        running = False

    # if the tracing key is pressed run the tracing function
    if tracing:
        pass