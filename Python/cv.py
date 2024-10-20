import tkinter as tk
from tkinter import Label, Frame
import cv2
from PIL import Image, ImageTk

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Camera On/Off Example")
        self.root.geometry("800x600")  # Larger window to accommodate camera and buttons
        
        # Frame for the camera
        self.camera_frame = Frame(root, width=640, height=480, bg="black")
        self.camera_frame.pack(side=tk.TOP, padx=10, pady=10)
        
        # Frame to display the camera feed
        self.camera_label = Label(self.camera_frame)
        self.camera_label.pack()

        # Frame for buttons
        self.button_frame = Frame(root)
        self.button_frame.pack(side=tk.BOTTOM, pady=20)

        # On and Off buttons
        self.on_button = tk.Button(self.button_frame, text="On", command=self.start_camera)
        self.on_button.pack(side=tk.LEFT, padx=10)

        self.off_button = tk.Button(self.button_frame, text="Off", command=self.stop_camera)
        self.off_button.pack(side=tk.RIGHT, padx=10)

        self.cap = None
        self.is_camera_on = False

    def start_camera(self):
        if not self.is_camera_on:
            self.cap = cv2.VideoCapture(0)
            self.is_camera_on = True
            self.update_frame()

    def stop_camera(self):
        if self.is_camera_on:
            self.is_camera_on = False
            if self.cap is not None:
                self.cap.release()
            self.display_placeholder()

    def update_frame(self):
        if self.is_camera_on:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.camera_label.imgtk = imgtk
                self.camera_label.config(image=imgtk)
            self.root.after(10, self.update_frame)

    def display_placeholder(self):
        placeholder = Image.new("RGB", (640, 480), color="gray")
        img_placeholder = ImageTk.PhotoImage(image=placeholder)
        self.camera_label.imgtk = img_placeholder
        self.camera_label.config(image=img_placeholder)

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()
