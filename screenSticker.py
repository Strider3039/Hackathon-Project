import tkinter as tk
import os
from PIL import Image, ImageTk

class DraggableSticker:
    """Creates a draggable sticker on the screen."""

    def __init__(self, sticker_path, position=(100, 100)):
        self.sticker_path = sticker_path

        # Create a transparent window
        self.root = tk.Toplevel()
        self.root.overrideredirect(True)  # Remove window borders
        self.root.attributes("-topmost", True)  # Keep above other windows
        self.root.attributes("-transparentcolor", "gray")  # Make gray color transparent

        # Load the sticker image
        self.image = Image.open(self.sticker_path).convert("RGBA")
        self.tk_image = ImageTk.PhotoImage(self.image)

        # Create a label to hold the sticker
        self.label = tk.Label(self.root, image=self.tk_image, bg="gray")
        self.label.pack()

        # Set window size to match sticker
        self.root.geometry(f"{self.image.width}x{self.image.height}+{position[0]}+{position[1]}")

        # Enable dragging
        self.label.bind("<ButtonPress-1>", self.start_move)
        self.label.bind("<B1-Motion>", self.on_move)

    def start_move(self, event):
        """Capture the initial position when dragging starts."""
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        """Move the sticker window based on mouse movement."""
        dx = event.x - self.x
        dy = event.y - self.y
        x = self.root.winfo_x() + dx
        y = self.root.winfo_y() + dy
        self.root.geometry(f"+{x}+{y}")

class StickerGallery:
    """A window to select and paste stickers onto the screen."""

    def __init__(self, root, gallery_path="Gallery"):
        self.root = root
        self.gallery_path = gallery_path

        # Immediately open the sticker gallery
        self.gallery_window = tk.Toplevel(root)
        self.gallery_window.title("Sticker Gallery")
        self.gallery_window.geometry("400x300")

        # Load saved stickers
        self.load_stickers()

        # Close the root window (optional, to avoid extra window)
        self.root.withdraw()

    def load_stickers(self):
        """Load stickers as buttons to paste them on screen."""
        sticker_files = [f for f in os.listdir(self.gallery_path) if f.endswith(".png")]

        if not sticker_files:
            tk.Label(self.gallery_window, text="No stickers found!").pack()
            return

        for sticker in sticker_files:
            sticker_path = os.path.join(self.gallery_path, sticker)
            img = Image.open(sticker_path).resize((100, 100), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)

            btn = tk.Button(self.gallery_window, image=img_tk, command=lambda p=sticker_path: self.place_sticker(p))
            btn.image = img_tk  # Keep reference
            btn.pack(padx=5, pady=5)

    def place_sticker(self, sticker_path):
        """Places a draggable sticker on the screen."""
        DraggableSticker(sticker_path, position=(200, 200))

# Start the application with the Sticker Gallery immediately open
root = tk.Tk()
StickerGallery(root)
root.mainloop()
