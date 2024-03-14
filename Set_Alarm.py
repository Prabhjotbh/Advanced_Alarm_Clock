import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import customtkinter as ctk
from customtkinter import *
import numpy
import time
import winsound

def create():
    global clock_label
    clock_label=CTkLabel(frame,text="",font=("Helvetica",56))
    clock_label.place(relx=0.5,rely=0.5,anchor=CENTER)
    update_time()
    add_button=CTkButton(frame,text="Add Alarm",width=20,command=create_alarm)
    add_button.grid(row=0,column=1)
def update_time():
    global clock_label
    current_time=time.strftime("%H:%M:%S")
    clock_label.configure(text=current_time)
    root.after(1000,update_time)
def create_alarm():
    root2=ctk.CTk()
    root2.title("SMART ALARM CLOCK")
    root2.geometry("400x200")
    frame2=ctk.CTkFrame(master=root2)
    frame2.pack(pady=20,padx=20,fill="both",expand=True)    
    label_head=CTkLabel(frame2,text="SET ALARM")
    label_head.grid(row=0,column=1)

    lbl1= CTkLabel(frame2,text="Alarm time-")
    lbl1.grid(row=1,column=0,padx=10,pady=10)

    global entry1 
    entry1 = CTkEntry(frame2,width=100)
    entry1.grid(row=1,column=2)

    lbl2= CTkLabel(frame2,text="Display during alarm-")
    lbl2.grid(row=2,column=0,padx=10,pady=10)

    global entry2 
    entry2 = CTkEntry(frame2,width=100)
    entry2.grid(row=2,column=2)

    button1=CTkButton(frame2,text="Add alarm",width=10,command=submit)
    button1.grid(row=4,column=1)

    global lbl3
    lbl3=CTkLabel(frame2,text="")
    lbl3.grid(row=4,column=0)
    root2.mainloop()

def msg():
    global entry1,lbl3
    alarmtime=entry1.get()
    lbl3.configure(text="Time to get up....")
    messagebox.showinfo("Time",f"ALarm time-{alarmtime}")

def submit():
    global entry1,entry2,lbl3
    alarmtime=entry1.get()
    msg()
    ctime=time.strftime("%H:%M")
    print(f"ALarm time-{alarmtime}")
    while alarmtime!=ctime:
        ctime=time.strftime("%H:%M")
        time.sleep(1)
    if alarmtime==ctime:
        print("Playing sounds..")
        winsound.PlaySound("*",winsound.SND_ASYNC)
        lbl3.configure(text="Playing Sounds...")
        messagebox.showinfo("Message",f"Msg-{entry2.get()}")    
#main

root=ctk.CTk()
root.title("CLOCK")
root.geometry("400x400")
frame=ctk.CTkFrame(root)
frame.pack(pady=20,padx=20,fill="both",expand=True)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

create()
root.mainloop()