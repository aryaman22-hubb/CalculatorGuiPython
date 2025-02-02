from tkinter import *

# Evaluate the expression
def expression_evaluation():
    try:
        result = str(eval(entry.get()))
        label_result.config(text="Result: " + result)
    except Exception:
        label_result.config(text="Error")


# Update the input field when a button is clicked
def button_click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + value)

# Clear's the input field
def clear_input():
    entry.delete(0, END)

# Create the main window(here screen)
screen = Tk()
screen.title("STANDARD CALCULATOR")
screen.geometry("280x380")
screen.resizable(False, False)
screen.configure(background="white")


# Input field
entry = Entry(screen, width=20, font=("Verdana", 14), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4)

label_result = Label(screen, text="Result: ", font=("Verdana", 14), bg="white", fg="black")
label_result.grid(row=1, column=0, columnspan=4)

# Buttons Structure (contains all the buttons used in the calculator)
button_7 = Button(screen, text='7', bg='#00a65a', fg='white', width=5, height=2, command=lambda: button_click('7'))
button_7.grid(row=2, column=0)
button_7.configure(font=('Verdana', 14))

button_8 = Button(screen, text='8', bg='#00a65a', fg='white', width=5, height=2, command=lambda: button_click('8'))
button_8.grid(row=2, column=1)
button_8.configure(font=('Verdana', 14))

button_9 = Button(screen, text='9', bg='#00a65a', fg='white', width=5, height=2, command=lambda: button_click('9'))
button_9.grid(row=2, column=2)
button_9.configure(font=('Verdana', 14))

button_divide = Button(screen, text='/', bg='#00a65a', fg='white', width=5, height=2, command=lambda: button_click('/'))
button_divide.grid(row=2, column=3)
button_divide.configure(font=('Verdana', 14))

button_4 = Button(screen, text='4', bg='#00a65a', fg='white', width=5, height=2, command=lambda: button_click('4'))
button_4.grid(row=3, column=0)
button_4.configure(font=('Verdana', 14))

button_5 = Button(screen, text='5', bg='#00a65a', fg='white', width=5, height=2, command=lambda: button_click('5'))
button_5.grid(row=3, column=1)
button_5.configure(font=('Verdana', 14))

button_6 = Button(screen, text='6', bg='#00a65a', fg='white', width=5, height=2, command=lambda: button_click('6'))
button_6.grid(row=3, column=2)
button_6.configure(font=('Verdana', 14))

button_multiply = Button(screen, text='x', bg='#00a65a', fg='white', width=5, height=2, command=lambda: button_click('*'))
button_multiply.grid(row=3, column=3)
button_multiply.configure(font=('Verdana', 14))

button_1 = Button(screen, text='1', bg='#00a65a', fg='white', width=5, height=2, command=lambda: button_click('1'))
button_1.grid(row=4, column=0)
button_1.configure(font=('Verdana', 14))

button_2 = Button(screen, text='2', bg='#00a65a', fg='white', width=5, height=2, command=lambda: button_click('2'))
button_2.grid(row=4, column=1)
button_2.configure(font=('Verdana', 14))

button_3 = Button(screen, text='3', bg='#00a65a', fg='white', width=5, height=2, command=lambda: button_click('3'))
button_3.grid(row=4, column=2)
button_3.configure(font=('Verdana', 14))

button_minus = Button(screen, text='-', bg='#00a65a', fg='white', width=5, height=2, command=lambda: button_click('-'))
button_minus.grid(row=4, column=3)
button_minus.configure(font=('Verdana', 14))

button_0 = Button(screen, text='0', bg='#00a65a', fg='white', width=5, height=2, command=lambda: button_click('0'))
button_0.grid(row=5, column=0)
button_0.configure(font=('Verdana', 14))

button_dot = Button(screen, text='.', bg='#00a65a', fg='white', width=5, height=2, command=lambda: button_click('.'))
button_dot.grid(row=5, column=1)
button_dot.configure(font=('Verdana', 14))

button_plus = Button(screen, text='+', bg='#00a65a', fg='white', width=5, height=2, command=lambda: button_click('+'))
button_plus.grid(row=5, column=2)
button_plus.configure(font=('Verdana', 14))

button_equal = Button(screen, text='=', bg='#00a65a', fg='white', width=5, height=2, command=expression_evaluation)
button_equal.grid(row=5, column=3)
button_equal.configure(font=('Verdana', 14))

button_clear = Button(screen, text='C', bg='#00a65a', fg='white', width=5, height=2, command=clear_input)
button_clear.grid(row=6, column=0)
button_clear.configure(font=('Verdana', 14))

# In order to run the main loop
screen.mainloop() 
