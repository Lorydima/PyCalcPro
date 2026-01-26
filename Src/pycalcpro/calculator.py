"""
PyCalc Pro - Main Calculator GUI Module

This module contains the main calculator GUI implementation.
"""

import tkinter as tk
from tkinter import Tk, Canvas, Entry, StringVar
import sys

from .assets import logo_path
from .operations import evaluate_expression
from .storage import save_operation
from .ui import (open_credit_window, open_unit_converter_window, 
                 open_math_advanced_operations_window, open_operations_memory_window)


def main_GUI_Function():
    """Main GUI function that creates and runs the calculator."""
    window = Tk()
    window.geometry("327x710")
    window.configure(bg="#1E1E1E") 
    window.title("PyCalc Pro V1.7")
    
    if logo_path:
        try:
            window.iconbitmap(logo_path)
        except Exception:
            pass

    input_var = StringVar()

    # Math base operations function
    def button_click(event):
        text = button_texts[event.widget.find_withtag("current")[0]]
        if text == "=":
            result = evaluate_expression(input_var.get(), save_operation)
            if result is not None:
                input_var.set(result)
        elif text == "C":
            # C = clear last entry (remove last character)
            input_var.set(input_var.get()[:-1])
        elif text == "CE":
            # CE = clear entry (reset calculator)
            input_var.set("")
        elif text == "Credit":
            try:
                open_credit_window(window)
            except Exception:
                pass
        elif text == "Unit Converter":
            try:
                open_unit_converter_window(window)
            except Exception:
                pass
        elif text == "Math Advanced operations":
            try:
                open_math_advanced_operations_window(window, input_var)
            except Exception:
                pass
        elif text == "Operations Memory":
            try:
                open_operations_memory_window(window)
            except Exception:
                pass
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
            result = evaluate_expression(input_var.get(), save_operation)
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

    # Canvas Setup
    canvas = Canvas(
        window, bg="#1E1E1E", height=700, width=327, bd=0, 
        highlightthickness=0, relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Input Area
    entry = Entry(window, textvariable=input_var, font=("Arial", 20), 
                 justify='right', bd=10, bg="#1E1E1E", fg="white", 
                 insertbackground='white', insertwidth=2)
    entry.place(x=10, y=10, width=307, height=60)
    entry.bind('<Return>', lambda e: input_var.set(evaluate_expression(input_var.get(), save_operation)))

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
        # Operations buttons are red, number/text buttons are white
        is_operation = text in ["CE", "C", "%", "+", "-", "*", "/", "="]
        is_feature_button = text in ["Math Advanced operations", "Unit Converter", "Credit", "Operations Memory"]
        
        if is_operation:
            fill_color = "#FF0000"
            text_color = "white"
        elif is_feature_button:
            fill_color = "#FF0000"
            text_color = "white"  # Ensure white text on red background for macOS compatibility
        else:
            fill_color = "#FFFFFF"
            text_color = "#000000"
        
        rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="")
        button_texts[rect_id] = text
        
        text_id = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, 
                                     fill=text_color, font=("Arial", 14, "normal"))
        canvas.tag_bind(rect_id, "<Button-1>", button_click)
        canvas.tag_bind(rect_id, "<Enter>", lambda e: canvas.config(cursor="hand2"))
        canvas.tag_bind(rect_id, "<Leave>", lambda e: canvas.config(cursor=""))

    # Window Loop
    window.bind("<Key>", key_input)
    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    main_GUI_Function()
