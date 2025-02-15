import tkinter as tk
import pygame

# gets the root to the tkinter library
root = tk.Tk()

# gets user system screen width and height
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

background_color = (169, 169, 169)

# set screen size
screen = pygame.display.set_mode((screenWidth / 2, screenHeight / 2))

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
        # key press processor
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Directly check the key event
                running = False
