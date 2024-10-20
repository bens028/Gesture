import tkinter as tk
from tkinter import Canvas
import cv2
import mediapipe as mp
from PIL import Image, ImageTk
import random

class HandDodgeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hand Dodge Game")
        self.root.geometry("640x480")
        
        
        self.cap = cv2.VideoCapture(0)
        
        
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)
        self.mp_drawing = mp.solutions.drawing_utils
        
        
        self.canvas = Canvas(root, width=640, height=480)
        self.canvas.pack()
        
        
        self.balls = []
        self.ball_speed = 5
        
        
        self.hand_tip = None  
        
        
        self.update_frame()
        self.fall_balls()
        
    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            
            frame = cv2.flip(frame, 1)
            
            
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = self.hands.process(rgb_frame)
            
            
            if result.multi_hand_landmarks:
                for hand_landmarks in result.multi_hand_landmarks:
                    
                    h, w, c = frame.shape
                    index_finger_tip = hand_landmarks.landmark[8]  
                    x_tip, y_tip = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
                    
                    
                    self.hand_tip = (x_tip, y_tip)
                    cv2.circle(frame, self.hand_tip, 10, (0, 255, 0), -1)  
                    
                    
                    self.detect_collision(x_tip, y_tip)
            
            
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            imgtk = ImageTk.PhotoImage(image=img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
            self.canvas.imgtk = imgtk
        
        
        self.root.after(10, self.update_frame)
    
    def fall_balls(self):
       
        if random.randint(1, 20) == 1:
            ball = {'x': random.randint(0, 600), 'y': 0, 'r': 20}  
            self.balls.append(ball)
        
        
        for ball in self.balls:
            ball['y'] += self.ball_speed
            self.canvas.create_oval(ball['x'], ball['y'], ball['x'] + ball['r'], ball['y'] + ball['r'], fill="red")
        
        
        self.balls = [ball for ball in self.balls if ball['y'] < 480]
        
        
        self.root.after(50, self.fall_balls)
    
    def detect_collision(self, hx, hy):
        
        for ball in self.balls:
            
            distance = ((ball['x'] - hx) ** 2 + (ball['y'] - hy) ** 2) ** 0.5
            if distance < ball['r']:  
                print("Collision Detected!")
                self.end_game()
    
    def end_game(self):
        self.cap.release()
        self.root.quit()

root = tk.Tk()
game = HandDodgeGame(root)
root.mainloop()
