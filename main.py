import tkinter as tk
import pygame
from button import Button
import trace
from fileSaver import save_image

# Initialize Tkinter root
root = tk.Tk()
root.withdraw()  # This will hide the root window

# gets user system screen width and height
screenWidth = pygame.display.Info().current_w
screenHeight = pygame.display.Info().current_h

backgroundColor = (169, 169, 169)

# set screen size
screen = pygame.display.set_mode((int(screenWidth / 2), int(screenHeight / 2)))

# window name
pygame.display.set_caption("Sticker Maker")
screen.fill(backgroundColor)

# update screen information
pygame.display.flip()

running = True

# A button to save the image
saveButton = Button(10, 10, 100, 50, (0, 128, 0), "Save", lambda: save_image(screen, root))
tracePoints = []

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

        # Check for button click event
        saveButton.check_click(event)

    if keys[pygame.K_ESCAPE]:
        running = False

    # if the tracing key is pressed run the tracing function
    while tracing:
        tracePoints.append(event.pos)

        if not tracing:
            running = False
            break

    if tracePoints:
        newSticker = tracePoints(screen, tracePoints, )


    saveButton.draw(screen)
    pygame.display.flip()