import os
import pygame

def open_gallery(screen):
    # Set the background color
    backgroundColor = (169, 169, 169)
    screen.fill(backgroundColor)

    # Ensure the gallery folder exists
    gallery_path = 'Gallery'
    if not os.path.exists(gallery_path):
        os.makedirs(gallery_path)

    # Get the list of image files in the gallery folder
    image_files = [f for f in os.listdir(gallery_path) if f.endswith('.jpg') or f.endswith('.png')]

    # Thumbnail size and spacing
    thumbnail_size = (100, 100)
    spacing = 20
    margin = 50

    # Load and display thumbnails
    x, y = margin, margin
    for image_file in image_files:
        image_path = os.path.join(gallery_path, image_file)
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, thumbnail_size)
        screen.blit(image, (x, y))

        # Create a delete button for each thumbnail
        delete_button = pygame.Rect(x + thumbnail_size[0] - 20, y, 20, 20)
        pygame.draw.rect(screen, (255, 0, 0), delete_button)
        font = pygame.font.Font(None, 20)
        text_surface = font.render("x", True, (255, 255, 255))
        screen.blit(text_surface, (x + thumbnail_size[0] - 15, y))

        # Check for delete button click
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if delete_button.collidepoint(event.pos):
                    os.remove(image_path)
                    open_gallery(screen)  # Refresh the gallery
                    return

        x += thumbnail_size[0] + spacing
        if x + thumbnail_size[0] + margin > screen.get_width():
            x = margin
            y += thumbnail_size[1] + spacing

    pygame.display.flip()
