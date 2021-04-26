import tkinter as tk
import animation as an
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from PIL import ImageTk,Image 

BG = '#b4cffa'

def make_barbershop(self):
    
    
    #render new window
    self.count = self.count + 1
    self.window=tk.Toplevel(self)
    self.window.geometry("1100x650")
    self.window.config(bg='#b4cffa')
    self.window.resizable(width=False, height=False)
    
    root = self.window
    
    add_customer = tk.Button(root,text='Add Customer',height=3,width=40,font='Arial 12 bold',command=self.add_customer).place(relx=0.30,rely=0.87)
    action_label= tk.Label(root,textvariable=self.action,font='arial 22 bold',bg=BG).place(relx=0.28,rely=0.02)

    waiting_label= tk.Label(root,textvariable=self.waiting_q,font='arial 22 bold',bg=BG).place(relx=0.28,rely=0.10)
    
    
    
    
    

        
