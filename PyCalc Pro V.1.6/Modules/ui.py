"""UI components and window management."""

import webbrowser
import tkinter as tk
from tkinter import Tk, Canvas, Entry, StringVar, Toplevel, Label, Button, PhotoImage, Text, Scrollbar

from .operations import evaluate_expression, convert_mass, convert_length
from .state import CalculatorState
from .utils import get_logo_path, load_license_text


class Calculator:
    """Main calculator UI class."""
    
    def __init__(self):
        """Initialize the calculator application."""
        self.window = None
        self.input_var = None
        self.entry = None
        self.canvas = None
        self.button_texts = {}
        self.logo_path = get_logo_path()
        self.state = None
    
    def run(self):
        """Start the calculator application."""
        self.window = Tk()
        self.window.geometry("327x710")
        self.window.configure(bg="#1E1E1E")
        self.window.title("PyCalc Pro V1.6")
        
        if self.logo_path:
            try:
                self.window.iconbitmap(self.logo_path)
            except Exception:
                pass
        
        # Initialize state management
        from .utils import get_data_file_path
        self.state = CalculatorState(get_data_file_path())
        
        # Setup UI
        self._setup_canvas()
        self._setup_input_area()
        self._setup_buttons()
        self._setup_keyboard()
        
        self.window.resizable(False, False)
        self.window.mainloop()
    
    def _setup_canvas(self):
        """Set up the main canvas."""
        self.canvas = Canvas(
            self.window, bg="#1E1E1E", height=700, width=327,
            bd=0, highlightthickness=0, relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        
        # White separator line
        self.canvas.create_rectangle(
            0.0, 80.0, 327.0, 87.95859918062783, fill="#FFFFFF", outline=""
        )
    
    def _setup_input_area(self):
        """Set up the input field."""
        self.input_var = StringVar()
        self.entry = Entry(
            self.window, textvariable=self.input_var, font=("Arial", 20),
            justify='right', bd=10, bg="#1E1E1E", fg="white",
            insertbackground='white', insertwidth=2
        )
        self.entry.place(x=10, y=10, width=307, height=60)
        self.entry.bind('<Return>', self._on_entry_return)
    
    def _on_entry_return(self, event):
        """Handle Return key in input field."""
        expression = self.input_var.get()
        result = evaluate_expression(expression)
        self.input_var.set(result)
        if result and not result.startswith("Error"):
            self.state.save_operation(f"{expression} = {result}")
        return "break"
    
    def _setup_buttons(self):
        """Set up calculator buttons."""
        buttons = [
            ("CE", 17, 115, 78, 168), ("C", 91, 115, 152, 168),
            ("%", 165, 115, 226, 168), ("+", 239, 115, 300, 168),
            ("-", 239, 190, 300, 243), ("*", 239, 265, 300, 318),
            ("/", 239, 340, 300, 393), ("=", 239, 415, 300, 468),
            ("0", 17, 415, 226, 468), ("1", 17, 340, 78, 393),
            ("2", 91, 340, 152, 393), ("3", 165, 340, 226, 393),
            ("4", 17, 265, 78, 318), ("5", 91, 265, 152, 318),
            ("6", 165, 265, 226, 318), ("7", 17, 190, 78, 243),
            ("8", 91, 190, 152, 243), ("9", 165, 190, 226, 243),
            ("Math Advanced operations", 17, 490, 300, 543),
            ("Unit Converter", 17, 565, 152, 618),
            ("Credit", 165, 565, 300, 618),
            ("Operations Memory", 17, 640, 300, 693)
        ]
        
        for (text, x1, y1, x2, y2) in buttons:
            is_operation = text in [
                "CE", "C", "%", "+", "-", "*", "/", "=",
                "Math Advanced operations", "Unit Converter",
                "Credit", "Operations Memory"
            ]
            fill_color = "#FF0000" if is_operation else "#FFFFFF"
            text_color = "white" if is_operation else "#000000"
            
            rect_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="")
            self.button_texts[rect_id] = text
            
            self.canvas.create_text(
                (x1 + x2) / 2, (y1 + y2) / 2, text=text,
                fill=text_color, font=("Arial", 14, "normal")
            )
            
            self.canvas.tag_bind(rect_id, "<Button-1>", self._on_button_click)
            self.canvas.tag_bind(rect_id, "<Enter>", lambda e: self.canvas.config(cursor="hand2"))
            self.canvas.tag_bind(rect_id, "<Leave>", lambda e: self.canvas.config(cursor=""))
    
    def _on_button_click(self, event):
        """Handle button clicks."""
        text = self.button_texts[self.canvas.find_withtag("current")[0]]
        
        if text == "=":
            result = evaluate_expression(self.input_var.get())
            self.input_var.set(result)
            if result and not result.startswith("Error"):
                self.state.save_operation(f"{self.input_var.get()} = {result}")
        elif text == "CE":
            self.input_var.set("")
        elif text == "C":
            self.input_var.set("0")
            self.window.after(100, lambda: self.input_var.set("") if self.input_var.get() == "0" else None)
        elif text == "Credit":
            self._open_credit_window()
        elif text == "Unit Converter":
            self._open_unit_converter_window()
        elif text == "Math Advanced operations":
            self._open_math_advanced_window()
        elif text == "Operations Memory":
            self._open_operations_memory_window()
        else:
            self.input_var.set(self.input_var.get() + text)
    
    def _setup_keyboard(self):
        """Set up keyboard input handling."""
        self.window.bind("<Key>", self._on_key_press)
    
    def _on_key_press(self, event):
        """Handle keyboard input."""
        try:
            if self.window.focus_get() == self.entry:
                return None
        except (NameError, tk.TclError):
            pass
        
        ch = event.char
        allowed = '0123456789+-*/%().,'
        
        if ch and ch in allowed:
            self.input_var.set(self.input_var.get() + ch)
            return "break"
        
        if event.keysym == "Return":
            expression = self.input_var.get()
            result = evaluate_expression(expression)
            self.input_var.set(result)
            if result and not result.startswith("Error"):
                self.state.save_operation(f"{expression} = {result}")
            return "break"
        elif event.keysym == "BackSpace":
            self.input_var.set(self.input_var.get()[:-1])
            return "break"
        elif event.keysym == "Delete":
            self.input_var.set("")
            return "break"
        elif event.keysym == "Escape":
            self.window.destroy()
            return "break"
    
    def _open_credit_window(self):
        """Open the credits window."""
        credit_window = Toplevel(self.window)
        credit_window.title("Credit")
        credit_window.geometry("300x250")
        credit_window.configure(bg="#1E1E1E")
        credit_window.resizable(False, False)
        
        if self.logo_path:
            try:
                credit_window.iconbitmap(self.logo_path)
            except Exception:
                pass
        
        credit_label = Label(
            credit_window,
            text="PyCalc Pro Version 1.6\nDeveloper: LDM Dev",
            font=("Arial", 18), bg="#1E1E1E", fg="white"
        )
        credit_label.pack(pady=10)
        
        try:
            if self.logo_path:
                img = PhotoImage(file=self.logo_path)
                logo_lbl = Label(credit_window, image=img, bg="#1E1E1E")
                logo_lbl.image = img
                logo_lbl.pack(pady=5)
        except Exception:
            pass
        
        website_btn = Button(
            credit_window, text="PyCalc Pro Website",
            font=("Arial", 12), bg="#FF0000", fg="white",
            command=lambda: webbrowser.open("https://lorydima.github.io/PyCalcPro/")
        )
        website_btn.pack(pady=10)
        
        github_btn = Button(
            credit_window, text="PyCalc Pro Git Hub Repository",
            font=("Arial", 12), bg="#FF0000", fg="white",
            command=lambda: webbrowser.open("https://github.com/Lorydima/PyCalcPro")
        )
        github_btn.pack(pady=10)
        
        license_btn = Button(
            credit_window, text="Read License",
            font=("Arial", 12), bg="#FF0000", fg="white",
            command=self._open_license_window
        )
        license_btn.pack(pady=10)
    
    def _open_license_window(self):
        """Open the license window."""
        license_window = Toplevel(self.window)
        license_window.title("License")
        license_window.geometry("900x600")
        license_window.configure(bg="#1E1E1E")
        license_window.resizable(True, True)
        
        if self.logo_path:
            try:
                license_window.iconbitmap(self.logo_path)
            except Exception:
                pass
        
        title = Label(
            license_window, text="PyCalc Pro - MIT License",
            font=("Arial", 18, "bold"), bg="#1E1E1E", fg="white"
        )
        title.pack(pady=10)
        
        frame = Label(license_window, bg="#1E1E1E")
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")
        
        text_widget = Text(
            frame, bg="#2E2E2E", fg="white", font=("Arial", 11),
            wrap="word", yscrollcommand=scrollbar.set
        )
        text_widget.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=text_widget.yview)
        
        license_text = load_license_text()
        text_widget.insert("1.0", license_text)
        text_widget.config(state="disabled")
    
    def _open_math_advanced_window(self):
        """Open the advanced math operations window."""
        math_window = Toplevel(self.window)
        math_window.title("Math Advanced operations")
        math_window.geometry("360x150")
        math_window.configure(bg="#1E1E1E")
        math_window.resizable(False, False)
        
        if self.logo_path:
            try:
                math_window.iconbitmap(self.logo_path)
            except Exception:
                pass
        
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
            self.input_var.set(self.input_var.get() + text)
        
        formulas = ["sqrt", "cos", "sin", "tan", "log", "π", "|x|", "x^x", "1/x"]
        for i, func in enumerate(formulas):
            row, col = divmod(i, 3)
            btn = Button(
                math_window, text=func, font=("Arial", 12),
                bg="#FF0000", fg="white", width=10
            )
            btn.grid(row=row, column=col, padx=10, pady=5)
            btn.bind("<Button-1>", math_button_click)
    
    def _open_unit_converter_window(self):
        """Open the unit converter window."""
        converter_window = Toplevel(self.window)
        converter_window.title("Unit Converter")
        converter_window.geometry("300x400")
        converter_window.configure(bg="#1E1E1E")
        converter_window.resizable(False, False)
        
        if self.logo_path:
            try:
                converter_window.iconbitmap(self.logo_path)
            except Exception:
                pass
        
        Label(
            converter_window,
            text="Select one of this category: \n mass or length",
            font=("Arial", 12), bg="#1E1E1E", fg="white"
        ).pack(pady=5)
        
        unit_category = Entry(converter_window, font=("Arial", 12))
        unit_category.pack(pady=5)
        
        Label(
            converter_window, text="Entry Value:",
            font=("Arial", 12), bg="#1E1E1E", fg="white"
        ).pack(pady=5)
        entry_value = Entry(converter_window, font=("Arial", 12))
        entry_value.pack(pady=5)
        
        Label(
            converter_window, text="Entry initial unit (Symbol):",
            font=("Arial", 12), bg="#1E1E1E", fg="white"
        ).pack(pady=5)
        entry_unit_start = Entry(converter_window, font=("Arial", 12))
        entry_unit_start.pack(pady=5)
        
        Label(
            converter_window, text="Entry final unit (Symbol):",
            font=("Arial", 12), bg="#1E1E1E", fg="white"
        ).pack(pady=5)
        entry_unit_final = Entry(converter_window, font=("Arial", 12))
        entry_unit_final.pack(pady=5)
        
        conversion_result = StringVar()
        conversion_result.set("0.00")
        
        result_label = Label(
            converter_window, textvariable=conversion_result,
            font=("Arial", 12), bg="#1E1E1E", fg="white"
        )
        result_label.pack(pady=10)
        
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
            
            if result is not None:
                conversion_result.set(f"{value} {initial_unit} = {result:.2f} {final_unit}")
        
        convert_btn = Button(
            converter_window, text="Convert",
            font=("Arial", 12), bg="#FF0000", fg="white",
            command=convert_units
        )
        convert_btn.pack(pady=10)
    
    def _open_operations_memory_window(self):
        """Open the operations memory window."""
        memory_window = Toplevel(self.window)
        memory_window.title("Operations Memory")
        memory_window.geometry("300x400")
        memory_window.configure(bg="#1E1E1E")
        memory_window.resizable(False, False)
        
        if self.logo_path:
            try:
                memory_window.iconbitmap(self.logo_path)
            except Exception:
                pass
        
        Label(
            memory_window, text="Last 10 Operations",
            font=("Arial", 14), bg="#1E1E1E", fg="white"
        ).pack(pady=10)
        
        operations = self.state.get_operations()
        for operation in operations:
            Label(
                memory_window, text=operation,
                font=("Arial", 12), bg="#1E1E1E", fg="white",
                anchor="center", justify="center"
            ).pack(fill="x", padx=10, pady=2)
