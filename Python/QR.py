import tkinter as tk
from tkinter import messagebox
import random
import string


orders = []
current_order = None  
timer_duration = 30 
remaining_time = timer_duration 
timer_running = False 
pick_up_code = "" 


food_prices = {
    "Pizza": 8.00,
    "Burger": 5.50,
    "Pasta": 7.00,
    "Salad": 4.00,
    "Sushi": 10.00
}


def generate_random_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


def select_food(food_item):
    global current_order
    current_order = food_item  


    selection_label.pack_forget()
    for button in food_buttons:
        button.pack_forget()

    
    quantity_label.pack(pady=10)
    quantity_spinbox.pack(pady=5)
    add_order_button.pack(pady=5) 
    finish_order_button.pack(pady=5)  
    back_button.pack(pady=5) 


def add_order():
    quantity = quantity_var.get()
    
    if current_order and quantity > 0:
        orders.append((current_order, quantity)) 
        update_receipt()
        reset_selection()
    else:
        messagebox.showwarning("Input Error", "Please select a valid food item and quantity.")


def update_receipt():
    receipt_text = "Your Order:\n\n"
    total_price = 0 
    for item, qty in orders:
        price = food_prices[item] * qty  
        total_price += price 
        receipt_text += f"{item} x {qty}  ${food_prices[item]:.2f} each: ${price:.2f}\n"
    
    if orders:
        receipt_text += f"\nTotal Price: ${total_price:.2f}\n"  
        receipt_text += f"Pick-up Code: {pick_up_code}\n"
    
    receipt_label.config(text=receipt_text)
    receipt_frame.pack(pady=20) 


def start_timer():
    global timer_running
    timer_running = True
    countdown(remaining_time)


def countdown(remaining_time):
    if remaining_time >= 0:
        receipt_label.config(text=f"Your Order:\n\n" + "\n".join([f"{item} x {qty}" for item, qty in orders]) + 
                             f"\n\nPick-up Code: {pick_up_code}\n" +
                             f"Total Price: ${sum(food_prices[item] * qty for item, qty in orders):.2f}\n" +
                             f"Time Remaining: {remaining_time} seconds")
        r.after(1000, countdown, remaining_time - 1)  
    else:
        order_expired()


def finish_order():
    global pick_up_code, remaining_time
    quantity = quantity_var.get()
    
    if current_order and quantity > 0:
        orders.append((current_order, quantity))  
        pick_up_code = generate_random_code()  
        update_receipt() 
        start_timer()  

        
        final_summary = "Final Order Summary:\n\n"
        total_price = 0 
        for item, qty in orders:
            price = food_prices[item] * qty  
            total_price += price  
            final_summary += f"{item} x {qty}  ${food_prices[item]:.2f} each: ${price:.2f}\n"
        final_summary += f"\nTotal Price: ${total_price:.2f}\n"
        final_summary += f"Pick-up Code: {pick_up_code}\n"

        messagebox.showinfo("Order Placed", final_summary)
    else:
        messagebox.showwarning("Input Error", "Please select a valid food item and quantity.")

   
    reset_selection()


def order_expired():
    global orders, pick_up_code, timer_running
    orders = []  
    pick_up_code = ""  
    timer_running = False 
    receipt_label.config(text="Your order has expired.")  


def reset_selection():
    global current_order
    current_order = None  

    quantity_label.pack_forget()
    quantity_spinbox.pack_forget()
    add_order_button.pack_forget() 
    finish_order_button.pack_forget()  
    back_button.pack_forget()

   
    selection_label.pack(pady=20)
    for button in food_buttons:
        button.pack(pady=5)


r = tk.Tk()
r.title("Food Selection System")
r.geometry("300x500")


selection_label = tk.Label(r, text="Please select a food item", font=("Arial", 14))
selection_label.pack(pady=20)


food_items = ["Pizza", "Burger", "Pasta", "Salad", "Sushi"]


food_buttons = []
for food in food_items:
    food_button = tk.Button(r, text=food, command=lambda f=food: select_food(f))
    food_buttons.append(food_button)
    food_button.pack(pady=5)


quantity_label = tk.Label(r, text="Enter Quantity:")
quantity_var = tk.IntVar(value=1) 
quantity_spinbox = tk.Spinbox(r, from_=1, to=10, textvariable=quantity_var)


add_order_button = tk.Button(r, text="Add Another Order", command=add_order)


finish_order_button = tk.Button(r, text="Finish Order", command=finish_order)


back_button = tk.Button(r, text="Back", command=reset_selection)


receipt_frame = tk.Frame(r)
receipt_label = tk.Label(receipt_frame, text="", font=("Arial", 12))
receipt_label.pack(pady=20)


pick_up_code = ""


r.mainloop()
















