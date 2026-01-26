"""
PyCalc Pro - UI Module

This module contains all UI window definitions and components.
"""

import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry, StringVar, PhotoImage, Text, Scrollbar, Frame
import math
import os
import webbrowser

from .assets import logo_path
from .operations import convert_mass, convert_length
from .storage import get_operations


def open_credit_window(window):
    """Open the credit/about window."""
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
    
    credit_label = Label(credit_window, text="PyCalc Pro Version 1.7\nDeveloper: LDM Dev", 
                        font=("Arial", 18), bg="#1E1E1E", fg="white")
    credit_label.pack(pady=10)
    
    try:
        if os.path.exists(logo_path):
            img = PhotoImage(file=logo_path)
            logo_lbl = Label(credit_window, image=img, bg="#1E1E1E")
            logo_lbl.image = img
            logo_lbl.pack(pady=5)
    except Exception:
        pass
    
    PyCalcPro_Website_button = Button(credit_window, text="PyCalc Pro Website", font=("Arial", 12), 
                                     bg="#FF0000", fg="white", 
                                     command=lambda: webbrowser.open("https://lorydima.github.io/PyCalcPro/"))
    github_button = Button(credit_window, text="PyCalc Pro Git Hub Repository", font=("Arial", 12), 
                          bg="#FF0000", fg="white", 
                          command=lambda: webbrowser.open("https://github.com/Lorydima/PyCalcPro"))
    license_button = Button(credit_window, text="Read License", font=("Arial", 12), 
                           bg="#FF0000", fg="white", command=lambda: open_license_window(window))
    
    github_button.pack(pady=10)
    PyCalcPro_Website_button.pack(pady=10)
    license_button.pack(pady=10)


def open_license_window(window):
    """Open the license window."""
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
    license_label = Label(license_window, text="PyCalc Pro - MIT License",
                         font=("Arial", 18, "bold"), bg="#1E1E1E", fg="white")
    license_label.pack(pady=10)

    # Frame for text and scrollbar
    frame = Frame(license_window, bg="#1E1E1E")
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Scrollbar
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    # Text widget
    license_text_widget = Text(frame, bg="#2E2E2E", fg="white", font=("Arial", 11),
                              wrap="word", yscrollcommand=scrollbar.set)
    license_text_widget.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=license_text_widget.yview)

    # Default MIT License (fallback)
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

    # Try to read LICENSE file from disk (preferred)
    try:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
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


def open_math_advanced_operations_window(window, input_var):
    """Open the math advanced operations window."""
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
        button = Button(math_adv_window, text=func, font=("Arial", 12), 
                       bg="#FF0000", fg="white", width=10)
        button.grid(row=row, column=col, padx=10, pady=5)
        button.bind("<Button-1>", math_button_click)


def open_unit_converter_window(window):
    """Open the unit converter window."""
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

    Label(unit_conv_window, text="Select one of this category: \n mass or length", 
          font=("Arial", 12), bg="#1E1E1E", fg="white").pack(pady=5)
    unit_category = Entry(unit_conv_window, font=("Arial", 12))
    unit_category.pack(pady=5)

    Label(unit_conv_window, text="Entry Value:", font=("Arial", 12), 
          bg="#1E1E1E", fg="white").pack(pady=5)
    entry_value = Entry(unit_conv_window, font=("Arial", 12))
    entry_value.pack(pady=5)

    Label(unit_conv_window, text="Entry initial unit (Symbol):", font=("Arial", 12), 
          bg="#1E1E1E", fg="white").pack(pady=5)
    entry_unit_start = Entry(unit_conv_window, font=("Arial", 12))
    entry_unit_start.pack(pady=5)

    Label(unit_conv_window, text="Entry final unit (Symbol):", font=("Arial", 12), 
          bg="#1E1E1E", fg="white").pack(pady=5)
    entry_unit_final = Entry(unit_conv_window, font=("Arial", 12))
    entry_unit_final.pack(pady=5)

    conversion_result = StringVar()
    conversion_result.set("0.00")
    Label(unit_conv_window, textvariable=conversion_result, font=("Arial", 12), 
          bg="#1E1E1E", fg="white").pack(pady=10)
    convert_button = Button(unit_conv_window, text="Convert", font=("Arial", 12), 
                           bg="#FF0000", fg="white", command=convert_units)
    convert_button.pack(pady=10)


def open_operations_memory_window(window):
    """Open the operations memory window."""
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

    Label(memory_window, text="Last 10 Operations", font=("Arial", 14), 
          bg="#1E1E1E", fg="white").pack(pady=10)
    for operation in operations:
        Label(memory_window, text=operation, font=("Arial", 12), bg="#1E1E1E", 
              fg="white", anchor="center", justify="center").pack(fill="x", padx=10, pady=2)
