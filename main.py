import tkinter as tk
import animation as an
import sys
from collections import deque
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from PIL import ImageTk,Image

import barber_shop
sys.path.insert(0, 'assets/')

BG = '#b4cffa'

class GUI(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        #keep track of how many windows are on the screen
        self.count = 0

        #keep track of customer number
        self.customer_count = 1
        self.waiting_queue = deque()

        #init barber to sleeping state
        self.action=tk.StringVar()
        self.action.set("Sleeping")

        #text variable for waiting queue
        self.waiting_q = tk.StringVar()
        
        #call the function to update every second
        self.update()

        #update the waiting queue regardless of barber actions
        self.update_queue()

        #update the waiting room
        self.update_waiting_room()
        
        #title
        title = tk.Label(root,text='The Sleeping Barber', font='arial 25 bold',bg=BG).place(relx=0.17,rely=0.05)

        #input prompt
        input_prompt = tk.Label(root,text='How many chairs in the waiting room?',font='arial 15 bold',bg=BG).place(relx=0.12,rely=0.25)

        #input field
        self.num_chairs = tk.StringVar()
        large_font = ('Arial',20)
        input_field = tk.Entry(root,width=20,textvariable=self.num_chairs,font=large_font).place(relx=0.18,rely=0.35)

        #submit button
        output_button = tk.Button(root,text='Start Simulation',height=3,width=20,font='Arial 12 bold',command=self.start_simulation).place(relx=0.28,rely=0.50)

        #load and resize images we need for simulation

        #haircut gif
        self.cutting  = (Image.open("cut.gif"))
        self.cutting  = self.cutting.resize((400,400))
        self.cutting_image = ImageTk.PhotoImage(self.cutting)

        #sleeping gif
        self.sleep  = (Image.open("sleep.gif"))
        self.sleep  = self.sleep.resize((400,400))
        self.sleep_image = ImageTk.PhotoImage(self.sleep)

        #waiting room images
        self.zero =(Image.open("0.png"))
        self.zero  = self.zero.resize((400,400))
        self.zero_cus= ImageTk.PhotoImage(self.zero)

        self.one =(Image.open("1.png"))
        self.one  = self.zero.resize((400,400))
        self.one_cus= ImageTk.PhotoImage(self.one)

        self.two =(Image.open("2.png"))
        self.two  = self.two.resize((400,400))
        self.two_cus= ImageTk.PhotoImage(self.two)

        self.three =(Image.open("3.png"))
        self.three  = self.three.resize((400,400))
        self.three_cus= ImageTk.PhotoImage(self.three)

        self.four =(Image.open("4.png"))
        self.four  = self.three.resize((400,400))
        self.four_cus= ImageTk.PhotoImage(self.four)

        self.five =(Image.open("5.png"))
        self.five  = self.five.resize((400,400))
        self.five_cus= ImageTk.PhotoImage(self.five)
        
        
    def start_simulation(self):
        #validate input
        if(not self.num_chairs.get().isdecimal()):
            messagebox.showerror('Error','Please enter an integer')
            return
        else:
            barber_shop.make_barbershop(self)

    
    #Add a customer to the waiting queue if there is a chair left
    def add_customer(self):
        if len(self.waiting_queue)<int(self.num_chairs.get()):
            self.waiting_queue.append(str("Customer ")+str(self.customer_count))
            self.customer_count = self.customer_count + 1
            
        else:
            print("chairs full -> customer left")
    
    def update(self):
        try:
            self.sleeping.place_forget()
            self.cutting_hair.place_forget()
            
        except:
            pass
        #If we should sleep -> set action to sleep and immediately update in case a new customer came in
        if len(self.waiting_queue)==0:
            self.action.set("The barber is sleeping")
            try:
                try:
                    self.sleeping=an.ImageLabel(self.window)
                    self.sleeping.place(relx=0.07,rely=0.20)
                    self.sleeping.load('sleep.gif')
                except:
                    self.sleeping=an.ImageLabel(self.window)
                    self.sleeping.place(relx=0.07,rely=0.20)
                    self.sleeping.load('sleep.gif')
            except:
                pass
            root.after(1000,self.update)
        #otherwise, take the next customer in line -> delay this update by 10 secondsm, we will be cutting hair then
        else:
            this_customer = self.waiting_queue.popleft()

            try:
                self.cutting_hair=an.ImageLabel(self.window)
                self.cutting_hair.place(relx=0.07,rely=0.20)
                self.cutting_hair.load('cut.gif')
            except:
                self.cutting_hair=an.ImageLabel(self.window)
                self.cutting_hair.place(relx=0.07,rely=0.20)
                self.cutting_hair.load('cut.gif')
                
            self.action.set("The barber is cutting the hair of "+str(this_customer))
            
            root.after(5000,self.update)
        
    def update_queue(self):
        sb = ""
        for customer in self.waiting_queue:
            sb = sb + customer + " "
        self.waiting_q.set(sb)
        root.after(100,self.update_queue)
        
    def update_waiting_room(self):
        try:
            if(len(self.waiting_queue))==0:
                self.waiting=an.ImageLabel(self.window)
                self.waiting.place(relx=0.50,rely=0.20)
                self.waiting.load('0.png')
                            
            elif(len(self.waiting_queue))==1:
                self.waiting=an.ImageLabel(self.window)
                self.waiting.place(relx=0.50,rely=0.20)
                self.waiting.load('1.png')
                            
            elif(len(self.waiting_queue))==2:
                self.waiting=an.ImageLabel(self.window)
                self.waiting.place(relx=0.50,rely=0.20)
                self.waiting.load('2.png')
                            
            elif(len(self.waiting_queue))==3:
                self.waiting=an.ImageLabel(self.window)
                self.waiting.place(relx=0.50,rely=0.20)
                self.waiting.load('3.png')
                            
            elif(len(self.waiting_queue))==4:
                self.waiting=an.ImageLabel(self.window)
                self.waiting.place(relx=0.50,rely=0.20)
                self.waiting.load('4.png')
                            
            elif(len(self.waiting_queue))==5:
                self.waiting=an.ImageLabel(self.window)
                self.waiting.place(relx=0.50,rely=0.20)
                self.waiting.load('5.png')
        except:
            pass

        root.after(100,self.update_waiting_room)
        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("The Sleeping Barber")
    root.resizable(width=False, height=False)
    root.geometry('500x500')
    root.config(bg=BG)
    my_gui = GUI(root)
    root.mainloop()
    
