import pygame
from button import Button

# Initialize Pygame
pygame.init()

# Get screen width and height from Pygame
screenWidth = pygame.display.Info().current_w
screenHeight = pygame.display.Info().current_h

background_color = (169, 169, 169)

# Set the screen size (convert to integers)
screen = pygame.display.set_mode((int(screenWidth / 2), int(screenHeight / 2)))

# Window name
pygame.display.set_caption("Sticker Maker")
screen.fill(background_color)

# Update screen information
pygame.display.flip()

def start_game():
    print("Start Game clicked!")

# Button setup
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
DARK_BLUE = (0, 50, 200)
startButton = Button(200, 150, 200, 50, BLUE, "Start Game", start_game)

running = True

# Window running loop
while running:

    for event in pygame.event.get():

        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
        # Key press processor
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Directly check the key event
                running = False

        # Check if the button is clicked
        startButton.check_click(event)

    # Draw the button
    startButton.draw(screen)

    # Update the display
    pygame.display.flip()

pygame.quit()
