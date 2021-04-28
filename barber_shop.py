import tkinter as tk
import animation as an
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from PIL import ImageTk,Image 

BG = '#b4cffa'
PK = '#f7cfff'
def make_barbershop(self):
    
    
    #render new window
    self.count = self.count + 1
    self.window=tk.Toplevel(self)
    self.window.geometry("1100x650")
    self.window.config(bg='#b4cffa')
    self.window.resizable(width=False, height=False)
    
    root = self.window
    
    add_customer = tk.Button(root,text='Add Customer',height=2,width=40,font='Arial 12 bold',command=self.add_customer,bg=PK).place(relx=0.30,rely=0.91)
    action_label= tk.Label(root,textvariable=self.action,font='arial 22 bold',bg=BG).place(relx=0.28,rely=0.02)

    self.chairs_full = tk.Label(root,text='Chairs are full, the customer left.',font='Arial 22 bold',bg=BG,fg='red')
    #place(relx=0.28,rely=0.84)

    waiting_label= tk.Label(root,textvariable=self.waiting_q,font='arial 18 bold',bg=BG).place(relx=0.05,rely=0.10)
    
 
    
    
    

        
