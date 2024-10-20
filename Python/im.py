import tkinter as tk
from tkinter import ttk
import cv2
import mediapipe as mp
import threading
import customtkinter as ctk
from customtkinter import *
from PIL import Image, ImageTk



mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=6, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils


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
            


            


def back_to_main():
   
    if 'cap' in globals():
        stop_camera(cap)
    

    if 'camera_frame' in globals():
        camera_frame.place_forget()
    
    if 'frame' in globals():
        frame.place_forget()
    
  
    show_main()


   
def stop_camera(cap):
    if cap is not None and cap.isOpened():
        cap.release()



def start_action():
    global frame, camera_frame, cap, camera_on, on_off_button, me, games
    
    for widget in root.winfo_children():
        widget.grid_forget()
    
    frame = tk.Frame(root, bg="#0B6477")
    frame.place(x=100, y=150, width=3630, height=1720)
    
    camera_frame = tk.Label(frame)

    me = tk.Frame(root, bg="#14919B")
    me.place(x=100, y=150, width=3630, height=150)

    d_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    d = Image.open(d_path).resize((150, 150))
    photo = ImageTk.PhotoImage(d)
    lw = tk.Label(me, image=photo, bg="#14919B")
    lw.place(x=30, y=5)
    lw.image = photo

    text_label = ctk.CTkLabel(me, text="MORRON 5", font=("Arial", 26), text_color="white")
    text_label.place(x=100, y=20)
    
    camera_x = 0
    camera_y = 0
    camera_width = 3630
    camera_height = 1580
    
    camera_frame.place(x=camera_x, y=camera_y, width=camera_width, height=camera_height)
    
    back_button = ctk.CTkButton(frame, text="Back",width=200, height=50,
                                fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                                border_color="black", border_width=2, command=back_to_main)
    back_button.place(x=20, y=710)


    on_off_button = ctk.CTkButton(frame, text="Turn On Camera",width=200, height=50,
                                  fg_color="#45DFB1", text_color="blue", hover_color="#0AD1C8",
                                  border_color="black", border_width=2, command=toggle_camera)
    on_off_button.place(x=300, y=710)
    
    
    

    camera_on = False
    cap = None


    games = ctk.CTkButton(frame, text="Turn On Games",width=200, height=50,
                                  fg_color="#45DFB1", text_color="blue", hover_color="#0AD1C8",
                                  border_color="black", border_width=2, command=toggle_camera)
    games.place(x=620, y=710)


def toggle_camera():
    global cap, camera_on
    if camera_on:
        stop_camera()
        on_off_button.configure(text="Turn On Camera", text_color="blue")
    else:
        start_camera()
        on_off_button.configure(text="Turn Off Camera", text_color="red")

    


def start_camera():
    global cap, camera_on
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera not accessible.")
        return
    camera_on = True
    update_frame(cap, camera_frame, 0, 0, 3630, 1580)

def stop_camera():
    global cap, camera_on
    if cap is not None and cap.isOpened():
        camera_on = False
        cap.release()
        camera_frame.configure(image='')

def update_frame(cap, camera_frame, x, y, width, height):
    global camera_on
    if not camera_on:
        return
    
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
                cv2.putText(frame, "OK!", (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 5, hand_color, 2)
            elif is_peace_sign(hand_landmarks):
                cv2.putText(frame, "Peace!", (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 5, hand_color, 2)
            elif is_hi_sign(hand_landmarks):
                cv2.putText(frame, "Hi!", (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 5, hand_color, 2)
            elif is_call_me_sign(hand_landmarks):
                cv2.putText(frame, "Call Me!", (10, 400), cv2.FONT_HERSHEY_SIMPLEX, 5, hand_color, 2)
            elif is_up_me_sign(hand_landmarks):
                cv2.putText(frame, "Thumbs Up!", (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 5, hand_color, 2)
            elif is_drink_sign(hand_landmarks):
                cv2.putText(frame, "I'm going to drink", (40, 700), cv2.FONT_HERSHEY_SIMPLEX, 5, hand_color, 2)
            
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                       landmark_drawing_spec=mp_drawing.DrawingSpec(color=hand_color, thickness=2, circle_radius=2))
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    img = Image.fromarray(rgb_frame)
    imgtk = ImageTk.PhotoImage(image=img)
    
    camera_frame.imgtk = imgtk
    camera_frame.configure(image=imgtk)
    
    if camera_on and cap.isOpened():
        camera_frame.after(10, update_frame, cap, camera_frame, x, y, width, height)
    else:
        print("Camera is closed")

def back_to_main():
    global cap, camera_on
    stop_camera()
    if 'camera_frame' in globals():
        camera_frame.place_forget()
    if 'frame' in globals():
        frame.place_forget()
    show_main()

   


def show_tutorial():
    for widget in frame.winfo_children():
        widget.pack_forget()

    global fra, fer, fru, ff, fe, fa, fp, fd, fq, fl, ft, fk
   

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

    gg_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\peace.PNG"
    gg = Image.open(gg_path).resize((350, 350))
    photo = ImageTk.PhotoImage(gg)
    ell = tk.Label(fru, image=photo, bg="#45DFB1")
    ell.place(x=30, y=120)
    ell.image = photo 
     
    ff = tk.Frame(root, bg="#45DFB1")
    ff.place(x=1000, y=270, width=500, height=700)

    gr_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    gr = Image.open(gr_path).resize((350, 350))
    photo = ImageTk.PhotoImage(gr)
    eli = tk.Label(ff, image=photo, bg="#45DFB1")
    eli.place(x=30, y=120)
    eli.image = photo

    fe = tk.Frame(root, bg="#45DFB1")
    fe.place(x=1700, y=270, width=500, height=700)

    ge_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\call.PNG"
    ge = Image.open(ge_path).resize((350, 350))
    photo = ImageTk.PhotoImage(ge)
    elo = tk.Label(fe, image=photo, bg="#45DFB1")
    elo.place(x=30, y=120)
    elo.image = photo

    fa = tk.Frame(root, bg="#45DFB1")
    fa.place(x=2400, y=270, width=500, height=700)

    ga_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    ga = Image.open(ga_path).resize((350, 350))
    photo = ImageTk.PhotoImage(ga)
    ela = tk.Label(fa, image=photo, bg="#45DFB1")
    ela.place(x=30, y=120)
    ela.image = photo 

    fp = tk.Frame(root, bg="#45DFB1")
    fp.place(x=3100, y=270, width=500, height=700)

    go_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\drink.PNG"
    go = Image.open(go_path).resize((350, 350))
    photo = ImageTk.PhotoImage(go)
    elx = tk.Label(fp, image=photo, bg="#45DFB1")
    elx.place(x=30, y=120)
    elx.image = photo 

    
#Down frame

    fd = tk.Frame(root, bg="#45DFB1")
    fd.place(x=300, y=1050, width=500, height=700)

    gp_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    gp = Image.open(gp_path).resize((350, 350))
    photo = ImageTk.PhotoImage(gp)
    elq = tk.Label(fd, image=photo, bg="#45DFB1")
    elq.place(x=30, y=120)
    elq.image = photo 
       
    fq = tk.Frame(root, bg="#45DFB1")
    fq.place(x=1000, y=1050, width=500, height=700)

    gd_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    gd = Image.open(gd_path).resize((350, 350))
    photo = ImageTk.PhotoImage(gd)
    elw = tk.Label(fq, image=photo, bg="#45DFB1")
    elw.place(x=30, y=120)
    elw.image = photo

    ft = tk.Frame(root, bg="#45DFB1")
    ft.place(x=1700, y=1050, width=500, height=700)

    gk_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    gk = Image.open(gk_path).resize((350, 350))
    photo = ImageTk.PhotoImage(gk)
    elp = tk.Label(ft, image=photo, bg="#45DFB1")
    elp.place(x=30, y=120)
    elp.image = photo

    fl = tk.Frame(root, bg="#45DFB1")
    fl.place(x=2400, y=1050, width=500, height=700)

    gs_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    gs = Image.open(gs_path).resize((350, 350))
    photo = ImageTk.PhotoImage(gs)
    elt = tk.Label(fl, image=photo, bg="#45DFB1")
    elt.place(x=30, y=120)
    elt.image = photo 

    fk = tk.Frame(root, bg="#45DFB1")
    fk.place(x=3100, y=1050, width=500, height=700)

    gy_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\logoo.PNG"
    gy = Image.open(gy_path).resize((350, 350))
    photo = ImageTk.PhotoImage(gy)
    elf = tk.Label(fk, image=photo, bg="#45DFB1")
    elf.place(x=30, y=120)
    elf.image = photo 

def Social():
    for widget in frame.winfo_children():
        widget.pack_forget()

    global frr
    global rr
    fra.place_forget()
    frr = tk.Frame(root, bg="#213A57")
    frr.place(x=155, y=200, width=3520, height=1620)
   
    text_label.place_forget()
    fr.place_forget()
    image_label.place_forget()
   
    path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\set.PNG"
    new = Image.open(path).resize((60, 60))  
    mm = ImageTk.PhotoImage(new)  

    so_button = ctk.CTkButton(frr, text="", image=mm, corner_radius=25, width=50, height=50,
                                fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                                border_color="black", border_width=2, command=return_to_settings)
    so_button.place(x=12, y=20)
    


def TP():
    for widget in frame.winfo_children():
        widget.pack_forget()

    global frr
    global rr
    fra.place_forget()
    frr = tk.Frame(root, bg="#213A57")
    frr.place(x=155, y=200, width=3520, height=1620)

    text_label.place_forget()
    fr.place_forget()
    image_label.place_forget()


    new_image_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\set.PNG"
    new_image = Image.open(new_image_path).resize((60, 60))  
    new_image_pho = ImageTk.PhotoImage(new_image)  

    
    tp_button = ctk.CTkButton(frr, text="", image=new_image_pho, corner_radius=25, width=50, height=50,
                                fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                                border_color="black", border_width=2, command=return_to_settings)
    tp_button.place(x=12, y=20)


  


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
    button.place(x=200, y=100)

 
    button1 = ctk.CTkButton(fra, text="Log in", width=200, height=50,
                            fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                            border_color="black", border_width=2, command=show_login)
    button1.place(x=200, y=200)

    

    sgt = ctk.CTkButton(fra, text="Social Media", width=200, height=50,
                           fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                           border_color="black", border_width=2, command=Social)
    sgt.place(x=600, y=100)

 
    faq = ctk.CTkButton(fra, text="Terms and Privacy", width=200, height=50,
                            fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                            border_color="black", border_width=2, command=TP)
    faq.place(x=600, y=200)

    

    back_button = ctk.CTkButton(fra, text="Back", corner_radius=25, width=200, height=50,
                                fg_color="#45DFB1", text_color="black", hover_color="#0AD1C8",
                                border_color="black", border_width=2, command=show_main)
    back_button.place(x=300, y=600)

    ho = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\bak.PNG"
    hom = Image.open(ho).resize((250, 250))
    photo = ImageTk.PhotoImage(hom)
    hm = tk.Label(fra, image=photo, bg="#213A57") 
    hm.place(x=420, y=1260)  
    hm.image = photo  

    abo = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\ab.PNG"
    abou = Image.open(abo).resize((130, 130))
    photo = ImageTk.PhotoImage(abou)
    ao = tk.Label(fra, image=photo, bg="#213A57") 
    ao.place(x=250, y=210)  
    ao.image = photo  
    




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

    vince = ctk.CTkLabel(rr, text="ALOBIN",
                                     text_color="white", font=("Arial", 16), wraplength=800)
    vince.place(x=120, y=30)

    vince = ctk.CTkLabel(rr, text="BACKEND",
                                     text_color="white", font=("Arial", 16), wraplength=800)
    vince.place(x=100, y=300)

    g_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\picc.PNG"
    

    gg_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\bara.PNG"
    

    gi_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\jc.PNG"
    

    ii_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\ash.PNG"
  
    
     

    i_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\rick.PNG"
   

   
    ab = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\set.PNG"
    abb = Image.open(ab).resize((60, 60))  
    abu = ImageTk.PhotoImage(abb)  


    about_back = ctk.CTkButton(frr, text="",image=abu, corner_radius=25, width=50, height=50,
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
    if 'me' in globals():
        me.place_forget()     
        

       
    
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

i_path = "C:\\Users\\ASUS\\OneDrive - Asia Pacific College\\Documents\\Alobin ICT241\\Python\\star.PNG"
i = Image.open(i_path).resize((155, 150))
ph = ImageTk.PhotoImage(i)
lb = tk.Label(frame, i=ph, bg="#0B6477")
lb.place(x=1460, y=92)
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