import pygame

FONT_COLOR = (255,255,255)

font = pygame.font.Font(None, 40)

class Button:
    
    def __init__(self, x, y, width, height, button_color, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.buttonColor = button_color
        self.hoverButtonColor = button_color + (50, 50, 50)
        self.text = text
        self.action = action

    def draw(self, screen):
        
        mouse_pos = pygame.mouse.get_pos()
        
        # Change color on mouse hover
        current_color = self.hoverButtonColor if self.rect.collidepoint(mouse_pos) else self.buttonColor
        
        # draw button 
        pygame.draw.rect(screen, current_color, self.rect, border_radius=10)
        text_surface = font.render(self.text, True, FONT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and self.action:
                self.action()
