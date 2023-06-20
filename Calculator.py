from tkinter import *

root = Tk()
root.title("Calculator")

output_frame = Frame(root, height=50, width=380, bg="white")
output_frame.pack(side=TOP)
digit_frame = Frame(root, width=380, bg="white")
digit_frame.pack(side=BOTTOM)

output = Label(output_frame, text="0", font=("Arial", 20), width=20, anchor="e", height=2)

#adding functions to buttons
def clear():
    output.config(text="0")
    output.update()

def entry(btn_text):
    if output.cget("text") == "0":
        output.config(text=btn_text)
    elif btn_text in '+-*/' and output.cget("text")[-1] in '+-*/':
        new_text = output.cget("text")[:-1] + btn_text
        output.config(text=new_text)
    else:
        output.config(text=output.cget("text") + btn_text)
    output.update()

def btn(char):
    entry(str(char))

def btn_equal():
    if output.cget("text")[-1] in '+-*/':
        pass
    else:
        output.config(text=str(eval(output.cget("text"))))
        output.update()


# Calculator button
btn_1 = Button(digit_frame, text="1", font=("Arial", 14), padx=40, pady=20, command=lambda: btn(1))
btn_2 = Button(digit_frame, text="2", font=("Arial", 14), padx=40, pady=20, command=lambda: btn(2))
btn_3 = Button(digit_frame, text="3", font=("Arial", 14), padx=40, pady=20, command=lambda: btn(3))
btn_4 = Button(digit_frame, text="4", font=("Arial", 14), padx=40, pady=20, command=lambda: btn(4))
btn_5 = Button(digit_frame, text="5", font=("Arial", 14), padx=40, pady=20, command=lambda: btn(5))
btn_6 = Button(digit_frame, text="6", font=("Arial", 14), padx=40, pady=20, command=lambda: btn(6))
btn_7 = Button(digit_frame, text="7", font=("Arial", 14), padx=40, pady=20, command=lambda: btn(7))
btn_8 = Button(digit_frame, text="8", font=("Arial", 14), padx=40, pady=20, command=lambda: btn(8))
btn_9 = Button(digit_frame, text="9", font=("Arial", 14), padx=40, pady=20, command=lambda: btn(9))
btn_0 = Button(digit_frame, text="0", font=("Arial", 14), padx=95, pady=20, command=lambda: btn(0))
btn_add = Button(digit_frame, text="+", font=("Arial", 14), padx=39, pady=60, command=lambda: btn('+'))
btn_sub = Button(digit_frame, text="-", font=("Arial", 14), padx=40, pady=20, command=lambda: btn('-'))
btn_mul = Button(digit_frame, text="*", font=("Arial", 14), padx=42, pady=20, command=lambda: btn('*'))
btn_div = Button(digit_frame, text="/", font=("Arial", 14), padx=42, pady=20, command=lambda: btn('/'))
btn_equal = Button(digit_frame, text="=", font=("Arial", 14), padx=39, pady=60, command=btn_equal)
btn_clear = Button(digit_frame, text="Clear", font=("Arial", 14), padx=20, pady=20, command=clear)
btn_quit = Button(digit_frame, text="Quit", font=("Arial", 14), padx=30, pady=20, command=root.quit)


# placing the buttons
output.grid(row=0, column=0, columnspan=4)
btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_0.grid(row=5, column=0, columnspan=2)
btn_add.grid(row=2, column=3, rowspan=2)
btn_sub.grid(row=1, column=3)
btn_mul.grid(row=1, column=2)
btn_div.grid(row=1, column=1)
btn_equal.grid(row=4, column=3, rowspan=2)
btn_clear.grid(row=5, column=2)
btn_quit.grid(row=1, column=0)


root.mainloop()
