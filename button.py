import pygame

pygame.init()

FONT_COLOR = (255, 255, 255)

# Ensure the font is initialized properly before using it
font = pygame.font.Font(None, 40)

class Button:
    
    def __init__(self, x, y, width, height, button_color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.buttonColor = button_color
        
        # Modify hover color by adding a small amount to each color component
        self.hoverButtonColor = tuple(min(255, c + 50) for c in button_color)  # Correct hover color calculation
        
        self.text = text

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        # Change color on mouse hover
        current_color = self.hoverButtonColor if self.rect.collidepoint(mouse_pos) else self.buttonColor

        # Draw button 
        pygame.draw.rect(screen, current_color, self.rect, border_radius=10)
        text_surface = font.render(self.text, True, FONT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

    # returns bottom left point
    def get_pos(self):
        return self.rect.bottomleft