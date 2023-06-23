import tkinter as tk

LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
WHITE = "#FFFFFF"
OFF_WHITE = "#F8FAFF"
LIGHT_BLUE = "#CCEDFF"

DIGIT_FONT_STYLE = ("Arial", 24, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

root = tk.Tk()
root.title("Calculator")
root.geometry("375x667")
root.resizable(0,0)

output_frame = tk.Frame(root, height=221, bg=LIGHT_GRAY)
output_frame.pack(expand=True, fill="both")
digit_frame = tk.Frame(root)
digit_frame.pack(expand=True, fill="both")

digit_frame.rowconfigure(0, weight=1)
for x in range(1,5):
    digit_frame.rowconfigure(x, weight=1)
    digit_frame.columnconfigure(x, weight=1)

#output expressions
total_expression = "0"
current_expression = "0"

total_label = tk.Label(output_frame, text=total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
total_label.pack(expand=True, fill="both")

current_label = tk.Label(output_frame, text=total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
current_label.pack(expand=True, fill="both")

def update_total_label():
    expression = total_expression

    for operator,symbol in operations.items():
        expression = expression.replace(operator, f' {symbol} ')

    total_label.config(text=expression)

def update_current_label():
    current_label.config(text=current_expression[:11])

def add_to_expression(value):
    global current_expression
    if current_expression != '0':
        current_expression += str(value)
    else:
        current_expression = str(value)
    update_current_label()

def append_operator(operator):
    global current_expression, total_expression

    current_expression += operator
    if total_expression != '0':
        total_expression += current_expression
    else:
        total_expression = current_expression

    current_expression = "0"
    update_total_label()
    update_current_label()

def clear():
    global total_expression, current_expression
    current_expression = "0"
    total_expression = "0"
    update_current_label()
    update_total_label()

def evaluate():
    global total_expression, current_expression
    total_expression += current_expression
    update_total_label()

    try:
        current_expression = str(eval(total_expression))

        total_expression = "0"

    except Exception as e:
        current_expression = "Error"
    finally:
        update_current_label()

digits = {
    7:(1,1), 8:(1,2), 9:(1,3),
    4:(2,1), 5:(2,2), 6:(2,3),
    1:(3,1), 2:(3,2), 3:(3,3),
    0:(4,1), '.':(4,2)
}

operations = {
    "/": "/", 
    "*": "x",
    "-": "-",
    "+": "+"
}

for digit, grid_value in digits.items():
    button = tk.Button(digit_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=0, command=lambda x=digit:add_to_expression(x))
    button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

i=0

for operator, symbol in operations.items():
    button = tk.Button(digit_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda x=operator:append_operator(x))
    button.grid(row=i, column=4, sticky=tk.NSEW)
    i += 1

clear = tk.Button(digit_frame, text='C', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=clear)
clear.grid(row=0, column=1, sticky=tk.NSEW, columnspan=3)

equal = tk.Button(digit_frame, text='=', bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=evaluate)
equal.grid(row=4, column=3, sticky=tk.NSEW, columnspan=2)

#binding keys
root.bind("<Return>", lambda event: evaluate())

for key in digits:
    root.bind(str(key), lambda event,digit=key: add_to_expression(digit))

for key in operations:
    root.bind(key, lambda event,operator=key: append_operator(operator))


root.mainloop()
