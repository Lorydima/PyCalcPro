# PyCalc Pro V1.4  Source Code Date: 23/06/2025 Developer: LDM Dev. 

'''
PyCalc Pro V1.4 is a calculator with basic math operations, advanced math operations and a unit converter function for mass and length 

Git Hub Repository Link: "https://github.com/Lorydima/PyCalcPro"

PyCalc Pro Website link: "https://lorydima.github.io/PyCalcPro/"
'''
# Library for app Dev.
from tkinter import Tk, Canvas, Entry, StringVar, Toplevel, Label, Button
import math
import os
import sys
import webbrowser
import json

# Logo Path
def get_logo_path():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, 'PyCalc_Pro_V1.4_Logo.ico')
    else:
        return os.path.join(os.path.dirname(__file__), 'PyCalc_Pro_V1.4_Logo.ico')

logo_path = get_logo_path()

if not os.path.exists(logo_path):
    logo_path = "PyCalc_Pro_V1.4_Logo.ico"    

# Operations Memory File Path
def get_operations_file_path():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, "PyCalcPro_V1.4_DATA.json")
    else:
        return os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "PyCalcPro_V1.4_DATA.json")

operations_file_path = get_operations_file_path()

# Operations Memory Save Functions
def save_operation(operation):
    try:
        if os.path.exists(operations_file_path):
            with open(operations_file_path, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {"operations": []}
        else:
            data = {"operations": []}

        data["operations"].append(operation)
        data["operations"] = data["operations"][-10:]

        with open(operations_file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving operation: {e}")

def get_operations():
    try:
        if os.path.exists(operations_file_path):
            with open(operations_file_path, "r") as file:
                try:
                    data = json.load(file)
                    return data.get("operations", [])
                except json.JSONDecodeError:
                    return []
        return []
    except Exception as e:
        print(f"Error reading operations: {e}")
        return []

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

# Length
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
    credit_window.geometry("300x250")
    credit_window.configure(bg="#1E1E1E")
    credit_window.resizable(False, False)
    if logo_path:
        credit_window.iconbitmap(logo_path)
    credit_label = Label(credit_window, text="PyCalc Pro Version 1.4\nDeveloper: LDM Dev", font=("Arial", 18), bg="#1E1E1E", fg="white")
    credit_label.pack(pady=10)
    PyCalcPro_Website_button = Button(credit_window, text="PyCalc Pro Website", font=("Arial", 12), bg="#FF0000", fg="white", command=lambda: webbrowser.open("https://lorydima.github.io/PyCalcPro/"))
    github_button = Button(credit_window, text="PyCalc Pro Git Hub Repository", font=("Arial", 12), bg="#FF0000", fg="white", command=lambda: webbrowser.open("https://github.com/Lorydima/PyCalcPro"))
    license_button = Button(
        credit_window,
        text="Read License",
        font=("Arial", 12),
        bg="#FF0000",
        fg="white",
        command=open_license_window
    )
    github_button.pack(pady=10)
    PyCalcPro_Website_button.pack(pady=10)
    license_button.pack(pady=10)

# "License" Window Setup
def open_license_window():
    license_window = Toplevel(window)
    license_window.title("License")
    license_window.geometry("800x400")
    license_window.configure(bg="#1E1E1E")
    license_window.resizable(False, False)
    
    if logo_path:
        license_window.iconbitmap(logo_path)
        
    # Title Label
    license_label = Label(license_window, text="PyCalc Pro Version 1.4 License", font=("Arial", 18), bg="#1E1E1E", fg="white")
    license_label.pack(pady=10)

    # License Text
    license_text = """Thank you for downloading PyCalc Pro V1.4. Before using the software, 
please take a moment to review the terms of use outlined below. 
Your compliance with these terms ensures the responsible and appropriate use of this application.

TERMS OF USE:

- By software we mean the entire program folder that was downloaded. 
  So the EXE file, DATA.json file and the .ico logo file.
- You can freely download and use this application.
- You can view the source code on Git Hub for educational or personal purposes.
- It is not permitted to republish either the application or the source code, 
  in any form or for any purpose, without explicit written permission from me.
- The software is provided 'as is', without any warranties of any kind.

Terms of use update date: 02/04/2025

Thank You again from LDM Dev.❤️
"""
    license_text_label = Label(license_window, text=license_text, font=("Arial", 12), bg="#1E1E1E", fg="white", justify="left")
    license_text_label.pack(padx=10, pady=10)

# "Math Advanced Operations" Window Setup
def open_math_advanced_operations_window():
    def math_button_click(event):
        text = event.widget["text"]
        if text == "π":
            text = "3.14"  
        elif text == "|x|":
            text = "abs("
        elif text == "x^x":
            text = "**"
        elif text in ["sqrt", "cos", "sin", "tan", "log"]:
            text += "("
        input_var.set(input_var.get() + text)

    math_adv_window = Toplevel(window)
    math_adv_window.title("Math Advanced operations")
    math_adv_window.geometry("360x150")
    math_adv_window.configure(bg="#1E1E1E")
    math_adv_window.resizable(False, False)
    if logo_path:
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
            conversion_result.set("Category not available")
            return
        conversion_result.set(f"{value} {initial_unit} = {result:.2f} {final_unit}")

    unit_conv_window = Toplevel(window)
    unit_conv_window.title("Unit Converter")
    unit_conv_window.geometry("300x400")
    unit_conv_window.configure(bg="#1E1E1E")
    unit_conv_window.resizable(False, False)
    if logo_path:
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

# "Operations Memory" Window Setup
def open_operations_memory_window():
    memory_window = Toplevel(window)
    memory_window.title("Operations Memory")
    memory_window.geometry("300x400")
    memory_window.configure(bg="#1E1E1E")
    memory_window.resizable(False, False)
    if logo_path:
        memory_window.iconbitmap(logo_path)

    operations = get_operations()

    Label(memory_window, text="Last 10 Operations", font=("Arial", 14), bg="#1E1E1E", fg="white").pack(pady=10)
    for operation in operations:
        Label(
            memory_window,
            text=operation,
            font=("Arial", 12),
            bg="#1E1E1E",
            fg="white",
            anchor="center",
            justify="center"
        ).pack(fill="x", padx=10, pady=2)

def check_and_show_license():
    try:
        with open(operations_file_path, "r") as file:
            data = json.load(file)
            license_accepted = data.get("license_accepted", False)
    except FileNotFoundError:
        data = {"license_accepted": False}
        license_accepted = False

    if not license_accepted:
        def accept_license():
            data["license_accepted"] = True
            with open(operations_file_path, "w") as file:
                json.dump(data, file, indent=4)
            license_window.destroy()

        def on_close():
            sys.exit()

        license_window = Tk()
        license_window.geometry("700x500")
        license_window.configure(bg="#1E1E1E")  
        license_window.title("License Agreement")
        if logo_path:
            license_window.iconbitmap(logo_path)  
        license_window.protocol("WM_DELETE_WINDOW", on_close)

        Label(
            license_window,
            text="PyCalc Pro V1.4 LICENSE",
            font=("Arial", 20, "bold"),
            fg="white",  
            bg="#1E1E1E"
        ).pack(pady=10)

        license_text = """
Thank you for downloading PyCalc Pro V1.4. Before using the software, please take a moment to review the license outlined below. Your compliance with these terms ensures the responsible and appropriate use of this application.

LICENSE:
- By software we mean the entire program folder that was downloaded. 
  So the EXE file, DATA.json file and the .ico logo file.
- You can freely download and use this application.
- You can view the source code on GitHub for educational or personal purposes.
- It is not permitted to republish either the application or the source code, in any form or for any 
  purpose, without explicit written permission from me.
- The software is provided 'as is', without any warranties of any kind.

Terms of use update date: 02/04/2025

Thank You again from LDM Dev. ❤️
        """

        Label(
            license_window,
            text=license_text,
            font=("Arial", 12),
            fg="white",
            bg="#1E1E1E",
            justify="left",
            wraplength=650
        ).pack(pady=20, padx=20)

        accept_button = Button(
            license_window,
            text="Accept",
            bg="#16BD0A",  
            fg="white",
            font=("Arial", 14, "bold"),
            command=accept_license,
            relief="flat",
            activebackground="#16BD0A",
            activeforeground="white"
        )
        accept_button.pack(pady=20, ipadx=20, ipady=10)

        license_window.resizable(False, False)
        license_window.mainloop()

# Main GUI Function
def main_GUI_Function():
    global window
    global input_var 
    check_and_show_license()

    window = Tk()
    window.geometry("327x710")
    window.configure(bg="#1E1E1E") 
    window.title("PyCalc Pro V1.4")
    if logo_path:
        window.iconbitmap(logo_path)

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

            advanced_functions = {
                "abs": abs,
                "sqrt": math.sqrt,
                "cos": lambda x: math.cos(math.radians(x)),  
                "sin": lambda x: math.sin(math.radians(x)),  
                "tan": lambda x: math.tan(math.radians(x)),  
                "log": math.log,
                "pi": math.pi
            }

            result = str(eval(expression, {"__builtins__": None}, advanced_functions))
            
            save_operation(f"{expression} = {result}")
            
            return result
        except Exception as e:
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
        elif text == "Operations Memory":
            open_operations_memory_window()
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
    if logo_path:
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
        ("Unit Converter", 17, 565, 152, 618), ("Credit", 165, 565, 300, 618), ("Operations Memory", 17, 640, 300, 693)
    ]
    button_texts = {}

    for (text, x1, y1, x2, y2) in buttons:
        fill_color = "#FF0000" if text in ["CE", "C", "%", "+", "-", "*", "/", "=", "Math Advanced operations", "Unit Converter", "Credit", "Operations Memory"] else "white"
        text_color = "white" if fill_color == "#FF0000" else "black"
        rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="")
        button_texts[rect_id] = text
        text_id = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, fill=text_color, font=("Arial", 15 if text == "" else 14))
        canvas.tag_bind(rect_id, "<Button-1>", button_click)
        canvas.tag_bind(text_id, "<Button-1>", button_click)
        canvas.tag_bind(rect_id, "<Enter>", lambda e: canvas.config(cursor="hand2"))
        canvas.tag_bind(rect_id, "<Leave>", lambda e: canvas.config(cursor=""))

    # Window Loop
    window.bind("<Key>", key_input)
    window.resizable(False, False)
    window.mainloop()

# Start Function
if __name__ == "__main__":
    main_GUI_Function()