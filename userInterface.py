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

class StateManager:
    
    def __init__(self, screen):
        self.states = {
            State.MENU_STATE: MenuState(screen),
            State.TRACE_STATE: TraceState(screen),
        }
        self.currentState = self.states[State.MENU_STATE]
    
    def change_state(self, new_state):
        self.currentState = self.states[new_state]
        
    def handle_events(self, event):
        self.currentState.handle_events(event, self)
    
    def update(self):
        self.currentState.update()
    
    def draw(self, screen):
        self.currentState.draw(screen)

class MenuState:
    
    def __init__(self, screen):
        self.screen = screen
        
        self.screenWidth = pygame.display.Info().current_w
        self.screenHeight = pygame.display.Info().current_h
        
        self.newStickerButton = Button((self.screenWidth/2) - (BUTTON_WIDTH / 2), self.screenHeight/4, BUTTON_WIDTH, BUTTON_HEIGHT, BLUE, "Trace Sticker")
        self.galleryButton  = Button((self.screenWidth/2) - (BUTTON_WIDTH / 2), self.newStickerButton.get_pos()[1] + BUTTON_PADDING, BUTTON_WIDTH, BUTTON_HEIGHT, BLUE, "Gallery")
        self.exitButton = Button((self.screenWidth/2) - (BUTTON_WIDTH / 2), self.galleryButton.get_pos()[1] + BUTTON_PADDING, BUTTON_WIDTH, BUTTON_HEIGHT, BLUE, "Exit")
    
    def handle_events(self, event, state_manager):
        if self.newStickerButton.check_click(event): state_manager.change_state(State.TRACE_STATE)
        if self.galleryButton.check_click(event):    gallery.open_gallery()
        if self.exitButton.check_click(event):       exit()
        
        
    def update(self):
        pass

    def draw(self, screen):
        self.screen.fill(BACKGROUND_COLOR)
        self.newStickerButton.draw(screen)
        self.galleryButton.draw(screen)
        self.exitButton.draw(screen)

class TraceState:
    
    def __init__(self, screen):
        self.screen = screen
    
    def update(self):
        pass
    
    def handle_events(self, event, state_manager):
        pass

    def draw(self, screen):
        self.screen.fill(BACKGROUND_COLOR)