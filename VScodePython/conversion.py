from tkinter import *

def nums_conversion():
    # Window For Sub-Menu 2.
    win = Tk()
    win.title("Sub-Menu 2")
    win.geometry("550x500")
    win.resizable(height = False, width = False)
    win.config(bg = "black")

    Title = Label(win, text = "Number System Conversion", font = ("Times New Roman", 25, "bold"), bg = "black", fg = "gold2", width = 35, height = 2, justify = CENTER)
    Title.place(x = -65, y = 0)

    Main_frame = Frame(win, bd = 4, background = "dark orange", height = 419, width = 550)
    Main_frame.place(x = 0, y = 80)

    Main_label = Label(Main_frame, text = "Please Specify A Number Below :", font = ("Times New Roman", 20, "bold"), bg = "dark orange", width = 40, height = 2, justify = CENTER)
    Main_label.place(x = -40, y = -25)

    # Class For Operations.
    class Conversion_Processes():
        def __init__(self, num = None):
            self.start = len(Main_entry.get())
            self.index = 0
            self.number = num
            self.end = END

        def insert_num(self):
            Main_entry.insert(self.start, self.number)

        def clear_num(self):
            Main_entry.delete(self.index, self.end)

        def to_bin(self):
            bin_var = int(Main_entry.get())
            bin_res = bin(bin_var)
            Bin_entry.insert(self.start, str(bin_res).replace('b', ' ').replace(' ', ''))

        def to_oct(self):
            oct_var = int(Main_entry.get())
            oct_res = oct(oct_var)
            # int(res) Returns Dec.
            if oct_res:
                Oct_entry.insert(self.start, str(oct_res))
            else:
                pass

        def to_hex(self):
            hex_var = int(Main_entry.get())
            hex_res = hex(hex_var)
            Hex_entry.insert(self.start, str(hex_res))

        def clear_all_entries(self):
            Bin_entry.delete(self.index, self.end)
            Oct_entry.delete(self.index, self.end)
            Hex_entry.delete(self.index, self.end)

    # Operations Are Limited To Integers Only.
    # Main Entry Length = 25 Digits.
    # Result Entry Length = 20 Bits | Digits.
    # Maximum Input Range : {Unsigned int64(+) | 19 Digits}
    Main_entry = Entry(Main_frame,  width = 25, bg = 'gold', font = ("Times New Roman", 20, "bold"), justify = LEFT)
    Main_entry.place(x = 105, y = 20)

    begin_btn = Button(Main_frame, justify = CENTER, width = 13, bg = "green2", fg = "black", text = "Begin Conversion", font = ("Times New Roman", 15, "bold"), activebackground = "red", relief = GROOVE , command = lambda: [f() for f in [Conversion_Processes(num = None).to_bin, Conversion_Processes(num = None).to_oct, Conversion_Processes(num = None).to_hex]])
    begin_btn.place(x = 294, y = 115)

    # Num-Button Intervals : (X-Interval = 58, Y-Interval = 40)
    btn7 = Button(Main_frame, justify = CENTER, width = 4, bg = "black", fg = "white", text = "7", font = ("Times New Roman", 15, "bold"), activebackground = "green", relief = GROOVE , command = lambda: Conversion_Processes(num = 7).insert_num())
    btn7.place(x = 105, y = 55)

    btn8 = Button(Main_frame, justify = CENTER, width = 4, bg = "black", fg = "white", text = "8", font = ("Times New Roman", 15, "bold"), activebackground = "green", relief = GROOVE , command = lambda: Conversion_Processes(num = 8).insert_num())
    btn8.place(x = 105 + 58, y = 55)

    btn9 = Button(Main_frame, justify = CENTER, width = 4, bg = "black", fg = "white", text = "9", font = ("Times New Roman", 15, "bold"), activebackground = "green", relief = GROOVE , command = lambda: Conversion_Processes(num = 9).insert_num())
    btn9.place(x = 105 + 58 * 2, y = 55)

    btn4 = Button(Main_frame, justify = CENTER, width = 4, bg = "black", fg = "white", text = "4", font = ("Times New Roman", 15, "bold"), activebackground = "green", relief = GROOVE , command = lambda: Conversion_Processes(num = 4).insert_num())
    btn4.place(x = 105, y = 55 + 40)

    btn5 = Button(Main_frame, justify = CENTER, width = 4, bg = "black", fg = "white", text = "5", font = ("Times New Roman", 15, "bold"), activebackground = "green", relief = GROOVE , command = lambda: Conversion_Processes(num = 5).insert_num())
    btn5.place(x = 105 + 58, y = 55 + 40)

    btn6 = Button(Main_frame, justify = CENTER, width = 4, bg = "black", fg = "white", text = "6", font = ("Times New Roman", 15, "bold"), activebackground = "green", relief = GROOVE , command = lambda: Conversion_Processes(num = 6).insert_num())
    btn6.place(x = 105 + 58 * 2, y = 55 + 40)

    btn1 = Button(Main_frame, justify = CENTER, width = 4, bg = "black", fg = "white", text = "1", font = ("Times New Roman", 15, "bold"), activebackground = "green", relief = GROOVE , command = lambda: Conversion_Processes(num = 1).insert_num())
    btn1.place(x = 105, y = 55 + 40 * 2)

    btn2 = Button(Main_frame, justify = CENTER, width = 4, bg = "black", fg = "white", text = "2", font = ("Times New Roman", 15, "bold"), activebackground = "green", relief = GROOVE , command = lambda: Conversion_Processes(num = 2).insert_num())
    btn2.place(x = 105 + 58, y = 55 + 40 * 2)

    btn3 = Button(Main_frame, justify = CENTER, width = 4, bg = "black", fg = "white", text = "3", font = ("Times New Roman", 15, "bold"), activebackground = "green", relief = GROOVE , command = lambda: Conversion_Processes(num = 3).insert_num())
    btn3.place(x = 105 + 58 * 2, y = 55 + 40 *2)

    btn0 = Button(Main_frame, justify = CENTER, width = 4, bg = "black", fg = "white", text = "0", font = ("Times New Roman", 15, "bold"), activebackground = "green", relief = GROOVE , command = lambda: Conversion_Processes(num = 0).insert_num())
    btn0.place(x = 105 + 58, y = 55 + 40 * 3)

    btn_clear = Button(Main_frame, justify = CENTER, width = 4, bg = "black", fg = "white", text = "C", font = ("Times New Roman", 15, "bold"), activebackground = "blue", relief = GROOVE , command = lambda: Conversion_Processes(num = None).clear_num())
    btn_clear.place(x = 105 + 58 * 2, y = 55 + 40 * 3)

    # Bin, Oct, Hex, Widgets.
    clear_entries = Button(Main_frame, justify = CENTER, width = 5, bg = "black", fg = "white", text = "Clear", font = ("Times New Roman", 15, "bold"), activebackground = "blue", relief = GROOVE , command = lambda: Conversion_Processes(num = None).clear_all_entries())
    clear_entries.place(x = 10, y = 290)

    Bin_label = Label(Main_frame, text = "Bin = ", font = ("Times New Roman", 20, "bold"), bg = "dark orange", width = 5, height = 2, justify = CENTER)
    Bin_label.place(x = 99, y = 225)

    Bin_entry = Entry(Main_frame, width = 20, bg = 'turquoise2', font = ("Times New Roman", 20, "bold"), justify = LEFT)
    Bin_entry.place(x = 175, y = 240)

    Oct_label = Label(Main_frame, text = "Oct = ", font = ("Times New Roman", 20, "bold"), bg = "dark orange", width = 5, height = 2, justify = CENTER)
    Oct_label.place(x = 99, y = 275)

    Oct_entry = Entry(Main_frame, width = 20, bg = 'turquoise2', font = ("Times New Roman", 20, "bold"), justify = LEFT)
    Oct_entry.place(x = 175, y = 290)

    Hex_label = Label(Main_frame, text = "Hex = ", font = ("Times New Roman", 20, "bold"), bg = "dark orange", width = 5, height = 2, justify = CENTER)
    Hex_label.place(x = 99, y = 325)
    
    Hex_entry = Entry(Main_frame, width = 20, bg = 'turquoise2', font = ("Times New Roman", 20, "bold"), justify = LEFT)
    Hex_entry.place(x = 175, y = 340)


        