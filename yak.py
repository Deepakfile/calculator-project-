from tkinter import *

def click_button(value):
    current = data.get()
    data.set(current + str(value))

def clear_display():
    data.set("")

def calculate():
    try:
        result = eval(data.get())
        data.set(result)
    except:
        data.set("Error")

root = Tk()
root.title("Calculator")
root.geometry("361x381+500+200")

data = StringVar()
display = Entry(root, textvariable=data, bd=29, justify="right", bg="powder blue", font=("Arial", 20))
display.grid(row=0, columnspan=4)

# Button layout
buttons = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['C', '0', '=', '/']
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == 'C':
            btn = Button(root, text=text, font=("Arial", 12, "bold"), bd=12, height=2, width=6, 
                        command=clear_display)
        elif text == '=':
            btn = Button(root, text=text, font=("Arial", 12, "bold"), bd=12, height=2, width=6, 
                        command=calculate)
        else:
            btn = Button(root, text=text, font=("Arial", 12, "bold"), bd=12, height=2, width=6, 
                        command=lambda value=text: click_button(value))
        btn.grid(row=i+1, column=j)

root.mainloop()