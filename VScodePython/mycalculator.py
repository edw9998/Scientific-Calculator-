from tkinter import *
import tkinter.messagebox as msb
from random import choice
import numpy as np
import matplotlib.pyplot as plt
import math
from feature import graph_feature 
from conversion import nums_conversion

# Set Up Main Window.
root = Tk()
root.geometry("630x502+0+0")
root.resizable(height = False, width = False)
root.title("My Application")
root.config(bg = "black")

# Create Menu Widget To Provide Access To Additional Features And 'Quit' Option.
# Feature 1 : Basic Trigonometric Graphs Visualization.
# Feature 2 : Number System Conversion(DEC, BIN, OCT, HEX).
Menu_Bar = Menu(root)
More_Menu = Menu(Menu_Bar, tearoff = 0)
More_Menu.add_command(label = 'Basic Trigonometric Graphs', command = lambda: graph_feature())
More_Menu.add_separator()
More_Menu.add_command(label = 'Number System Conversion', command = lambda: nums_conversion())
More_Menu.add_separator()
More_Menu.add_command(label = "Quit", command = root.quit)
More_Menu.add_separator()
Menu_Bar.add_cascade(label = 'More', menu = More_Menu)

# Create A Label As The Title Of The App.
L = Label(root, text = 'Scientific Calculator', font = ("Times New Roman", 40, "bold"), bg = 'gray', fg = 'gray10', width = 26, justify = CENTER)
L.place(x = -100, y = 0)

# Create An Entry As The Container Of Calculator Expression.
# Define A Control Variable For The Expression.
E_Var = StringVar()
E = Entry(root, width = 27, bg = 'gold', font = ("Times New Roman", 35, "bold"), justify = LEFT, textvariable = E_Var)
E.place(x = 0, y = 66)

# Create Calculator Operations.
class Operations:
    global E
    def __init__(self, opr = ''):
        self.length = len(E.get())
        self.operator = opr
        self.end = END

    def clear_entry(self):
        E.delete(0, self.end)

    def insert_operator(self):
        E.insert(self.length, self.operator)

    def absolute(self):
        # Always Remember To Convert Expression To Numeric Type Before Operating On Them !
        try:
            abs_val = float(E.get())
            abs_res = abs(abs_val)
            E.delete(0, self.end)
            if str(abs_res).endswith('.0'):
                E.insert(self.length, str(abs_res).replace(".0", " "))
            else:
                E.insert(self.length, str(abs_res))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Numerical Characters Only !")   

    def negative(self):
        try:
            neg_val = float(E.get())
            neg_res = -1 * neg_val
            E.delete(0, self.end)
            if str(neg_res).endswith('.0'):
                E.insert(0, str(neg_res).replace(".0", " "))
            elif str(neg_res).endswith('.0') == False:
                E.insert(0, str(neg_res))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Numerical Characters Only !")

    def ceil(self):
        try:
            ceil_val = float(E.get())
            ceil_res = np.ceil(ceil_val)
            E.delete(0, self.end)
            if isinstance(ceil_res , float):
                E.insert(0, str(ceil_res))
            else:
                pass
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Decimal Numbers Only !")

    def floor(self):
        try:
            floor_val = float(E.get())
            floor_res = np.floor(floor_val)
            E.delete(0, self.end)
            if isinstance(floor_res, float):
                E.insert(0, str(floor_res))
            else:
                pass
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Decimal Numbers Only !")

    def cbrt(self):
        try:
            cbrt_val = float(E.get())
            cbrt_res = np.cbrt(cbrt_val)
            E.delete(0, self.end)
            if str(cbrt_res).endswith('.0'):
                E.insert(0, str(cbrt_res).replace(".0", " "))
            elif isinstance(cbrt_res, float):
                E.insert(0, str(round(float(cbrt_res), 6)))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Numerical Characters Only !")

    def sqrt(self):
        try:
            sqrt_val = float(E.get())
            sqrt_res = np.sqrt(sqrt_val)
            E.delete(0, self.end)
            if str(sqrt_res).endswith('.0'):
                E.insert(0, str(sqrt_res).replace(".0", " ") + "," + " " + str(-1 * sqrt_res).replace(".0", " "))
            elif isinstance(sqrt_res, float):
                E.insert(0, str(round(float(sqrt_res), 6)))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Numerical Characters Only !")

    def log2(self):
        try:
            log2_val = float(E.get())
            log2_res = np.log2(log2_val)
            E.delete(0, self.end)
            if str(log2_res).endswith('.0'):
                E.insert(0, str(log2_res).replace(".0", " "))
            elif str(log2_res).endswith('.0') == False:
                E.insert(0, str(round(log2_res, 6)))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Numerical Characters Only !")

    def log10(self):
        try:
            log10_val = float(E.get())
            log10_res = np.log10(log10_val)
            E.delete(0, self.end)
            if str(log10_res).endswith('.0'):
                E.insert(0, str(log10_res).replace(".0", " "))
            elif str(log10_res).endswith('.0') == False:
                E.insert(0, str(round(log10_res, 6)))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Numerical Characters Only !")

    def factorial(self):
        try:
            factorial_val = int(E.get())
            factorial_res = np.math.factorial(factorial_val)
            E.delete(0, self.end)
            if isinstance(factorial_res, int):
                E.insert(0, str(factorial_res))
            else:
                E.insert(0, "Invalid Value : Not An Integer !")
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Integers Only !")

    def ln(self):
        try:
            ln_val = float(E.get())
            ln_res = np.log(ln_val)
            E.delete(0, self.end)
            if str(ln_res).endswith('.0'):
                E.insert(0, str(ln_res).replace(".0", " "))
            else:
                E.insert(0, str(ln_res))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Numerical Characters Only !")

    def exp(self):
        try:
            exp_val = float(E.get())
            exp_res = np.exp(exp_val)
            E.delete(0, self.end)
            if str(exp_res).endswith('.0'):
                E.insert(0, str(exp_res).replace(".0", " "))
            else:
                E.insert(0, str(exp_res))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Numerical Characters Only !")

    def sine(self):
        # Trigonometric Operators Require Radian Values.
        try:
            sine_val = float(E.get())
            sine_res = np.sin(math.radians(sine_val))
            E.delete(0, self.end)
            E.insert(0, str(sine_res))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Numerical Characters Only !")

    def cosine(self):
        try:
            cosine_val = float(E.get())
            cosine_res = np.cos(math.radians(cosine_val))
            E.delete(0, self.end)
            E.insert(0, str(cosine_res))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Numerical Characters Only !")

    def tangent(self):
        try:
            tan_val = float(E.get())
            tan_res = np.tan(math.radians(tan_val))
            E.delete(0, self.end)
            E.insert(0, str(tan_res))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Numerical Characters Only !")

    def csc(self):
        try:
            csc_val = float(E.get())
            csc_res = 1 / np.sin(math.radians(csc_val))
            E.delete(0, self.end)
            E.insert(0, str(csc_res))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Numerical Characters Only !")

    def sec(self):
        try:
            sec_val = float(E.get())
            sec_res = 1 / np.cos(math.radians(sec_val))
            E.delete(0, self.end)
            E.insert(0, str(sec_res))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Numerical Characters Only !")

    def cot(self):
        try:
            cot_val = float(E.get())
            cot_res = 1 / np.tan(math.radians(cot_val))
            E.delete(0, self.end)
            E.insert(0, str(cot_res))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Numerical Characters Only !")

    def arc_sin(self):
        try:
            arc_sin_val = float(E.get())
            arc_sin_res = math.asin(arc_sin_val)
            E.delete(0, self.end)
            E.insert(0, str(arc_sin_res))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Trigonometric Values (Between -1 And 1) Only !")

    def arc_cos(self):
        try:
            arc_cos_val = float(E.get())
            arc_cos_res = math.acos(arc_cos_val)
            E.delete(0, self.end)
            E.insert(0, str(arc_cos_res))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Trigonometric Values (Between -1 And 1) Only !")

    def arc_tan(self):
        try:
            arc_tan_val = float(E.get())
            arc_tan_res = math.atan(arc_tan_val)
            E.delete(0, self.end)
            E.insert(0, str(arc_tan_res))
        except Exception:
            msb.showinfo("Input Error Detected !", "Please Enter Trigonometric Values (Between -1 And 1) Only !")

    def equals(self):
        try:
            equation = compile(E.get(), "<string>", "eval")
            output = eval(equation)
            E.delete(0, self.end)
            E.insert(0, str(output))
        except Exception:
            msb.showinfo("An Error Occurred !", "Please Check Your Expression And Try Again.")

# Create Calculator Buttons.
# (X-Interval = 90, Y-Interval = 54)
# Buttons For The First Row.
# Create Higher Order Functions With Lambda For Each Button Command, To Prevent Direct Execution.
insert_random_int_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "Rand.", font = ("Times New Roman", 20, "bold"), activebackground = "green", relief = GROOVE , command = lambda: Operations(opr = str(choice([num for num in range(1, 100 + 1)]))).insert_operator())
insert_random_int_btn.place(x = 0, y = 123)

ceil_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "⌈x⌉", font = ("Times New Roman", 20, "bold"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).ceil())
ceil_btn.place(x = 90, y = 123)

floor_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "⌊x⌋", font = ("Times New Roman", 20, "bold"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).floor())
floor_btn.place(x = 90 * 2, y = 123)

mod_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "mod", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = '%').insert_operator())
mod_btn.place(x = 90 * 3, y = 123)

factorial_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "x!", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).factorial())
factorial_btn.place(x = 90 * 4, y = 123)

sin_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "sin(x)", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).sine())
sin_btn.place(x = 90 * 5, y = 123)

csc_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "csc(x)", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).csc())
csc_btn.place(x = 90 * 6, y = 123)

# Buttons For The Second Row.
abs_value_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "|x|", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).absolute())
abs_value_btn.place(x = 0, y = 123 + 54)

x_pow_y_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "x^y", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = '**').insert_operator())
x_pow_y_btn.place(x = 0 + 90, y = 123 + 54)

cbrt_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "3√x", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).cbrt())
cbrt_btn.place(x = 90 * 2, y = 123 + 54)

log_base2_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "log2(x)", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).log2())
log_base2_btn.place(x = 90 * 3, y = 123 + 54)

natural_log_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "ln(x)", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).ln())
natural_log_btn.place(x = 90 * 4, y = 123 + 54)

cos_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "cos(x)", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).cosine())
cos_btn.place(x = 90 * 5, y = 123 + 54)

sec_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "sec(x)", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).sec())
sec_btn.place(x = 90 * 6, y = 123 + 54)

# Buttons For The Third Row.
negative_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "-x", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).negative())
negative_btn.place(x = 0, y = 177 + 54)

x_squared_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "x^2", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = '**2').insert_operator())
x_squared_btn.place(x = 0 + 90, y = 177 + 54)

sqrt_x_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "√x", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).sqrt())
sqrt_x_btn.place(x = 90 * 2, y = 177 + 54)

log_base10_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "log(x)", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).log10())
log_base10_btn.place(x = 90 * 3, y = 177 + 54)

exp_x_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "exp(x)", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).exp())
exp_x_btn.place(x = 90 * 4, y = 177 + 54)

tan_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "tan(x)", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).tangent())
tan_btn.place(x = 90 * 5, y = 177 + 54)

cot_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "cot(x)", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).cot())
cot_btn.place(x = 90 * 6, y = 177 + 54)

# Buttons For The Fourth Row.
insert_pi_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "π", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = str(round(math.pi, 2))).insert_operator())
insert_pi_btn.place(x = 0, y = 231 + 54)

insert_seven_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "7", font = ("Times New Roman", 20, "bold"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = '7').insert_operator())
insert_seven_btn.place(x = 0 + 90, y = 231 + 54)

insert_eight_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "8", font = ("Times New Roman", 20, "bold"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = '8').insert_operator())
insert_eight_btn.place(x = 90 * 2, y = 231 + 54)

insert_nine_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "9", font = ("Times New Roman", 20, "bold"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = '9').insert_operator())
insert_nine_btn.place(x = 90 * 3, y = 231 + 54)

insert_open_parentheses = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "(", font = ("Times New Roman", 20, "bold"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = '(').insert_operator())
insert_open_parentheses.place(x = 90 * 4, y = 231 + 54)

insert_close_parentheses = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = ")", font = ("Times New Roman", 20, "bold"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = ')').insert_operator())
insert_close_parentheses.place(x = 90 * 5, y = 231 + 54)

arc_sin_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = " asin(x)", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).arc_sin())
arc_sin_btn.place(x = 90 * 6, y = 231 + 54)

# Buttons For The Fifth Row.
insert_euler_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "e", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = str(round(math.e, 2))).insert_operator())
insert_euler_btn.place(x = 0, y = 285 + 54)

insert_four_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "4", font = ("Times New Roman", 20, "bold"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = '4').insert_operator())
insert_four_btn.place(x = 0 + 90, y = 285 + 54)

insert_five_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "5", font = ("Times New Roman", 20, "bold"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = '5').insert_operator())
insert_five_btn.place(x = 90 * 2, y = 285 + 54)

insert_six_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "6", font = ("Times New Roman", 20, "bold"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = '6').insert_operator())
insert_six_btn.place(x = 90 * 3, y = 285 + 54)

insert_plus_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "+", font = ("Times New Roman", 20, "bold"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = '+').insert_operator())
insert_plus_btn.place(x = 90 * 4, y = 285 + 54)

insert_minus_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "-", font = ("Times New Roman", 20, "bold"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = '-').insert_operator())
insert_minus_btn.place(x = 90 * 5, y = 285 + 54)

arc_cos_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "acos(x)", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).arc_cos())
arc_cos_btn.place(x = 90 * 6, y = 285 + 54)

# Buttons For The Sixth Row.
insert_tau_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "τ", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = str(round(math.tau, 2))).insert_operator())
insert_tau_btn.place(x = 0, y = 339 + 54)

insert_one_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "1", font = ("Times New Roman", 20, "bold"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = '1').insert_operator())
insert_one_btn.place(x = 0 + 90, y = 339 + 54)

insert_two_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "2", font = ("Times New Roman", 20, "bold"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = '2').insert_operator())
insert_two_btn.place(x = 90 * 2, y = 339 + 54)

insert_three_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "3", font = ("Times New Roman", 20, "bold"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = '3').insert_operator())
insert_three_btn.place(x = 90 * 3, y = 339 + 54)

insert_multiply_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "×", font = ("Times New Roman", 20, "bold"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = '*').insert_operator())
insert_multiply_btn.place(x = 90 * 4, y = 339 + 54)

insert_div_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "÷", font = ("Times New Roman", 20, "bold"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = '/').insert_operator())
insert_div_btn.place(x = 90 * 5, y = 339 + 54)

arc_tan_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "atan(x)", font = ("Times New Roman", 20, "bold", "italic"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = None).arc_tan())
arc_tan_btn.place(x = 90 * 6, y = 339 + 54)

# Buttons For The Seventh Row.
insert_zero_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "0", font = ("Times New Roman", 20, "bold"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = '0').insert_operator())
insert_zero_btn.place(x = 0, y = 393 + 54)

insert_doublezero_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "00", font = ("Times New Roman", 20, "bold"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = '00').insert_operator())
insert_doublezero_btn.place(x = 0 + 90, y = 393 + 54)

insert_triplezero_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "000", font = ("Times New Roman", 20, "bold"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = '000').insert_operator())
insert_triplezero_btn.place(x = 90 * 2, y = 393 + 54)

raise_to_tens_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "×10^x", font = ("Times New Roman", 20, "bold"), activebackground = "red", relief = GROOVE, command = lambda: Operations(opr = '*10**').insert_operator())
raise_to_tens_btn.place(x = 90 * 3, y = 393 + 54)

insert_dec_point = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = ".", font = ("Times New Roman", 20, "bold"), activebackground = "green", relief = GROOVE, command = lambda: Operations(opr = '.').insert_operator())
insert_dec_point.place(x = 90 * 4, y = 393 + 54)

equals_to_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "=", font = ("Times New Roman", 20, "bold"), activebackground = "blue", relief = SUNKEN, command = lambda: Operations(opr = None).equals())
equals_to_btn.place(x = 90 * 5, y = 393 + 54)

clear_btn = Button(root, justify = CENTER, width = 5, bg = "black", fg = "white", text = "C", font = ("Times New Roman", 20, "bold"), activebackground = "blue", relief = SUNKEN, command = lambda: Operations(opr = None).clear_entry())
clear_btn.place(x = 90 * 6, y = 393 + 54)

# Run The Menu Widget And The Whole Structure Of The App.
if __name__ == '__main__':
    root.config(menu = Menu_Bar)
    root.mainloop()