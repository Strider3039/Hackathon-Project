import tkinter as tk
import os
import pyautogui
import numpy as np
import cv2

def test():
    root = tk.Tk()
    app = StickerMaker(root)
    root.mainloop()
    
class StickerMaker:
    def __init__(self, root):
        # initialize the tkinter window root, title, and size
        self.root = root
        self.start_snipping()

    def start_snipping(self):
        self.root.withdraw()

        # open snipping top level window overlay
        self.snip_window = tk.Toplevel(self.root)
        # set window to fullscreen and 30% opacity
        self.snip_window.attributes("-fullscreen", True)
        self.snip_window.attributes("-alpha", 0.3)

        # create a canvas widget to trace on and change the cursor to a circle
        self.canvas = tk.Canvas(self.snip_window, cursor="circle", bg="gray")
        # make sure the canvas fills the entire window
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # initialize variables for tracing
        self.points = []
        self.tracing = False
        self.tracing_line = None
        self.polygon = None

        # bind mouse actions to the canvas functions
        self.snip_window.bind("<Button-1>", self.start_tracing)
        self.snip_window.bind("<ButtonRelease-1>", self.capture_snip)

        # exit out of the program if the Escape key is pressed
        self.snip_window.bind("<Escape>", lambda event: exit())


    def start_tracing(self, event):
        # start tracing when the left mouse button is pressed, called above
        # delete all canvas and point info first
        self.tracing = True
        self.points = []
        self.canvas.delete("all")  # Clear previous traces
        # draw a line from the current mouse position to the next
        self.canvas.bind("<Motion>", self.draw)

    def draw(self, event):
        
        # draw a line from the current mouse position to the next
        if self.tracing:
            self.points.append((event.x, event.y))
            # if there are more than 2 points, draw a red line between the last two points
            if len(self.points) > 1:
                self.canvas.create_line(self.points[-2], self.points[-1], fill="red", width=2)
            # if a polygon exists, delete it and create a new one with the updated points
            if self.polygon:
                self.canvas.delete(self.polygon)
            self.polygon = self.canvas.create_polygon(self.points, outline="blue", fill="lightblue", stipple="gray50")

    def capture_snip(self, event):
        # when done tracing, unbind the mouse motion on the canvas,
        # capture the snip and save it to a file
        self.tracing = False
        self.canvas.unbind("<Motion>")
        self.snip_window.withdraw()

        # get the full dimensions of the screen
        x, y, w, h = 0, 0, self.snip_window.winfo_screenwidth(), self.snip_window.winfo_screenheight()
        # take a screenshot of the screen using pyautogui
        img = pyautogui.screenshot(region=(x, y, w, h))
        # convert the screenshot to a numpy array and then to a cv2 image
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # create a mask of the polygon drawn on the canvas
        mask = np.zeros((h, w), dtype=np.uint8)
        # if there are more than 2 points, fill the polygon with white
        if len(self.points) > 2:
            cv2.fillPoly(mask, [np.array(self.points, dtype=np.int32)], 255)

         # Create a transparent image
        b, g, r = cv2.split(img)
        alpha = mask  # Use mask as alpha channel
        transparent_img = cv2.merge([b, g, r, alpha])

        # if the Gallery folder doesn't exist, create it
        save_path = "Gallery"
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # save the snip to a file with a timestamp
        self.ask_filename(transparent_img, save_path)

    def ask_filename(self, image, save_path):
        # create a new top level window to ask for a filename
        filename_window = tk.Toplevel(self.root)
        filename_window.title("Save Sticker")
        filename_window.geometry("400x150")

        # create a label and entry widget for the filename
        tk.Label(filename_window, text="Type file name and press enter or create:").pack(pady=5)
        filename_entry = tk.Entry(filename_window)
        filename_entry.pack(pady=5)

        # create a button to save the image
        def save_image():
            file_name = filename_entry.get()
            # if the filename is not empty, save the image to the Gallery folder
            if file_name:
                # Find the bounding box of the non-transparent pixels
                b, g, r, alpha = cv2.split(image)
                coords = cv2.findNonZero(alpha)
                x, y, w, h = cv2.boundingRect(coords)

                # Crop the image to the bounding box
                cropped_image = image[y:y+h, x:x+w]

                full_path = os.path.join(save_path, f"{file_name}.png")
                cv2.imwrite(full_path, cropped_image)
                filename_window.destroy()
                self.snip_window.destroy()
                self.root.quit()

        # bind the Enter key to the save_image function
        filename_entry.bind("<Return>", lambda event: save_image())
        tk.Button(filename_window, text="Create", command=save_image).pack(pady=5)

test()
