import pygame
import os
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
    