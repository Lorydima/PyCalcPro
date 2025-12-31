# PyCalc Pro V1.6 Source Code Date: 29/12/2025 Developer: LDM Dev. 

'''
PyCalc Pro V1.6 is a calculator with basic math operations, advanced math operations and a unit converter function for mass and length 

Git Hub Repository Link: "https://github.com/Lorydima/PyCalcPro"

PyCalc Pro Website link: "https://lorydima.github.io/PyCalcPro/"

Before you use this code read the license in the LICENSE.txt or on Git Hub Repository.
'''

# Library for app Dev.
import tkinter as tk
from tkinter import Tk, Canvas, Entry, StringVar, Toplevel, Label, Button, PhotoImage, Text, Scrollbar, Frame
import math
import os
import sys
import webbrowser
import json
from decimal import Decimal, InvalidOperation

# Logo Path
def get_logo_path():
    filename = 'PyCalc_Pro_V1.6_Logo.ico'
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return os.path.join(os.path.dirname(__file__), filename)

logo_path = get_logo_path()

# Fallback: prefer the V1.6 logo filename
if not os.path.exists(logo_path):
    logo_path = "PyCalc_Pro_V1.6_Logo.ico"

# Operations Memory File Path
def get_operations_file_path():
    filename = "PyCalcPro_V1.6_DATA.json"
    if hasattr(sys, 'frozen'):
        app_dir = os.path.dirname(sys.executable)
    else:
        app_dir = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(app_dir, filename)

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
        try:
            credit_window.iconbitmap(logo_path)
        except Exception:
            pass
    credit_label = Label(credit_window, text="PyCalc Pro Version 1.6\nDeveloper: LDM Dev", font=("Arial", 18), bg="#1E1E1E", fg="white")
    credit_label.pack(pady=10)
    try:
        if os.path.exists(logo_path):
            img = PhotoImage(file=logo_path)
            logo_lbl = Label(credit_window, image=img, bg="#1E1E1E")
            logo_lbl.image = img
            logo_lbl.pack(pady=5)
    except Exception:
        pass
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

# "License" Window Setup - read MIT license from file (optional display)
def open_license_window():
    license_window = Toplevel(window)
    license_window.title("License")
    license_window.geometry("900x600")
    license_window.configure(bg="#1E1E1E")
    license_window.resizable(True, True)

    if logo_path:
        try:
            license_window.iconbitmap(logo_path)
        except Exception:
            pass

    # Title Label
    license_label = Label(
        license_window,
        text="PyCalc Pro - MIT License",
        font=("Arial", 18, "bold"),
        bg="#1E1E1E",
        fg="white"
    )
    license_label.pack(pady=10)

    # Frame for text and scrollbar
    frame = Frame(license_window, bg="#1E1E1E")
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Scrollbar
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    # Text widget
    license_text_widget = Text(
        frame,
        bg="#2E2E2E",
        fg="white",
        font=("Arial", 11),
        wrap="word",
        yscrollcommand=scrollbar.set
    )
    license_text_widget.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=license_text_widget.yview)

    # Default MIT License (fallback)
    license_text = """MIT License

Copyright (c) 2025 LDM Dev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

    # Try to read LICENSE file from disk (preferred)
    try:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        candidates = [
            os.path.join(base_dir, 'LICENSE'),
            os.path.join(base_dir, 'LICENSE.txt'),
        ]

        for path in candidates:
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    license_text = f.read()
                break
    except Exception:
        pass

    license_text_widget.insert("1.0", license_text)
    license_text_widget.config(state="disabled")

# "Math Advanced Operations" Window Setup
def open_math_advanced_operations_window():
    def math_button_click(event):
        text = event.widget["text"]
        if text == "π":
            text = str(math.pi)
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
        try:
            math_adv_window.iconbitmap(logo_path)
        except Exception:
            pass
    
    Formulas = ["sqrt", "cos", "sin", "tan", "log", "π", "|x|", "x^x", "1/x"]
    for i, func in enumerate(Formulas):
        row, col = divmod(i, 3)
        button = Button(math_adv_window, text=func, font=("Arial", 12), bg="#FF0000", fg="white", width=10)
        button.grid(row=row, column=col, padx=10, pady=5)
        button.bind("<Button-1>", math_button_click)

# "Unit Converter" Window Setup
def open_unit_converter_window():
    def convert_units():
        raw = entry_value.get().strip()
        raw = raw.replace(',', '.')
        value = float(raw) if raw != '' else 0.0
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
        try:
            unit_conv_window.iconbitmap(logo_path)
        except Exception:
            pass

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
        try:
            memory_window.iconbitmap(logo_path)
        except Exception:
            pass

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

# Main GUI Function
def main_GUI_Function():
    global window
    global input_var 

    window = Tk()
    window.geometry("327x710")
    window.configure(bg="#1E1E1E") 
    window.title("PyCalc Pro V1.6")
    if logo_path:
        try:
            window.iconbitmap(logo_path)
        except Exception:
            pass

    # Calculator Formulas

    # Evaluate Function - improved with Decimal precision and better error handling
    def evaluate_expression(expression):
        """
        Safely evaluate calculator expression with Decimal precision.
        - Prevents arbitrary code execution
        - Uses Decimal for precision (no floating-point artifacts)
        - Returns user-friendly error messages
        """
        try:
            expression = expression.strip()
            if not expression:
                return ""
            
            expression = expression.replace(',', '.')
            
            # Input validation: only allow safe characters
            allowed_chars = set('0123456789+-*/%().pi')
            if not all(c in allowed_chars or c.isspace() for c in expression.lower()):
                return "Error: Invalid characters in input"
            
            # Prevent multiple operations without operands
            if '++' in expression or '--' in expression or '**' in expression or '//' in expression:
                return "Error: Invalid expression"

            # Handle percentage operator
            if '%' in expression:
                for operator in ['+', '-', '*', '/']:
                    if operator in expression:
                        parts = expression.split(operator)
                        if len(parts) == 2:
                            left, right = parts
                            if '%' in right:
                                right_val = right.replace('%', '').strip()
                                try:
                                    left_decimal = Decimal(left.strip())
                                    right_decimal = Decimal(right_val)
                                    result = left_decimal * right_decimal / Decimal(100)
                                    expression = f"{left}{operator}{result}"
                                except (InvalidOperation, ValueError):
                                    return "Error: Invalid expression"
                        break

            # Replace pi with its Decimal value
            expression = expression.replace('pi', str(Decimal(str(math.pi))))

            # Define safe functions for evaluation
            safe_functions = {
                "abs": abs,
                "sqrt": lambda x: Decimal(str(math.sqrt(float(x)))),
                "cos": lambda x: Decimal(str(math.cos(math.radians(float(x))))),
                "sin": lambda x: Decimal(str(math.sin(math.radians(float(x))))),
                "tan": lambda x: Decimal(str(math.tan(math.radians(float(x))))),
                "log": lambda x: Decimal(str(math.log10(float(x)))),
                "ln": lambda x: Decimal(str(math.log(float(x)))),
            }
            
            # Evaluate with restricted namespace
            result = eval(expression, {"__builtins__": None}, safe_functions)
            
            # Convert result to Decimal if not already
            if not isinstance(result, Decimal):
                result = Decimal(str(result))
            
            # Format result: remove trailing zeros and unnecessary decimal point
            result_str = str(result)
            if '.' in result_str:
                result_str = result_str.rstrip('0').rstrip('.')
            
            save_operation(f"{expression} = {result_str}")
            return result_str
            
        except ZeroDivisionError:
            return "Error: Division by zero"
        except ValueError:
            return "Error: Invalid number format"
        except SyntaxError:
            return "Error: Invalid expression"
        except Exception as e:
            return f"Error: Invalid input"

    # Math base operations function
    def button_click(event):
        text = button_texts[event.widget.find_withtag("current")[0]]
        if text == "=":
            result = evaluate_expression(input_var.get())
            input_var.set(result)
        elif text == "CE":
            # CE = clear last entry (clear input field)
            input_var.set("")
        elif text == "C":
            # C = clear everything and reset to 0
            input_var.set("0")
            # Immediately clear the 0 after showing it briefly
            window.after(100, lambda: input_var.set("") if input_var.get() == "0" else None)
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
        # Don't interfere if user is typing in the entry field
        try:
            if window.focus_get() == entry:
                return None
        except (NameError, tk.TclError):
            pass

        ch = event.char
        allowed = '0123456789+-*/%().,'
        
        # Only allow safe characters, reject free-form text
        if ch and ch in allowed:
            input_var.set(input_var.get() + ch)
            return "break"

        if event.keysym == "Return":
            result = evaluate_expression(input_var.get())
            input_var.set(result)
            return "break"
        elif event.keysym == "BackSpace":
            input_var.set(input_var.get()[:-1])
            return "break"
        elif event.keysym == "Delete":
            input_var.set("")
            return "break"
        elif event.keysym == "Escape":
            window.destroy()
            return "break"

    # Windows Task Bar Logo
    if logo_path:
        try:
            window.iconbitmap(logo_path)
        except Exception:
            pass

    # Canvas Setup
    canvas = Canvas(
        window, bg="#1E1E1E", height=700, width=327, bd=0, highlightthickness=0, relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Input Area
    input_var = StringVar()
    entry = Entry(window, textvariable=input_var, font=("Arial", 20), justify='right', bd=10, bg="#1E1E1E", fg="white", insertbackground='white', insertwidth=2)
    entry.place(x=10, y=10, width=307, height=60)
    entry.bind('<Return>', lambda e: input_var.set(evaluate_expression(input_var.get())))

    # Create white line
    canvas.create_rectangle(
        0.0, 80.0, 327.0, 87.95859918062783, fill="#FFFFFF", outline=""
    )

    # Calculator Buttons - fixed for macOS label visibility
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
        # Operations buttons are red/white, number/text buttons are white/black
        is_operation = text in ["CE", "C", "%", "+", "-", "*", "/", "=", "Math Advanced operations", "Unit Converter", "Credit", "Operations Memory"]
        fill_color = "#FF0000" if is_operation else "#FFFFFF"
        text_color = "white" if is_operation else "#000000"
        
        rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="")
        button_texts[rect_id] = text
        
        text_id = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, fill=text_color, font=("Arial", 14, "normal"))
        canvas.tag_bind(rect_id, "<Button-1>", button_click)
        canvas.tag_bind(rect_id, "<Enter>", lambda e: canvas.config(cursor="hand2"))
        canvas.tag_bind(rect_id, "<Leave>", lambda e: canvas.config(cursor=""))

    # Window Loop
    window.bind("<Key>", key_input)
    window.resizable(False, False)
    window.mainloop()

# Start Function
if __name__ == "__main__":
    main_GUI_Function()
