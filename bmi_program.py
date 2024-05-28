import tkinter
from tkinter import *
import os

def clear():
    os.system("clear")
    
def calculate():
    wright = int(t1.get("1.0","end-1c"))
    height = float(t2.get("1.0","end-1c"))
    bmi = wright / height**2
    
    l3 = Label(program, text=" ")
    if bmi <= 18.40:
        l3.after(6000, lambda: l3.destroy())
        l3 = Label(program, text="{:.2f} Underweight. Please eat something.".format(bmi), font=("tahoma",14,"normal"))
        l3.pack()
    elif bmi >= 18.50 and bmi <= 24.90:
        l3.after(6000, lambda: l3.destroy())
        l3 = Label(program, text="{:.2f} Normal weight. Very good!".format(bmi), font=("tahoma",14,"normal"))
        l3.pack()
    elif bmi >= 25.00 and bmi <= 39.90:
        l3.after(6000, lambda: l3.destroy())
        l3 = Label(program, text="{:.2f} Overweight. Please do sporting and walk free.".format(bmi), font=("tahoma",14,"normal"))
        l3.pack()
    elif bmi >= 40.0:
        l3.after(6000, lambda: l3.destroy())
        l3 = Label(program, text="{:.2f} WARNING! Obese. Please go to see your doctor.".format(bmi), font=("tahoma",14,"normal"))
        l3.pack()
           
    t1.delete("1.0","end-1c")
    t2.delete("1.0","end-1c")

def exited_program():
    program.destroy()
    print("Clicked button and exited the program.")

try:
    clear()
    program = Tk()
    program.title("BMI Calculator")
    program.geometry('450x300')

    satir_label = Label(program, text="\n")
    satir_label.pack()

    l1 = Label(program, text="Enter Your Wright(kg)", font=("tahoma",15,"normal"))
    l1.pack()

    t1 = Text(program, width=13, height=2)
    t1.pack()

    l2 = Label(program, text="Enter Your Height(cm)",font=("tahoma",15,"normal"))
    l2.pack()

    t2 = Text(program, width=13, height=2)
    t2.pack()

    btn_calculate = Button(program, text="Calculate", font=("tahoma",15,"normal"), command=calculate)
    btn_calculate.pack()

    btn_close = Button(program, text="Quit", fg="white", bg="dark red", font=("tahoma",15,"normal"), command=exited_program)
    btn_close.pack()

    program.mainloop()

except:
    print("There was an error. Please try again.")
