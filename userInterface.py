import pygame
from enum import Enum
from button import Button

BLUE = (0, 71, 171)
BACKGROUND_COLOR = (169, 169, 169)

class State(Enum):
    MENU_STATE = "menuState"
    TRACE_STATE = "traceState"
    GALLERY_STATE = "galleryState"

class StateManager:
    
    def __init__(self, screen):
        self.states = {
            State.MENU_STATE: MenuState(screen),
            State.TRACE_STATE: TraceState(screen),
            State.GALLERY_STATE: GalleryState(screen)
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
        
        self.newStickerButton = Button(self.screenWidth/2, self.screenHeight/4, 100, 50, BLUE, "Trace Sticker")
        self.galleryButton  = Button(self.screenWidth/2, self.screenHeight/2, 100, 50, BLUE, "Gallery")
        self.exitButton = Button(self.screenWidth/2, self.screenHeight, 100, 50, BLUE, "Exit")
    
    def handle_events(self, event, state_manager):
        if self.newStickerButton.check_click(event): state_manager.change_state(State.TRACE_STATE)
        if self.galleryButton.check_click(event):    state_manager.change_state(State.GALLERY_STATE)
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
        

class GalleryState:
    
    def __init__(self, screen):
        self.screen = screen
        
        self.screenWidth = pygame.display.Info().current_w
        self.screenHeight = pygame.display.Info().current_h
        
        self.mainMenuButton = Button(self.screenWidth/2, self.screenHeight/4, 100, 50, BLUE, "Main Menu")

    def update(self):
        pass
    
    def handle_events(self, event, state_manager):
        if self.mainMenuButton.check_click(event) : state_manager.change_state(State.MENU_STATE)

    def draw(self, screen):
        self.screen.fill(BACKGROUND_COLOR)
        self.mainMenuButton.draw(screen)
