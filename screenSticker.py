import tkinter as tk
import os
from PIL import Image, ImageTk

class DraggableSticker:
    def __init__(self, sticker_path, position=(100, 100)):
        self.sticker_path = sticker_path
        self.scale_factor = 1.0  # Track scaling

        # Create a new window for the sticker
        self.root = tk.Toplevel()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-transparentcolor", "gray")

        self.load_image()

        # Create a label to display the image
        self.label = tk.Label(self.root, image=self.tk_image, bg="gray")
        self.label.pack()
        self.root.geometry(f"{self.image.width}x{self.image.height}+{position[0]}+{position[1]}")

        # Bind mouse events to the label
        self.label.bind("<ButtonPress-1>", self.start_move)
        self.label.bind("<B1-Motion>", self.on_move)
        self.label.bind("<Button-3>", self.remove_sticker)  # Right-click to remove
        self.label.bind("<Shift-MouseWheel>", self.size_up)  # Shift to size up
        self.label.bind("<Control-MouseWheel>", self.size_down)  # Control to size down

    # Load the image and convert it to a format that Tkinter can display
    def load_image(self):
        self.image = Image.open(self.sticker_path).convert("RGBA")
        self.resized_image = self.image.copy()
        self.tk_image = ImageTk.PhotoImage(self.resized_image)

    # Start moving the sticker
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    # Move the sticker
    def on_move(self, event):
        dx = event.x - self.x
        dy = event.y - self.y
        x = self.root.winfo_x() + dx
        y = self.root.winfo_y() + dy
        self.root.geometry(f"+{x}+{y}")

    # Remove the sticker
    def remove_sticker(self, event):
        self.root.destroy()

    # Size up the sticker
    def size_up(self, event):
        self.scale_factor *= 1.1  # Zoom in
        self.scale_factor = min(self.scale_factor, 10.0)  # Limit max size
        self.resize_sticker()

    # Size down the sticker
    def size_down(self, event):
        self.scale_factor *= 0.9  # Zoom out
        self.scale_factor = max(self.scale_factor, 0.1)  # Limit min size
        self.resize_sticker()

    # Resize the sticker
    def resize_sticker(self):
        # Resize the image
        new_size = (int(self.image.width * self.scale_factor), int(self.image.height * self.scale_factor))
        # Resize the image using LANCZOS filter for better quality
        self.resized_image = self.image.resize(new_size, Image.LANCZOS)
        # Update the Tkinter image
        self.tk_image = ImageTk.PhotoImage(self.resized_image)
        # Update the label with the new image
        self.label.config(image=self.tk_image)
        # Update the window size to match the new image size
        self.root.geometry(f"{new_size[0]}x{new_size[1]}+{self.root.winfo_x()}+{self.root.winfo_y()}")

class StickerGallery:
    def __init__(self, root, gallery_path="Gallery"):
        self.root = root
        self.gallery_path = gallery_path

        # Create the gallery window
        self.gallery_window = tk.Toplevel(root)
        self.gallery_window.title("Sticker Gallery")
        self.gallery_window.geometry("600x400")

        # Create a close button for the gallery window
        close_button = tk.Button(self.gallery_window, text="Close", command=self.close_gallery)
        close_button.pack(pady=10)

        # Create a frame for the thumbnails grid
        self.thumbnail_frame = tk.Frame(self.gallery_window)
        self.thumbnail_frame.pack(fill=tk.BOTH, expand=True)

        self.load_stickers()
        self.root.withdraw()

    # Load stickers from the gallery folder
    def load_stickers(self):
        if not os.path.exists(self.gallery_path):
            tk.Label(self.gallery_window, text="Gallery folder not found!").pack()
            return

        sticker_files = [f for f in os.listdir(self.gallery_path) if f.endswith(".png")]
        if not sticker_files:
            tk.Label(self.gallery_window, text="No stickers found!").pack()
            return

        # Create buttons with thumbnails for each sticker
        row = 0
        col = 0
        for sticker in sticker_files:
            sticker_path = os.path.join(self.gallery_path, sticker)
            img = Image.open(sticker_path).resize((100, 100), Image.LANCZOS)  # Resize for thumbnail
            img_tk = ImageTk.PhotoImage(img)
            # Create a button with the image and a command to place the sticker
            btn = tk.Button(self.thumbnail_frame, image=img_tk, command=lambda p=sticker_path: self.place_sticker(p))
            btn.image = img_tk  # Store reference to prevent garbage collection
            btn.grid(row=row, column=col, padx=5, pady=5)  # Grid layout for thumbnails
            col += 1
            if col == 5:  # Create a new row after 5 thumbnails
                col = 0
                row += 1

    def place_sticker(self, sticker_path):
        DraggableSticker(sticker_path, position=(200, 200))

    # Close the gallery window
    def close_gallery(self):
        self.gallery_window.destroy()

root = tk.Tk()
StickerGallery(root)
root.mainloop()
