from tkinter import *
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
# Matplotlib With Tkinter Backend.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def plot_sin():
    # TkInter Window For The Graph.
    win = Tk()
    win.title('Graph')
    win.geometry("500x500")

    # Figsize = (5x5)inches, rads -> (0 <= rads <= 2π), vals -> (-1 <= vals <= 1)
    # Use Default Dots Per Inch(100).
    x = np.arange(0, math.pi*2, 0.05)
    fig = plt.figure()
    axe = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    y = np.sin(x)
    axe.plot(x, y, 'r')
    axe.grid(True) # I Added Grid And Color To Each Graph, For The Eyes To Read Them Easier.
    axe.set_xlabel('Angles')
    axe.set_title('Y = Sin(x)')
    # axe.set_xticks() Provides Accurate Distance Measurement Between Each Quadrant.
    axe.set_xticks([0, 1.5, 3.1, 4.7])
    axe.set_xticklabels(['(0° To 90°)','(90° To 180°)','(180° To 270°)','(270° To 360°)'])
    axe.spines['left'].set_color('red')

    # Figure Axes Plot On A Canvas, Which Is Then Placed In TkInter Window by .get_tk_widget() method.
    canvas = FigureCanvasTkAgg(fig, master = win)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Toolbars For Each Graph.
    toolbar = NavigationToolbar2Tk(canvas, win)
    toolbar.update()
    canvas.get_tk_widget().pack()

def plot_cos():
    win = Tk()
    win.title('Y = Cos(x)')
    win.geometry("500x500")

    x = np.arange(0, math.pi*2, 0.05)
    fig = plt.figure()
    axe = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 
    y = np.cos(x)
    axe.plot(x, y, 'g')
    axe.grid(True)
    axe.set_xlabel('Angles')
    axe.set_title('Y = Cos(x)')
    axe.set_xticks([0, 1.6, 3.1, 4.7])
    axe.set_xticklabels(['(0° To 90°)','(90° To 180°)','(180° To 270°)','(270° To 360°)'])
    axe.spines['left'].set_color('red')

    canvas = FigureCanvasTkAgg(fig, master = win)
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, win)
    toolbar.update()
    canvas.get_tk_widget().pack()

def plot_tan():
    win = Tk()
    win.title('Y = Tan(x)')
    win.geometry("500x500")

    x = np.arange(0, math.pi*2, 0.05)
    fig = plt.figure()
    axe = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 
    y = np.tan(x)
    axe.plot(x, y, 'm')
    axe.grid(True)
    axe.set_xlabel('Angles')
    axe.set_title('Y = Tan(x)')
    axe.set_xticks([0, 1.5, 3, 4.7])
    axe.set_xticklabels(['(0° To 90°)','(90° To 180°)','(180° To 270°)','(270° To 360°)'])
    axe.spines['left'].set_color('red')

    canvas = FigureCanvasTkAgg(fig, master = win)
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, win)
    toolbar.update()
    canvas.get_tk_widget().pack()

def plot_csc():
    # I Increased Both Figsize And Geometry To Obtain A Better Visualization Of Csc Function.
    # Same Thing Will Go For Both Sec And Cot Functions.
    win = Tk()
    win.title('Y = Csc(x)')
    win.geometry("500x500")

    x = np.arange(0, math.pi*2, 0.05)
    fig = plt.figure()
    axe = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 
    y = [1 / np.sin(i) for i in x]
    axe.plot(x, y, 'c')
    axe.grid(True)
    axe.set_xlabel('Angles')
    axe.set_title('Y = Csc(x)')
    axe.set_xticks([0, 1.5, 3, 4.7])
    axe.set_xticklabels(['(0° To 90°)','(90° To 180°)','(180° To 270°)','(270° To 360°)'])
    axe.spines['left'].set_color('red')

    canvas = FigureCanvasTkAgg(fig, master = win)
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, win)
    toolbar.update()
    canvas.get_tk_widget().pack()

def plot_sec():
    win = Tk()
    win.title('Y = Csc(x)')
    win.geometry("500x500")

    x = np.arange(0, math.pi*2, 0.05)
    fig = plt.figure()
    axe = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 
    y = [1 / np.cos(j) for j in x]
    axe.plot(x, y, 'y')
    axe.grid(True)
    axe.set_xlabel('Angles')
    axe.set_title('Y = Sec(x)')
    axe.set_xticks([0, 1.5, 3, 4.7])
    axe.set_xticklabels(['(0° To 90°)','(90° To 180°)','(180° To 270°)','(270° To 360°)'])
    axe.spines['left'].set_color('red')

    canvas = FigureCanvasTkAgg(fig, master = win)
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, win)
    toolbar.update()
    canvas.get_tk_widget().pack()

def plot_cot():
    win = Tk()
    win.title('Y = Csc(x)')
    win.geometry("500x500")

    x = np.arange(0, math.pi*2, 0.05)
    fig = plt.figure()
    axe = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 
    y = [1/ np.tan(k) for k in x]
    axe.plot(x, y, 'b')
    axe.grid(True)
    axe.set_xlabel('Angles')
    axe.set_title('Y = Cot(x)')
    axe.set_xticks([0, 1.5, 3, 4.7])
    axe.set_xticklabels(['(0° To 90°)','(90° To 180°)','(180° To 270°)','(270° To 360°)'])
    axe.spines['left'].set_color('red')

    canvas = FigureCanvasTkAgg(fig, master = win)
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, win)
    toolbar.update()
    canvas.get_tk_widget().pack()










