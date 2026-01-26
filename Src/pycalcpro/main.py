# PyCalc Pro V1.7 Source Code Date: 26/01/2026 Developer: LDM Dev. 

'''
PyCalc Pro V1.7 is a calculator with basic math operations, advanced math operations and a unit converter function for mass and length 

Git Hub Repository Link: "https://github.com/Lorydima/PyCalcPro"

PyCalc Pro Website link: "https://lorydima.github.io/PyCalcPro/"

Before you use this code read the license in the LICENSE.txt or on Git Hub Repository.

If you discover a security vulnerability please read the file SECURITY.md on the Git Hub Repository.
'''

# Library for app Dev.
from tkinter import Tk, Canvas, Entry, StringVar, Toplevel, Label, Button, PhotoImage, Text, Scrollbar, Frame
from decimal import Decimal, InvalidOperation
import tkinter as tk
import math
import os
import sys
import webbrowser
import json

# Logo Path
def get_logo_path():
    """
    Get the path to the application logo file.
    - Handles PyInstaller bundled paths
    - Falls back to current directory if not found
    """
    filename = 'PyCalc_Pro_Logo.ico'
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return os.path.join(os.path.dirname(__file__), filename)

logo_path = get_logo_path()

# Fallback: prefer the logo filename
if not os.path.exists(logo_path):
    logo_path = "PyCalc_Pro_Logo.ico"

# Operations Memory File Path
def get_operations_file_path():
    """
    Get the path to the operations history JSON file.
    - Handles different environments (frozen, development)
    - Returns standardized file path
    """
    filename = "DATA.json"
    if hasattr(sys, 'frozen'):
        app_dir = os.path.dirname(sys.executable)
    else:
        app_dir = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(app_dir, filename)

operations_file_path = get_operations_file_path()

# Operations Memory Save Functions
def save_operation(operation):
    """
    Save a calculator operation to the operations history.
    - Appends operation to JSON file
    - Maintains last 10 operations
    - Handles file I/O errors gracefully
    """
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
    """
    Retrieve the last 10 operations from history.
    - Reads from JSON file
    - Returns empty list if file doesn't exist or is corrupted
    """
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
    """
    Convert mass between different units.
    - Supports: kg, g, mg, lb, oz, ton, tonne
    - Returns converted value as float
    """
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
    """
    Convert length between different units.
    - Supports: km, m, cm, mm, µm, in, ft, yd, mile
    - Returns converted value as float
    """
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
    """
    Open the credit/about window.
    - Displays application version and developer info
    - Provides links to website and GitHub
    - Shows license information
    """
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
    credit_label = Label(credit_window, text="PyCalc Pro Version 1.7\nDeveloper: LDM Dev", font=("Arial", 18), bg="#1E1E1E", fg="white")
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

# "License" Window Setup 
def open_license_window():
    """
    Open the license information window.
    - Displays MIT License text
    - Reads from LICENSE.txt if available
    - Shows default MIT license as fallback
    """
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

    # Default MIT License 
    license_text = """MIT License

Copyright (c) 2026 LDM Dev

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

    # Try to read LICENSE file from disk
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
    """
    Open the advanced math operations window.
    - Provides buttons for sqrt, sin, cos, tan, log, etc.
    - Inserts function calls into calculator input
    """
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
    """
    Open the unit converter window.
    - Converts between mass units (kg, g, mg, lb, oz, etc.)
    - Converts between length units (km, m, cm, mm, etc.)
    - Displays conversion result
    """
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
    """
    Open the operations memory window.
    - Displays the last 10 calculator operations
    - Shows each operation with its result
    """
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
    """
    Main GUI initialization and execution function.
    - Creates main calculator window
    - Initializes all UI components
    - Sets up event handlers
    - Starts main event loop
    """
    global window
    global input_var 

    window = Tk()
    window.geometry("327x710")
    window.configure(bg="#1E1E1E") 
    window.title("PyCalc Pro V1.7")
    if logo_path:
        try:
            window.iconbitmap(logo_path)
        except Exception:
            pass

    # Calculator Formulas

    # Evaluate Function
    def evaluate_expression(expression):
        """
        Safely evaluate calculator expression with Decimal precision.
        - Prevents arbitrary code execution
        - Uses Decimal for precision (no floating-point artifacts)
        - Returns user-friendly error messages
        - Saves operation to history
        """
        try:
            original_expression = expression  
            expression = expression.strip()
            if not expression:
                return ""
            
            expression = expression.replace(',', '.')
            original_expression = expression  
            
            allowed_chars = set('0123456789+-*/%().piabcgilnoqrstx^|')
            for c in expression.lower():
                if c not in allowed_chars and not c.isspace():
                    return "Error: Invalid characters in input"
            
            if '++' in expression or '--' in expression or '**' in expression or '//' in expression:
                return "Error: Invalid expression"

            expression = expression.replace('pi', str(Decimal(str(math.pi))))

            import re
            def convert_to_decimal(match):
                num_str = match.group(0)
                try:
                    Decimal(num_str)
                    return f"Decimal('{num_str}')"
                except:
                    return num_str
            
            expression = re.sub(r'\d+\.?\d*', convert_to_decimal, expression)

            if '%' in expression:
                for operator in ['+', '-', '*', '/']:
                    if operator in expression:
                        parts = expression.split(operator)
                        if len(parts) == 2:
                            left, right = parts
                            if '%' in right:
                                right_val = right.replace('%', '').strip()
                                try:
                                    result = eval(left, {"__builtins__": None, "Decimal": Decimal}) * eval(right_val, {"__builtins__": None, "Decimal": Decimal}) / Decimal(100)
                                    expression = f"({left}){operator}({result})"
                                except (InvalidOperation, ValueError):
                                    return "Error: Invalid expression"
                        break

            safe_namespace = {
                "Decimal": Decimal,
                "abs": abs,
                "sqrt": lambda x: Decimal(str(math.sqrt(float(x)))),
                "cos": lambda x: Decimal(str(math.cos(math.radians(float(x))))),
                "sin": lambda x: Decimal(str(math.sin(math.radians(float(x))))),
                "tan": lambda x: Decimal(str(math.tan(math.radians(float(x))))),
                "log": lambda x: Decimal(str(math.log10(float(x)))),
                "ln": lambda x: Decimal(str(math.log(float(x)))),
            }
            
            result = eval(expression, {"__builtins__": None}, safe_namespace)
            
            if not isinstance(result, Decimal):
                result = Decimal(str(result))
            
            result_str = str(result)
            if '.' in result_str:
                result_str = result_str.rstrip('0').rstrip('.')
            
            save_operation(f"{original_expression} = {result_str}")
            return result_str
            
        except ZeroDivisionError:
            return "Error: Division by zero"
        except ValueError:
            return "Error: Invalid number format"
        except SyntaxError:
            return "Error: Invalid expression"
        except TypeError:
            return "Error: Invalid input"
        except Exception as e:
            return "Error: Invalid input"

    # Math base operations function
    def button_click(event):
        """
        Handle calculator button click events.
        - Processes number and operation buttons
        - Opens feature windows
        - Updates input display
        """
        text = button_texts[event.widget.find_withtag("current")[0]]
        if text == "=":
            result = evaluate_expression(input_var.get())
            if result is not None:
                input_var.set(result)
        elif text == "C":
            input_var.set(input_var.get()[:-1])
        elif text == "CE":
            input_var.set("")
        elif text == "Credit":
            try:
                open_credit_window()
            except Exception as e:
                pass
        elif text == "Unit Converter":
            try:
                open_unit_converter_window()
            except Exception as e:
                pass
        elif text == "Math Advanced operations":
            try:
                open_math_advanced_operations_window()
            except Exception as e:
                pass
        elif text == "Operations Memory":
            try:
                open_operations_memory_window()
            except Exception as e:
                pass
        else:
            input_var.set(input_var.get() + text)

    # Keyboard input command function
    def key_input(event):
        """
        Handle keyboard input events.
        - Processes numeric and operator keys
        - Handles special keys (Return, BackSpace, Delete, Escape)
        - Validates input characters
        """
        try:
            if window.focus_get() == entry:
                return None
        except (NameError, tk.TclError):
            pass

        ch = event.char
        allowed = '0123456789+-*/%().,'

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
        is_operation = text in ["CE", "C", "%", "+", "-", "*", "/", "="]
        is_feature_button = text in ["Math Advanced operations", "Unit Converter", "Credit", "Operations Memory"]
        
        if is_operation:
            fill_color = "#FF0000"
            text_color = "white"
        elif is_feature_button:
            fill_color = "#FF0000"
            text_color = "white"
        else:
            fill_color = "#FFFFFF"
            text_color = "#000000"
        
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
