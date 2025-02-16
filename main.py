import tkinter as tk
import os
import pyautogui
import numpy as np
import cv2
import time

# test 1

class StickerMaker:
    def __init__(self, root):
        # initialize the tkinter window root, title, and size
        self.root = root
        self.root.title("Sticker Maker")
        self.root.geometry("200x200")

        # create a new tk button widget that runs the start_snipping function when pressed
        self.btn_new_sticker = tk.Button(self.root, text="New Sticker", command=self.start_snipping)
        # add a 20 pixel margin between the button and top of window
        self.btn_new_sticker.pack(pady=20)

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

        # apply the mask to the image to get the snip
        result = cv2.bitwise_and(img, img, mask=mask)

        # if the Gallery folder doesn't exist, create it
        save_path = "Gallery"
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # save the snip to a file with a timestamp
        timestamp = int(time.time())
        file_name = os.path.join(save_path, f"snip_{timestamp}.png")
        cv2.imwrite(file_name, result)

        print(f"image saved to {file_name}")

        # destroy cv2 windows and the snip window
        cv2.destroyAllWindows()
        self.snip_window.destroy()

        self.root.deiconify()


# Create and launch the application
# mainloop() is an infinite loop used to run the application, 
# wait for an event to occur and process the event till the window is not closed.
root = tk.Tk()
app = StickerMaker(root)
root.mainloop()
