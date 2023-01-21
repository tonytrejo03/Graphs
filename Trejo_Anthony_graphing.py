# Tony Trejo
# HW9
# This program will graph different lines based on users
# choice of graph whie givng a max x value and min x value

import matplotlib.pyplot as plt
import PySimpleGUI as sg
import math



# matplotlib
def draw_plot():
    plt.figure()
    xs = []
    for i in range(x_min,x_max+1):
        xs.append(i)
    ys = []                     # linear
    for x in xs:
        ys.append(x)
    plt.plot(xs,ys)         
    plt.figure()
    ys = []                     # quadratic
    for x in xs:
        ys.append(x*x)
    plt.plot(xs,ys)
    plt.figure()
    ys = []                     # cubic
    for x in xs:
        ys.append(x*x*x)
    plt.plot(xs,ys)
    plt.figure()
    ys = []                     # logarithmic
    for x in xs:
        ys.append(math.log(x))
    plt.plot(xs,ys)
    plt.figure()
    ys = []                     # linearithmic
    for x in xs:
        ys.append(x*math.log(x,2))
    plt.plot(xs,ys)
#    plt.title("Algorithmic Complexity Functions", fontsize=14)
 #   plt.xlabel("x", fontsize=10)
  #  plt.ylabel("y", fontsize=10)
   # plt.grid(True)
    # plt.show()


# PysimpleGUI
layout = [[sg.Text("This plotting tool shows you the difference between a linear,")],
          [sg.Text("quadratic, cubic, and logarithmic curve.")],
          [sg.Text("What do you want to plot? Check the boxes.")],
          [sg.Checkbox("Linear",key="linear"),sg.Checkbox("Quadratic",key="quadratic"),sg.Checkbox("Cubic",key="cubic"),sg.Checkbox("Logarithmic",key="lograrithmic"),sg.Checkbox("Linearithmic",key="linearithmic")],
          [sg.Text("Enter min X: "),sg.Input(key="x_min",do_not_clear=True,size=(5,1)),sg.Text("Enter max X: "),sg.Input(key="x_max",do_not_clear=True,size=(5,1))],
          [sg.Button("Plot"),sg.Button("Close")]]
          
          
win = sg.Window(title="Function Plotter",layout=layout)



# loop
while True:
    event, values = win.read()
    if event == sg.WIN_CLOSED or event == "Close":
        break
    elif event == "Plot":
        x_min = int(values["x_min"])
        if x_min <= 0:
            sg.Popup("You must specify integers for Min X and Max X")
            sg.Button("OK")
            sg.Window(title="Error")
            if event == "OK":
                break
        x_max = int(values["x_max"])
        if x_max <= x_min:
            sg.Popup("X max must be greater than x min.")
            sg.Button("Ok")
            sg.Window(title="Error")
            if event == "Ok":
                break
        draw_plot()
        plt.title("Algorithmic Complexity Functions", fontsize=14)
        plt.xlabel("x", fontsize=10)
        plt.ylabel("y", fontsize=10)
        plt.grid(True)
        plt.show()
        
           
win.close()
