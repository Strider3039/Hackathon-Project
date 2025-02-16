import pygame
import os
import math
from tkinter import simpledialog

def save_image(image, root):
    # Create a gallery folder in case it doesn't exist
    if not os.path.exists("gallery"):
        os.makedirs("gallery")
    
    # Ask the user for the file name
    fileName = simpledialog.askstring("Save Image", "Enter the file name:", parent=root)
    if fileName:
        filePath = os.path.join('gallery', f"{fileName}.png")
        pygame.image.save(image, filePath)

def distance_calc(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
    

def trace_png(screen, points):
    
    if not points: return

    # make sure the trace is large enough
    if len(points) < 3:
        return None 

    # **find and create the bounding box** 
    # get the x and y coordinates from points
    x_coords, y_coords = zip(*points)
    # find the max and min boundaries for the box
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    width, height = max_x - min_x, max_y - min_y

    # creates an image canvas the size of the bounding box
    # SRCALPHA makes the image transparent upon creation
    sticker_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # copy the pixels on screen within the bounding box
    sticker_surface.blit(screen, (0, 0), (min_x, min_y, width, height))
    # create an empty mask to capture the shape using pygames polygon object
    mask_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    # create a polygon object with parameters surface, color, and points
    # make a list of local coordinates, done by recording the difference between the current and min values of each x and y
    # mean x_min, y_min would now be (0,0) the origin
    pygame.draw.polygon(mask_surface, (255,255,255,255), [(x - min_x, y - min_y) for x, y in points])

    # apply the mask to the original surface to get only the traced shape
    sticker_surface.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)


    

    # Save the traced image to the gallery folder
    save_image(sticker_surface)