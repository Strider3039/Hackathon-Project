import tkinter as tk
import os
import pyautogui
import numpy as np
import cv2
import time


class StickerMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Sticker Maker")
        self.root.geometry("200x200")

        self.btn_new_sticker = tk.Button(self.root, text="New Sticker", command=self.start_snipping)
        self.btn_new_sticker.pack(pady=20)

    def start_snipping(self):
        """Opens the snipping overlay."""
        self.snip_window = tk.Toplevel(self.root)
        self.snip_window.attributes("-fullscreen", True)
        self.snip_window.attributes("-alpha", 0.3)

        self.canvas = tk.Canvas(self.snip_window, cursor="circle", bg="gray")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.points = []
        self.tracing = False
        self.tracing_line = None
        self.polygon = None

        self.snip_window.bind("<Shift_L>", self.start_tracing)
        self.snip_window.bind("<KeyRelease-Shift_L>", self.capture_snip)

    def start_tracing(self, event):
        """Start recording points when Shift is pressed."""
        self.tracing = True
        self.points = []
        self.canvas.delete("all")  # Clear previous traces
        self.canvas.bind("<Motion>", self.draw)

    def draw(self, event):
        """Record points while Shift is held down."""
        if self.tracing:
            self.points.append((event.x, event.y))
            if len(self.points) > 1:
                self.canvas.create_line(self.points[-2], self.points[-1], fill="red", width=2)
            if self.polygon:
                self.canvas.delete(self.polygon)
            self.polygon = self.canvas.create_polygon(self.points, outline="blue", fill="lightblue", stipple="gray50")

    def capture_snip(self, event):
        """Capture and save the snipped image when Shift is released."""
        self.tracing = False
        self.canvas.unbind("<Motion>")
        self.snip_window.withdraw()

        x, y, w, h = 0, 0, self.snip_window.winfo_screenwidth(), self.snip_window.winfo_screenheight()
        img = pyautogui.screenshot(region=(x, y, w, h))
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        mask = np.zeros((h, w), dtype=np.uint8)
        if len(self.points) > 2:
            cv2.fillPoly(mask, [np.array(self.points, dtype=np.int32)], 255)

        result = cv2.bitwise_and(img, img, mask=mask)

        save_path = "Gallery"
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        timestamp = int(time.time())
        file_name = os.path.join(save_path, f"snip_{timestamp}.png")
        cv2.imwrite(file_name, result)

        print(f"image saved to {file_name}")

        cv2.destroyAllWindows()
        self.snip_window.destroy()


# Create and launch the application
root = tk.Tk()
app = StickerMaker(root)
root.mainloop()
