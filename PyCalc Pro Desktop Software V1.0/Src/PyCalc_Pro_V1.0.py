# PyCalc Pro V1.0  Source Code Date: 22/01/2025 Developer: LDM Dev. 

'''
PyCalc Pro V1.0 is a calculator with basic math operations, advanced math operations and and a unit converter function for mass and length 

Git Hub Repository Link: "https://github.com/Lorydima/PyCalcPro"
'''
# Library for app Dev.
from tkinter import Tk, Canvas, Entry, StringVar, Toplevel, Label, Button
import math

# Logo Path
logo_path = 'PyCalc_Pro_V1.0_Logo.ico'

# Unit Converter Functions

# Mass
def convert_mass(value, initial_unit, final_unit):
    conversions = {
        'kg': 1,
        'g': 1000,
        'mg': 1e6,
        'lb': 2.20462,
        'oz': 35.274,
        'ton': 0.001,
        'tonne': 0.001
    }
    return value * (conversions[final_unit] / conversions[initial_unit])

# Lenght
def convert_length(value, initial_unit, final_unit):
    conversions = {
        'km': 0.001,
        'm': 1,
        'cm': 100,
        'mm': 1000,
        'µm': 1e6,
        'in': 39.3701,
        'ft': 3.28084,
        'yd': 1.09361,
        'mile': 0.000621371
    }
    return value * (conversions[final_unit] / conversions[initial_unit])

# Windows Setups Functions

# "Credit" Window Setup
def open_credit_window():
    credit_window = Toplevel(window)
    credit_window.title("Credit")
    credit_window.geometry("300x150")
    credit_window.configure(bg="#1E1E1E")
    credit_window.resizable(False, False)
    credit_window.iconbitmap(logo_path)
    credit_label = Label(credit_window, text="PyCalc Pro Version 1.0\nDeveloper: LDM Dev", font=("Arial", 18), bg="#1E1E1E", fg="white")
    credit_label.pack(pady=50)

# "Math Advanced Operations" Window Setup
def open_math_advanced_operations_window():
    def math_button_click(event):
        text = event.widget["text"]
        if text == "π":
            text = str(math.pi)
        elif text == "|x|":
            text = "abs()"
        elif text == "x^x":
            text = "x*x"
        elif text in ["sqrt", "cos", "sin", "tan", "log"]:
            text += "()"
        input_var.set(input_var.get() + text)

    math_adv_window = Toplevel(window)
    math_adv_window.title("Math Advanced operations")
    math_adv_window.geometry("360x150")
    math_adv_window.configure(bg="#1E1E1E")
    math_adv_window.resizable(False, False)
    math_adv_window.iconbitmap(logo_path)
    
    Formulas = ["sqrt", "cos", "sin", "tan", "log", "π", "|x|", "x^x", "1/x"]
    for i, func in enumerate(Formulas):
        row, col = divmod(i, 3)
        button = Button(math_adv_window, text=func, font=("Arial", 12), bg="#FF0000", fg="white", width=10)
        button.grid(row=row, column=col, padx=10, pady=5)
        button.bind("<Button-1>", math_button_click)

# "Unit Converter" Window Setup
def open_unit_converter_window():
    def convert_units():
        value = float(entry_value.get())
        category = unit_category.get().lower()
        initial_unit = entry_unit_start.get().lower()
        final_unit = entry_unit_final.get().lower()
        if category == 'mass':
            result = convert_mass(value, initial_unit, final_unit)
        elif category == 'length':
            result = convert_length(value, initial_unit, final_unit)
        else:
            conversion_result.set("Category not avaible")
            return
        conversion_result.set(f"{value} {initial_unit} = {result:.2f} {final_unit}")

    unit_conv_window = Toplevel(window)
    unit_conv_window.title("Unit Converter")
    unit_conv_window.geometry("300x400")
    unit_conv_window.configure(bg="#1E1E1E")
    unit_conv_window.resizable(False, False)
    unit_conv_window.iconbitmap(logo_path)

    Label(unit_conv_window, text="Select one of this category: \n mass or length", font=("Arial", 12), bg="#1E1E1E", fg="white").pack(pady=5)
    unit_category = Entry(unit_conv_window, font=("Arial", 12))
    unit_category.pack(pady=5)

    Label(unit_conv_window, text="Entry Value:", font=("Arial", 12), bg="#1E1E1E", fg="white").pack(pady=5)
    entry_value = Entry(unit_conv_window, font=("Arial", 12))
    entry_value.pack(pady=5)

    Label(unit_conv_window, text="Entry initial unit (Symbol):", font=("Arial", 12), bg="#1E1E1E", fg="white").pack(pady=5)
    entry_unit_start = Entry(unit_conv_window, font=("Arial", 12))
    entry_unit_start.pack(pady=5)

    Label(unit_conv_window, text="Entry final unit (Symbol):", font=("Arial", 12), bg="#1E1E1E", fg="white").pack(pady=5)
    entry_unit_final = Entry(unit_conv_window, font=("Arial", 12))
    entry_unit_final.pack(pady=5)

    conversion_result = StringVar()
    conversion_result.set("0.00")
    Label(unit_conv_window, textvariable=conversion_result, font=("Arial", 12), bg="#1E1E1E", fg="white").pack(pady=10)
    convert_button = Button(unit_conv_window, text="Convert", font=("Arial", 12), bg="#FF0000", fg="white", command=convert_units)
    convert_button.pack(pady=10)

# Window "Calculator" Setup
window = Tk()
window.geometry("327x650")
window.configure(bg="#FFFFFF")
window.title("PyCalc Pro V1.0")

# Calculator Formulas

# Evaluate Function
def evaluate_expression(expression):
    try:
        if '%' in expression:
            for operator in ['+', '-', '*', '/']:
                if operator in expression:
                    left, right = expression.split(operator)
                    if '%' in right:
                        right = right.replace('%', '')
                        right = f"({left} * {right} / 100)"
                        expression = f"{left}{operator}{right}"
                    break

        return str(eval(expression, {"__builtins__": None}, {"abs": abs, "sqrt": math.sqrt, "cos": math.cos, "sin": math.sin, "tan": math.tan, "log": math.log, "pi": math.pi}))
    except Exception or ValueError or SyntaxError as e:
        return f"Input Error: {e}"

# Math base operations function
def button_click(event):
    text = button_texts[event.widget.find_withtag("current")[0]]
    if text.isdigit():
        if not input_var.get().endswith(text):
            input_var.set(input_var.get() + text)
    elif text == "=":
        input_var.set(evaluate_expression(input_var.get()))
    elif text == "CE":
        input_var.set("")
    elif text == "C":
        input_var.set(input_var.get()[:-1])
    elif text == "Credit":
        open_credit_window()
    elif text == "Unit Converter":
        open_unit_converter_window()
    elif text == "Math Advanced operations":
        open_math_advanced_operations_window()
    else:
        input_var.set(input_var.get() + text)

# Keyboard input command function
def key_input(event):
    if event.char.isdigit() and not input_var.get().endswith(event.char):
        input_var.set(input_var.get() + event.char)
    elif event.char in "+-*/%" and not input_var.get().endswith(event.char):
        input_var.set(input_var.get() + event.char)
    elif event.keysym == "Return":
        input_var.set(evaluate_expression(input_var.get()))
    elif event.keysym == "BackSpace":
        input_var.set(input_var.get()[:-1])
    elif event.keysym == "Delete":
        input_var.set("")
    elif event.keysym == "Escape":
        window.destroy()
    return "break"

# Windows Task Bar Logo
window.iconbitmap(logo_path)

# Canvas Setup
canvas = Canvas(
    window, bg="#1E1E1E", height=700, width=327, bd=0, highlightthickness=0, relief="ridge"
)
canvas.place(x=0, y=0)

# Input Area
input_var = StringVar()
entry = Entry(window, textvar=input_var, font=("Arial", 20), justify='right', bd=10, bg="#1E1E1E", fg="white")
entry.place(x=10, y=10, width=307, height=60)

# Create white line
canvas.create_rectangle(
    0.0, 80.0, 327.0, 87.95859918062783, fill="#FFFFFF", outline=""
)

# Calculator Buttons
buttons = [
    ("CE", 17, 115, 78, 168), ("C", 91, 115, 152, 168), ("%", 165, 115, 226, 168), ("+", 239, 115, 300, 168),
    ("-", 239, 190, 300, 243), ("*", 239, 265, 300, 318), ("/", 239, 340, 300, 393), ("=", 239, 415, 300, 468),
    ("0", 17, 415, 226, 468), ("1", 17, 340, 78, 393), ("2", 91, 340, 152, 393), ("3", 165, 340, 226, 393),
    ("4", 17, 265, 78, 318), ("5", 91, 265, 152, 318), ("6", 165, 265, 226, 318), ("7", 17, 190, 78, 243),
    ("8", 91, 190, 152, 243), ("9", 165, 190, 226, 243), ("Math Advanced operations", 17, 490, 300, 543),
    ("Unit Converter", 17, 565, 152, 618), ("Credit", 165, 565, 300, 618)
]
button_texts = {}

for (text, x1, y1, x2, y2) in buttons:
    fill_color = "#FF0000" if text in ["CE", "C", "%", "+", "-", "*", "/", "=", "Math Advanced operations",  "Unit Converter", "Credit"] else  "white"
    text_color = "white" if fill_color == "#FF0000" else "black"
    rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="")
    button_texts[rect_id] = text
    canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, fill=text_color, font=("Arial", 15 if text == "" else 14))
    canvas.tag_bind(rect_id, "<Button-1>", button_click)
    canvas.tag_bind(rect_id, "<Enter>", lambda e: canvas.config(cursor="hand2"))
    canvas.tag_bind(rect_id, "<Leave>", lambda e: canvas.config(cursor=""))

# Window Loop
window.bind("<Key>", key_input)
window.resizable(False, False)
window.mainloop()
