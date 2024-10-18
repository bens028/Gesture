import tkinter as tk
from tkinter import ttk
import cv2
import mediapipe as mp
import threading
import customtkinter as ctk
from customtkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
import mysql.connector
from tkinter import messagebox

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=6, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

#hii
#aha7hdaybfysr
#hello
def is_hi_sign(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    
   
    return (index_finger_tip.y < thumb_tip.y and 
            middle_finger_tip.y < thumb_tip.y and
            ring_finger_tip.y < thumb_tip.y and 
            pinky_finger_tip.y < thumb_tip.y and
            thumb_tip.y < thumb_ip.y)

def is_peace_sign(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    
    return (index_finger_tip.y < thumb_tip.y and 
            middle_finger_tip.y < thumb_tip.y and 
            ring_finger_tip.y > thumb_tip.y and 
            pinky_finger_tip.y > thumb_tip.y)

def is_up_me_sign(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

  
    return (thumb_tip.y < index_finger_tip.y and 
            thumb_tip.y < middle_finger_tip.y and 
            thumb_tip.y < ring_finger_tip.y and 
            thumb_tip.y < pinky_finger_tip.y)
    


def is_call_me_sign(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    pinky_finger_dip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP]
   


    return (thumb_tip.y < index_finger_tip.y and 
            thumb_tip.y < middle_finger_tip.y and
            thumb_tip.y < ring_finger_tip.y and
            pinky_finger_tip.y < index_finger_tip.y and 
            pinky_finger_tip.y < middle_finger_tip.y and
            pinky_finger_tip.y < ring_finger_tip.y or
            thumb_tip.x > pinky_finger_dip.x and
            pinky_finger_dip.x > pinky_finger_tip.x)      


def is_drink_sign(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    return (thumb_tip.y > index_finger_tip.y and 
            thumb_tip.y > middle_finger_tip.y and
            thumb_tip.y > ring_finger_tip.y and
            pinky_finger_tip.y < index_finger_tip.y and 
            pinky_finger_tip.y < middle_finger_tip.y and
            pinky_finger_tip.y < ring_finger_tip.y and
            pinky_finger_tip.y < thumb_tip.y)
            

def is_ok_sign(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    return (abs(thumb_tip.x - index_finger_tip.x) < 0.05 and  
            abs(thumb_tip.y - index_finger_tip.y) < 0.05 and 
            middle_finger_tip.y < thumb_tip.y and
            ring_finger_tip.y < thumb_tip.y and
            pinky_finger_tip.y < thumb_tip.y)
            


            
   
def stop_camera(cap):
    if cap is not None and cap.isOpened():
        cap.release()

def back_to_main():
   
    if 'cap' in globals():
        stop_camera(cap)
    

    if 'camera_frame' in globals():
        camera_frame.place_forget()
    
    if 'frame' in globals():
        frame.place_forget()
    
  
    show_main()

def start_action():
    global frame, camera_frame, cap
    
    for widget in root.winfo_children():
        widget.grid_forget()

    
    frame = tk.Frame(root, bg="#0B6477")
    frame.place(x=100, y=150, width=3630, height=1720)

   
    camera_frame = tk.Label(frame)
    
   
    camera_x = 1500  
    camera_y = 500 
    camera_width = 1000 
    camera_height = 1000  
    
    camera_frame.place(x=camera_x, y=camera_y, width=camera_width, height=camera_height)
    
    
    back_button = ctk.CTkButton(frame, text="Back", corner_radius=25, width=200, height=50,
                                fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                                border_color="black", border_width=2, command=back_to_main)
    back_button.place(x=camera_width + 20, y=20)  
    
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera not accessible.")
        return

    camera_thread = threading.Thread(target=update_frame, args=(cap, camera_frame, camera_x, camera_y, camera_width, camera_height))
    camera_thread.start()

def update_frame(cap, camera_frame, x, y, width, height):
    ret, frame = cap.read()
    if not ret:
        print("Unable to capture video")
        return

    
    frame = cv2.flip(frame, 1)
    
    
    frame = cv2.resize(frame, (width, height))
    
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    
    hand_color = (0, 255, 0)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            if is_ok_sign(hand_landmarks):
                cv2.putText(frame, "OK!", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, hand_color, 2)
            elif is_peace_sign(hand_landmarks):
                cv2.putText(frame, "Peace!", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, hand_color, 2)
            elif is_hi_sign(hand_landmarks):
                cv2.putText(frame, "Hi!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, hand_color, 2)
            elif is_call_me_sign(hand_landmarks):
                cv2.putText(frame, "Call Me!", (10, 190), cv2.FONT_HERSHEY_SIMPLEX, 1, hand_color, 2)
            elif is_up_me_sign(hand_landmarks):
                cv2.putText(frame, "Thumbs Up!", (10, 280), cv2.FONT_HERSHEY_SIMPLEX, 1, hand_color, 2)
            elif is_drink_sign(hand_landmarks):
                cv2.putText(frame, "I'm going to drink", (40, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, hand_color, 2)

           
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                       landmark_drawing_spec=mp_drawing.DrawingSpec(color=hand_color, thickness=2, circle_radius=2))

   
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
   
    img = Image.fromarray(rgb_frame)
    imgtk = ImageTk.PhotoImage(image=img)

   
    camera_frame.imgtk = imgtk
    camera_frame.configure(image=imgtk)
    
    if cap.isOpened():
        camera_frame.after(10, update_frame, cap, camera_frame, x, y, width, height)
    else:
        print("Camera is closed")

   


def show_tutorial():
    for widget in frame.winfo_children():
        widget.pack_forget()

    global fra
    global fer
    global fru
    global ff
    global fe
    global fa
    global fp
    global fd
    global fq
    global fl
    global ft
    global fk
    

#Up Frame

    text_label.place_forget()
    fr.place_forget()
    image_label.place_forget()

    fer = tk.Frame(root, bg="#213A57")
    fer.place(x=155, y=200, width=3520, height=1620)

    back_button = ctk.CTkButton(fer, text=".", corner_radius=25, width=35, height=35,
                                fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                                border_color="black", border_width=2, command=show_main)
    back_button.place(x=12, y=20)

    fru = tk.Frame(root, bg="#45DFB1")
    fru.place(x=300, y=270, width=500, height=700)

    gg_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    gg = Image.open(gg_path).resize((450, 450))
    photo = ImageTk.PhotoImage(gg)
    ell = tk.Label(fru, image=photo, bg="#45DFB1")
    ell.place(x=30, y=120)
    ell.image = photo 
     
    ff = tk.Frame(root, bg="#45DFB1")
    ff.place(x=1000, y=270, width=500, height=700)

    gr_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    gr = Image.open(gr_path).resize((450, 450))
    photo = ImageTk.PhotoImage(gr)
    eli = tk.Label(ff, image=photo, bg="#45DFB1")
    eli.place(x=30, y=120)
    eli.image = photo

    fe = tk.Frame(root, bg="#45DFB1")
    fe.place(x=1700, y=270, width=500, height=700)

    ge_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    ge = Image.open(ge_path).resize((450, 450))
    photo = ImageTk.PhotoImage(ge)
    elo = tk.Label(fe, image=photo, bg="#45DFB1")
    elo.place(x=30, y=120)
    elo.image = photo

    fa = tk.Frame(root, bg="#45DFB1")
    fa.place(x=2400, y=270, width=500, height=700)

    ga_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    ga = Image.open(ga_path).resize((450, 450))
    photo = ImageTk.PhotoImage(ga)
    ela = tk.Label(fa, image=photo, bg="#45DFB1")
    ela.place(x=30, y=120)
    ela.image = photo 

    fp = tk.Frame(root, bg="#45DFB1")
    fp.place(x=3100, y=270, width=500, height=700)

    go_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    go = Image.open(go_path).resize((450, 450))
    photo = ImageTk.PhotoImage(go)
    elx = tk.Label(fp, image=photo, bg="#45DFB1")
    elx.place(x=30, y=120)
    elx.image = photo 

    
#Down frame

    fd = tk.Frame(root, bg="#45DFB1")
    fd.place(x=300, y=1050, width=500, height=700)

    gp_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    gp = Image.open(gp_path).resize((450, 450))
    photo = ImageTk.PhotoImage(gp)
    elq = tk.Label(fd, image=photo, bg="#45DFB1")
    elq.place(x=30, y=120)
    elq.image = photo 
       
    fq = tk.Frame(root, bg="#45DFB1")
    fq.place(x=1000, y=1050, width=500, height=700)

    gd_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    gd = Image.open(gd_path).resize((450, 450))
    photo = ImageTk.PhotoImage(gd)
    elw = tk.Label(fq, image=photo, bg="#45DFB1")
    elw.place(x=30, y=120)
    elw.image = photo

    ft = tk.Frame(root, bg="#45DFB1")
    ft.place(x=1700, y=1050, width=500, height=700)

    gk_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    gk = Image.open(gk_path).resize((450, 450))
    photo = ImageTk.PhotoImage(gk)
    elp = tk.Label(ft, image=photo, bg="#45DFB1")
    elp.place(x=30, y=120)
    elp.image = photo

    fl = tk.Frame(root, bg="#45DFB1")
    fl.place(x=2400, y=1050, width=500, height=700)

    gs_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    gs = Image.open(gs_path).resize((450, 450))
    photo = ImageTk.PhotoImage(gs)
    elt = tk.Label(fl, image=photo, bg="#45DFB1")
    elt.place(x=30, y=120)
    elt.image = photo 

    fk = tk.Frame(root, bg="#45DFB1")
    fk.place(x=3100, y=1050, width=500, height=700)

    gy_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    gy = Image.open(gy_path).resize((450, 450))
    photo = ImageTk.PhotoImage(gy)
    elf = tk.Label(fk, image=photo, bg="#45DFB1")
    elf.place(x=30, y=120)
    elf.image = photo 




def show_settings():
   
    for widget in frame.winfo_children():
        widget.pack_forget()

    global fra
    if 'frr' in globals():
        frr.place_forget()
   
    text_label.place_forget()
    fr.place_forget()
    image_label.place_forget()

  
    fra = tk.Frame(root, bg="#213A57")
    fra.place(x=155, y=200, width=3520, height=1620)


    button = ctk.CTkButton(fra, text="About us", width=200, height=50,
                           fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                           border_color="black", border_width=2, command=about)
    button.place(x=200, y=20)

 
    button1 = ctk.CTkButton(fra, text="Log in", width=200, height=50,
                            fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                            border_color="black", border_width=2, command=show_login)
    button1.place(x=400, y=20)


    back_button = ctk.CTkButton(fra, text="Back", corner_radius=25, width=200, height=50,
                                fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                                border_color="black", border_width=2, command=show_main)
    back_button.place(x=300, y=600)


def about():
    global frr
    global rr
    fra.place_forget()
    frr = tk.Frame(root, bg="#213A57")
    frr.place(x=155, y=200, width=3520, height=1620)
    rr = tk.Frame(root, bg="#14919B")
    rr.place(x=155, y=1020, width=3520, height=810)

  
    about_title = ctk.CTkLabel(frr, text="About Us", text_color="white", font=("Arial", 30))
    about_title.place(x=200, y=100)

    about_description = ctk.CTkLabel(frr, text="This application is dedicated to providing excellent tutorial services about sign language.",
                                     text_color="white", font=("Arial", 16), wraplength=800)
    about_description.place(x=200, y=180)

   
    about_info = ctk.CTkLabel(frr, text="Our mission is to innovate and inspire through our state-of-the-art technology. "
                                        "We strive to make the world a better place with sustainable solutions.", 
                                        text_color="white", font=("Arial", 14), wraplength=1000)
    about_info.place(x=200, y=200)

    vince = ctk.CTkLabel(rr, text="VINCE NELMAR ALOBIN - BACKEND",
                                     text_color="white", font=("Arial", 16), wraplength=800)
    vince.place(x=20, y=300)

    g_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\picc.PNG"
    g = Image.open(g_path).resize((450, 450))
    photo = ImageTk.PhotoImage(g)
    el = tk.Label(rr, image=photo, bg="#14919B")
    el.place(x=100, y=150)
    el.image = photo  

    gg_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\bara.PNG"
    gg = Image.open(gg_path).resize((450, 450))
    photo = ImageTk.PhotoImage(gg)
    e = tk.Label(rr, image=photo, bg="#14919B")
    e.place(x=800, y=150)
    e.image = photo  

    gi_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\jc.PNG"
    gi = Image.open(gi_path).resize((450, 450))
    photo = ImageTk.PhotoImage(gi)
    ee = tk.Label(rr, image=photo, bg="#14919B")
    ee.place(x=1500, y=150)
    ee.image = photo  

    ii_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\ash.PNG"
    ii = Image.open(ii_path).resize((450, 450))
    photo = ImageTk.PhotoImage(ii)
    eg = tk.Label(rr, image=photo, bg="#14919B")
    eg.place(x=2200, y=150)
    eg.image = photo  

    i_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\rick.PNG"
    i = Image.open(i_path).resize((450, 450))
    photo = ImageTk.PhotoImage(i)
    og = tk.Label(rr, image=photo, bg="#14919B")
    og.place(x=2900, y=150)
    og.image = photo  

   


    about_back = ctk.CTkButton(frr, text=".", corner_radius=25, width=50, height=50,
                               fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                               border_color="black", border_width=2, command=return_to_settings)
    about_back.place(x=20, y=20)


def return_to_settings():
    show_settings()
    frr.place_forget()
    fre.place_forget()
    rr.place_forget()
    
def show_login():
    global frr
    global fre
    fra.place_forget()
    frr = tk.Frame(root, bg="#213A57")
    frr.place(x=155, y=200, width=3520, height=1620)
    fre = tk.Frame(root, bg="#14919B")
    fre.place(x=155, y=200, width=1200, height=1620)

    
    img_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\user.PNG"
    img = Image.open(img_path).resize((150, 150))
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(frr, image=photo, bg="#213A57")
    label.place(x=1300, y=400)
    label.image = photo  


    mg_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\pass.PNG"
    mg = Image.open(mg_path).resize((150, 150))
    photo = ImageTk.PhotoImage(mg)
    bel = tk.Label(frr, image=photo, bg="#213A57")
    bel.place(x=1300, y=600)
    bel.image = photo  

    g_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\pep.PNG"
    g = Image.open(g_path).resize((1000, 1000))
    photo = ImageTk.PhotoImage(g)
    el = tk.Label(fre, image=photo, bg="#14919B")
    el.place(x=80, y=400)
    el.image = photo  

 
    user_label = ctk.CTkLabel(frr, text="Username", text_color="white", font=("Arial", 20))
    user_label.place(x=650, y=180)

    wel_label = ctk.CTkLabel(fre, text="WELCOME!", text_color="white", font=("Times New Roman", 50))
    wel_label.place(x=140, y=80)   

    user_entry = ctk.CTkEntry(frr, width=200, height=30)
    user_entry.place(x=650, y=205)

    pass_label = ctk.CTkLabel(frr, text="Password", text_color="white", font=("Arial", 20))
    pass_label.place(x=650, y=260)

    pass_entry = ctk.CTkEntry(frr, width=200, show="*", height=30)
    pass_entry.place(x=650, y=285)


    login_button = ctk.CTkButton(frr, text="Log in", corner_radius=25, width=150, height=40,
                                 fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                                 border_color="black", border_width=2)
    login_button.place(x=560, y=390)

    sign_button = ctk.CTkButton(frr, text="Sign up", corner_radius=25, width=150, height=40,
                                 fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                                 border_color="black", border_width=2)
    sign_button.place(x=730, y=390)

  
    login_back = ctk.CTkButton(frr, text="Back to Settings", corner_radius=25, width=200, height=50,
                               fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                               border_color="black", border_width=2, command=return_to_settings)
    login_back.place(x=665, y=500)

    def register_user():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Input Error", "All fields are required")
        return

    try:
        cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        messagebox.showinfo("Registration", "Registration successful!")
        user_entry.delete(0, tk.END)
        pass_entry.delete(0, tk.END())
        status_label.config(text="")
    
   
    username = user_entry.get()
    password = pass_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Input Error", "All fields are required")
        return

    cursor.execute("SELECT password FROM user WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result and password == result[0]:  # Check plain text password
        status_label.config(text=f"Welcome, {username}!", fg="green")
    else:
        status_label.config(text="Invalid username or password.", fg="red")




#code here for database login
#Button Login_button
#Textfield user_entry pass_entry
db = mysql.connector.connect(
    host="localhost",
    port=3307,              # MySQL server port
    user="root",
    password="",
    database="client"      # Replace with your database name
)
cursor = db.cursor()

# Create 'users' table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    )
""")
# Status label to show login feedback
status_label = tk.Label(root, text="", font=("Helvetica", 10))
status_label.grid(row=3, column=0, columnspan=2, pady=10)







def show_main():
    
    for widget in frame.winfo_children():
        widget.pack_forget()
    for widget in fr.winfo_children():
        widget.pack_forget()

   
    text_label.place(x=150, y=75)
    fr.place(x=100, y=150, width=1200, height=1720)
    image_label.place(x=50, y=50)  
    label.place(x=1460, y=640)

    
    if 'fra' in globals():
        fra.place_forget()
    if 'fer' in globals():
        fer.place_forget()
    if 'frr' in globals():
        frr.place_forget()
    if 'fre' in globals():
        fre.place_forget()
    if 'rr' in globals():
        rr.place_forget()
    if 'fer' in globals():
        fer.place_forget()
    if 'fru' in globals():
        fru.place_forget()
    if 'ff' in globals():
        ff.place_forget()
    if 'fe' in globals():
        fe.place_forget()
    if 'fa' in globals():
        fa.place_forget()
    if 'fp' in globals():
        fp.place_forget() 
    if 'fd' in globals():
        fd.place_forget()
    if 'fq' in globals():
        fq.place_forget()
    if 'ft' in globals():
        ft.place_forget()
    if 'fl' in globals():
        fl.place_forget()
    if 'fk' in globals():
        fk.place_forget()
                      

       
    
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")  

root = ctk.CTk()
root.title("Sign Language")
root.geometry("3840x2160")



frame = tk.Frame(root, bg="#0B6477")
frame.place(x=100, y=150, width=3630, height=1720)

fr = tk.Frame(root, bg="#14919B")
fr.place(x=100, y=150, width=1200, height=1720)

image_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
image = Image.open(image_path).resize((300, 300))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(fr, image=photo, bg="#14919B") 
image_label.place(x=50, y=50)  
image_label.image = photo  

 
img_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\set.PNG"
img = Image.open(img_path).resize((150, 150))
photo = ImageTk.PhotoImage(img)
label = tk.Label(frame, image=photo, bg="#0B6477")
label.place(x=1460, y=630)
label.image = photo  


im_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\tu.PNG"
im = Image.open(im_path).resize((150, 150))
pho = ImageTk.PhotoImage(im)
lab = tk.Label(frame, im=pho, bg="#0B6477")
lab.place(x=1460, y=380)
lab.image = photo

i_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\sta.PNG"
i = Image.open(i_path).resize((160, 150))
ph = ImageTk.PhotoImage(i)
lb = tk.Label(frame, i=ph, bg="#0B6477")
lb.place(x=1460, y=100)
lb.image = photo 

ima_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\com.PNG"
ima = Image.open(ima_path).resize((1300, 1300))
p = ImageTk.PhotoImage(ima)
lbl = tk.Label(fr, ima=p, bg="#14919B")
lbl.place(x=20, y=400)
lbl.image = photo 

i_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\commu.PNG"
i = Image.open(i_path).resize((1000, 1000))
pp = ImageTk.PhotoImage(i)
l = tk.Label(frame, i=pp, bg="#0B6477")
l.place(x=2400, y=400)
l.image = photo 

text_label = ctk.CTkLabel(fr, text="MORRON 5", font=("Arial", 26), text_color="white")
text_label.place(x=150, y=72)  


start_button = ctk.CTkButton(frame, text="Start", corner_radius=25, width=200, height=50,
                              fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                              border_color="black", border_width=2, command=start_action)
start_button.place(x=720, y=50) 


tutorial_button = ctk.CTkButton(frame, text="Tutorial", corner_radius=25, width=200, height=50,
                                 fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                                 border_color="black", border_width=2, command=show_tutorial)
tutorial_button.place(x=720, y=170)  


settings_button = ctk.CTkButton(frame, text="Settings", corner_radius=25, width=200, height=50,
                                 fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                                 border_color="black", border_width=2,command=show_settings)
settings_button.place(x=720, y=290)  

root.mainloop()                           