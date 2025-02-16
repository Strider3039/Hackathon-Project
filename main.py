import tkinter as tk
import os
import pyautogui
import numpy as np
import cv2
import time


class FreeformSnip:
    def __init__(self, root):
        self.root = root
        self.root.title("Freeform Snipping Tool")
        self.root.geometry("300x200")

        self.btn_new_sticker = tk.Button(self.root, text="New Sticker", command=self.start_snipping)
        self.btn_new_sticker.pack(pady=20)

    def start_snipping(self):
        """Opens the snipping overlay."""
        # Hide the main window when starting the snipping
        self.root.withdraw()

        # Create snip window and make it the size of the screen (no fullscreen)
        self.snip_window = tk.Toplevel(self.root)
        self.snip_window.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}")
        self.snip_window.attributes("-alpha", 0.3)

        self.canvas = tk.Canvas(self.snip_window, cursor="cross", bg="gray")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.points = []
        self.tracing = False
        self.tracing_line = None
        self.polygon = None

        # Bind left mouse button to start tracing
        self.snip_window.bind("<Button-1>", self.start_tracing)
        # Bind left mouse button release to capture snip
        self.snip_window.bind("<ButtonRelease-1>", self.capture_snip)

    def start_tracing(self, event):
        """Start recording points when left click is pressed."""
        if not self.tracing:  # Only start tracing if it's not already tracing
            self.tracing = True
            self.points = []
            self.canvas.delete("all")  # Clear previous traces
            self.canvas.bind("<Motion>", self.draw)  # Bind mouse motion to drawing

    def draw(self, event):
        """Record points while mouse is moving and left click is held down."""
        if self.tracing:
            self.points.append((event.x, event.y))
            if len(self.points) > 1:
                self.canvas.create_line(self.points[-2], self.points[-1], fill="red", width=2)
            if self.polygon:
                self.canvas.delete(self.polygon)
            self.polygon = self.canvas.create_polygon(self.points, outline="blue", fill="lightblue", stipple="gray50")

    def capture_snip(self, event):
        """Capture and save the snipped image when left click is released."""
        self.tracing = False
        self.canvas.unbind("<Motion>")  # Unbind mouse motion (stop drawing)
        self.snip_window.withdraw()  # Hide the snipping window

        # Get the snip region coordinates
        x, y, w, h = 0, 0, self.snip_window.winfo_screenwidth(), self.snip_window.winfo_screenheight()

        # Take screenshot of the region
        img = pyautogui.screenshot(region=(x, y, w, h))
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Create mask
        mask = np.zeros((h, w), dtype=np.uint8)
        if len(self.points) > 2:
            points_array = np.array(self.points, dtype=np.int32)
            cv2.fillPoly(mask, [points_array], 255)  # Fill the polygon region

        # Apply the mask to the image
        result = cv2.bitwise_and(img, img, mask=mask)

        # Save the result to the "Gallery" folder
        save_path = "Gallery"
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        timestamp = int(time.time())
        file_name = os.path.join(save_path, f"snip_{timestamp}.png")
        cv2.imwrite(file_name, result)

        print(f"Snip saved to {file_name}")

        cv2.destroyAllWindows()

        # Show the main window after snipping is done
        self.root.deiconify()

        self.snip_window.destroy()


# Create and launch the application
root = tk.Tk()
app = FreeformSnip(root)
root.mainloop()
