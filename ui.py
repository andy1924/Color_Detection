import tkinter as tk
from tkinter import filedialog, Label, Button
import os
import cv2
from PIL import Image, ImageTk
import webcolors
class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dominant Color Detection")
        self.root.geometry("600x400")

        self.label = Label(root, text="Upload an image to detect its dominant color", font=("Arial", 14))
        self.label.pack(pady=20)

        self.upload_button = Button(root, text="Upload Image", command=self.upload_image, font=("Arial", 12))
        self.upload_button.pack(pady=10)

        # Label to show the uploaded image
        self.image_label = Label(root)
        self.image_label.pack(pady=10)

        # Label to show the dominant color name
        self.result_label = Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Variable to store the image path (without unnecessary path manipulation)
        self.image_path = None

    def upload_image(self):
        # Open file dialog to select an image
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            # Extract the filename (without unnecessary copying)
            self.image_path = os.path.basename(file_path)

            # Display the image
            img = Image.open(file_path)
            img = img.resize((250, 250), Image.ANTIALIAS)
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk

if __name__ == "__main__":
    root = tk.Tk()
    ui = UI(root)
    root.mainloop()