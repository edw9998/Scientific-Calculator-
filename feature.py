# The First Feature Will Allow Users To View Graphical Representation Of Various Basic Trigonometric Functions.
from tkinter import *
import graphs

def graph_feature():
    win = Tk()
    win.title("Sub-Menu 1")
    win.geometry("550x500")
    win.resizable(height = False, width = False)
    win.config(bg = "snow")

    label1 = Label(win, text = "Basic Trigonometric Graphs", font = ("Times New Roman", 25, "bold"), bg = "black", fg = "khaki1", width = 35, height = 2, justify = CENTER)
    label1.place(x = -70, y = 0)

    label2 = Label(win, text = "View Graphical Representation Of These Trigonometric Functions :", font = ("Times New Roman", 14, "bold"), bg = "gold2", fg = "black", width = 50, justify = LEFT)
    label2.place(x = 0, y = 80)

    btns_frame = Frame(win, bd = 4, background = "dark orange", height = 392, width = 550)
    btns_frame.place(x = 0, y = 108)

    class Button_Placings:
        '''
        Button Intervals In Frame -> (X = 260, Y = 120).
        '''
        global btns_frame
        def __init__(self):
            self.root = btns_frame
            self.style = ("Times New Roman", 20, "bold", "italic")
            self.cursor_style = "plus"
            self.place = CENTER
            self.relief = RAISED
            self.bgcolor = "black" 
            self.fgcolor = "snow" 
            self.height = 1
            self.width = 8
            
        def place_sin_btn(self):
            sin_btn = Button(self.root, text = "y = sin(x)", font = self.style, bg = self.bgcolor, fg = self.fgcolor, cursor = self.cursor_style, justify = self.place, relief = self.relief, height = self.height, width = self.width, command = lambda: graphs.plot_sin())
            sin_btn.place(x = 75, y = 30)

        def place_cos_btn(self):
            cos_btn = Button(self.root, text = "y = cos(x)", font = self.style, bg = self.bgcolor, fg = self.fgcolor, cursor = self.cursor_style, justify = self.place, relief = self.relief, height = self.height, width = self.width, command = lambda: graphs.plot_cos())
            cos_btn.place(x = 75, y = 30 + 120)

        def place_tan_btn(self):
            tan_btn = Button(self.root, text = "y = tan(x)", font = self.style, bg = self.bgcolor, fg = self.fgcolor, cursor = self.cursor_style, justify = self.place, relief = self.relief, height = self.height, width = self.width, command = lambda: graphs.plot_tan())
            tan_btn.place(x = 75, y = 30 + 120 * 2)

        def place_csc_btn(self):
            csc_btn = Button(self.root, text = "y = csc(x)", font = self.style, bg = self.bgcolor, fg = self.fgcolor, cursor = self.cursor_style, justify = self.place, relief = self.relief, height = self.height, width = self.width, command = lambda: graphs.plot_csc())
            csc_btn.place(x = 335, y = 30)

        def place_sec_btn(self):
            sec_btn = Button(self.root, text = "y = sec(x)", font = self.style, bg = self.bgcolor, fg = self.fgcolor, cursor = self.cursor_style, justify = self.place, relief = self.relief, height = self.height, width = self.width, command = lambda: graphs.plot_sec())
            sec_btn.place(x = 335, y = 30 + 120)

        def place_cot_btn(self):
            cot_btn = Button(self.root, text = "y = cot(x)", font = self.style, bg = self.bgcolor, fg = self.fgcolor, cursor = self.cursor_style, justify = self.place, relief = self.relief, height = self.height, width = self.width, command = lambda: graphs.plot_cot())
            cot_btn.place(x = 335, y = 30 + 120 * 2)

    Button_Placings().place_sin_btn()
    Button_Placings().place_cos_btn()
    Button_Placings().place_tan_btn()
    Button_Placings().place_csc_btn()
    Button_Placings().place_sec_btn()
    Button_Placings().place_cot_btn()


    



  
            









    
    
