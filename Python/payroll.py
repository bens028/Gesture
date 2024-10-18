import tkinter as tk
from tkinter import messagebox


p = {
    's': 2.50,
    'm': 3.00,
    'l': 3.50
}

class C:
    def __init__(self, r):
        self.r = r
        self.r.title("Coffee Payroll System")
        self.r.geometry("500x600")  
        self.r.configure(bg="#f9f9f9")  

        self.mf = tk.Frame(self.r, bg="#ffffff", padx=20, pady=20)
        self.mf.pack(fill=tk.BOTH, expand=True)

      
        self.t = tk.Label(self.mf, text="Morron 5", font=("Arial", 24, "bold"), bg="#ffffff")
        self.t.pack(pady=20)

     
        self.lb = tk.Button(self.mf, text="Login", command=self.l, width=20, bg="#4A90E2", fg="white", font=("Arial", 14))
        self.lb.pack(pady=10)

       
        self.bb = tk.Button(self.mf, text="Buy Coffee", command=self.o, width=20, bg="#4CAF50", fg="white", font=("Arial", 14))
        self.bb.pack(pady=10)

        self.of = tk.Frame(self.r, bg="#e0f7fa", padx=20, pady=20)
        self.of.pack(fill=tk.BOTH, expand=True)
        self.of.pack_forget()

        
        self.cl = tk.Label(self.of, text="Enter Your Name:", bg="#e0f7fa", font=("Arial", 14))
        self.cl.pack(pady=5)

        self.ce = tk.Entry(self.of, font=("Arial", 14))
        self.ce.pack(pady=5)

       
        self.co = tk.Label(self.of, text="Enter Quantity:", bg="#e0f7fa", font=("Arial", 14))
        self.co.pack(pady=5)

        self.ce_qty = tk.Entry(self.of, font=("Arial", 14))
        self.ce_qty.pack(pady=5)

      
        self.cs = tk.Label(self.of, text="Select Coffee Size:", bg="#e0f7fa", font=("Arial", 14))
        self.cs.pack(pady=5)

        self.sv = tk.StringVar(value='s')
        self.ss = tk.Radiobutton(self.of, text='Small ($2.50)', variable=self.sv, value='s', bg="#e0f7fa", font=("Arial", 12))
        self.sm = tk.Radiobutton(self.of, text='Medium ($3.00)', variable=self.sv, value='m', bg="#e0f7fa", font=("Arial", 12))
        self.sl = tk.Radiobutton(self.of, text='Large ($3.50)', variable=self.sv, value='l', bg="#e0f7fa", font=("Arial", 12))

        self.ss.pack()
        self.sm.pack()
        self.sl.pack()

        
        self.sb = tk.Button(self.of, text="Submit Order", command=self.ct, width=20, bg="#FF9800", fg="white", font=("Arial", 15))
        self.sb.pack(pady=20)

        
        self.bb = tk.Button(self.of, text="Back to Main Menu", command=self.m, width=20, bg="#f44336", fg="white", font=("Arial", 15))
        self.bb.pack(pady=10)

      
        self.tl = tk.Label(self.of, text="", bg="#e0f7fa", font=("Arial", 17))
        self.tl.pack(pady=5)

    def l(self):
        messagebox.showinfo("Login", "Login functionality is not implemented.")

    def o(self):
        self.mf.pack_forget()
        self.of.pack(fill=tk.BOTH, expand=True)

    def m(self):
        self.of.pack_forget()
        self.mf.pack(fill=tk.BOTH, expand=True)

    def ct(self):
        n = self.ce.get()
        qty = self.ce_qty.get()
        s = self.sv.get()

        if not n:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return

        if not qty.isdigit() or int(qty) <= 0:
            messagebox.showwarning("Input Error", "Please enter a valid quantity.")
            return

        qty = int(qty)
        t = p[s] * qty
        self.tl.config(text=f"{n}, your total is: P{t:.2f}")

if __name__ == "__main__":
    r = tk.Tk()
    a = C(r)
    r.mainloop()







