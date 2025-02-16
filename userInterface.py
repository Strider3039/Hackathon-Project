import pygame
from enum import Enum
from button import Button
import gallery

BLUE = (0, 71, 171)
BACKGROUND_COLOR = (169, 169, 169)

BUTTON_WIDTH = 300
BUTTON_HEIGHT = 50
BUTTON_PADDING = 20
    
class State(Enum):
    MENU_STATE = "menuState"
    TRACE_STATE = "traceState"

class Menu:
    
    def __init__(self, screen):
        self.screen = screen
        
        self.screenWidth = pygame.display.Info().current_w
        self.screenHeight = pygame.display.Info().current_h
        
        self.newStickerButton = Button((self.screenWidth/2) - (BUTTON_WIDTH / 2), self.screenHeight/4, BUTTON_WIDTH, BUTTON_HEIGHT, BLUE, "Trace Sticker")
        self.galleryButton  = Button((self.screenWidth/2) - (BUTTON_WIDTH / 2), self.newStickerButton.get_pos()[1] + BUTTON_PADDING, BUTTON_WIDTH, BUTTON_HEIGHT, BLUE, "Gallery")
        self.exitButton = Button((self.screenWidth/2) - (BUTTON_WIDTH / 2), self.galleryButton.get_pos()[1] + BUTTON_PADDING, BUTTON_WIDTH, BUTTON_HEIGHT, BLUE, "Exit")
    
    def handle_events(self, event, state_manager):
        if self.newStickerButton.check_click(event):
            pass
        if self.galleryButton.check_click(event):
            gallery.open_gallery()
        if self.exitButton.check_click(event):
            exit()
        
        
    def update(self):
        pass

    def draw(self, screen):
        self.screen.fill(BACKGROUND_COLOR)
        self.newStickerButton.draw(screen)
        self.galleryButton.draw(screen)
        self.exitButton.draw(screen)
