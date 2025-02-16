import pygame

def trace_points(screen, points, filename):
    
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

    #
    sticker_surface.blit(screen, (0, 0), (min_x, min_y, width, height))
