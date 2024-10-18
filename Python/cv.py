import tkinter as tk
from tkinter import Frame
import cv2
from PIL import Image, ImageTk

#hello try

# Initialize Tkinter window
window = tk.Tk()
window.geometry("1280x720")  # Set window size
window.title("Camera in Frame")

# Function to start camera feed
def start_camera():
    cap = cv2.VideoCapture(0)  # Open default camera
    update_frame(cap)

# Function to update the frame with the camera feed
def update_frame(cap):
    _, frame = cap.read()  # Capture frame-by-frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert color format
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    
    camera_label.imgtk = imgtk
    camera_label.config(image=imgtk)
    camera_label.after(10, lambda: update_frame(cap))  # Continuously update

# Frame to display camera feed
camera_frame = Frame(window, width=640, height=480, bg="black")
camera_frame.place(x=100, y=100)  # Adjust coordinates here (x=320, y=100)

# Label inside the frame to hold the camera image
camera_label = tk.Label(camera_frame)
camera_label.pack()

# Start button to initiate the camera
start_button = tk.Button(window, text="Start Camera", command=start_camera)
start_button.place(x=560, y=600)  # Adjust coordinates of the button

# Run the Tkinter main loop
window.mainloop()
