import pygame
import os
from tkinter import filedialog
    
# returns a selected image
def load_image(root)-> pygame.image:
    # open file dialog to choose the image
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;")])

    if file_path: 
            # load the image
            image = pygame.image.load(file_path)
                        
            #create folder if it doesnt exist already
            if not os.path.exists("gallery"):
                os.makedirs("gallery")
            
            # get the file name i.e. "someImage.png"
            base_name = os.path.basename(file_path)
            
            # add file to path 
            save_path = os.path.join('gallery', base_name)
            
            # save the image
            pygame.image.save(image, save_path)
    else:
        print("Error laoding file")
        return None