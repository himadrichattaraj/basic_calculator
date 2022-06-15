from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equal():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Error")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Error")
        equation_text = ""

def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)

window = Tk()
window.title("Calculator")
window.geometry("350x425")
window.config(background="black")

equation_text = ""
equation_label = StringVar()

write_label = Label(window, textvariable=equation_label, font=("consolas", 40), bg="#1c1b1b", fg="white", width=11, height=1)
write_label.pack(padx=0, pady=10)

button_frame = Frame(window, bg="black")
button_frame.pack()

button1 = Button(button_frame, text=1, height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command= lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(button_frame, text=2, height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command= lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(button_frame, text=3, height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command= lambda: button_press(3))
button3.grid(row=0, column=2)

button_div = Button(button_frame, text="÷", height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command= lambda: button_press("/"))
button_div.grid(row=0, column=3)

button4 = Button(button_frame, text=4, height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command= lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(button_frame, text=5, height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command= lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(button_frame, text=6, height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command= lambda: button_press(6))
button6.grid(row=1, column=2)

button_mul = Button(button_frame, text="x", height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command= lambda: button_press("*"))
button_mul.grid(row=1, column=3)

button7 = Button(button_frame, text=7, height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command= lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(button_frame, text=8, height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command= lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(button_frame, text=9, height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command= lambda: button_press(9))
button9.grid(row=2, column=2)

button_pls = Button(button_frame, text="+", height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command= lambda: button_press("+"))
button_pls.grid(row=2, column=3)

button_dot = Button(button_frame, text=".", height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command= lambda: button_press("."))
button_dot.grid(row=3, column=0)

button0 = Button(button_frame, text=0, height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command= lambda: button_press(0))
button0.grid(row=3, column=1)

button_equal = Button(button_frame, text="=", height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command=equal)
button_equal.grid(row=3, column=2)

button_minus = Button(button_frame, text="-", height=0, width=3, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command= lambda: button_press("-"))
button_minus.grid(row=3, column=3)

button_cls = Button(button_frame, text="CLEAR", height=0, width=0, font=("consolas", 23),
                 bg="#1c1b1b", fg="white", activebackground="#2b2a2a", activeforeground="white",
                 command=clear)
button_cls.grid(row=4, column=1, columnspan=2)

window.mainloop()
