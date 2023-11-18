import tkinter as tk
import math
win = tk.Tk()
win.geometry('700x300')

def draw_line(e):
    x, y = e.x, e.y
    list_of_x.append(x)
    list_of_y.append(y)
    print('x', list_of_x[canvas.abc])
    print('y', list_of_y[canvas.abc])
    canvas.abc += 1
    # finding_center()
    every_dots()
    win.bind('<ButtonRelease-1>', finding_center)
    if canvas.old_coords:
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1, width=2)
    canvas.old_coords = x, y

def finding_center(a):
    list_of_x.sort()
    list_of_y.sort()
    x_biggest = list_of_x[(len(list_of_x))-1]
    y_biggest = list_of_y[(len(list_of_y))-1]
    x_smallest = list_of_x[0]
    y_smallest = list_of_y[0]
    x_center = x_biggest - x_smallest
    y_center = y_biggest - y_smallest
    r = x_center / 2
    r = y_center / 2
    x = x_smallest + r
    y = y_smallest + r
    # print('------------------------------------------')
    # print('center x', x,'y', y )
    canvas.create_oval(x-r, y-r, x+r, y+r, width=2)
    canvas.create_oval(x-5, y-5, x+5, y+5, width=2, fill='black')
    b = 0
    for i in every_dots():
        distance = math.sqrt(abs(i[0] - x_center) * 
        abs(i[0] - x_center) + abs(i[1] - y_center) * abs(i[1] - y_center))
        # print(distance)
        b+=distance
    # print(distance)
    d = b / len(every_dots())
    # print('r', r)
    # print(d)
        

def every_dots():
    list_ = []
    for i in range(len(list_of_x)):
        emty_list = []
        emty_list.append(list_of_x[i])
        emty_list.append(list_of_y[i])
        list_.append(emty_list)
    # print(list_)
    return list_
        

canvas = tk.Canvas(win, width=700, height=300)
canvas.pack()
canvas.create_text(200, 50, text="draw your best circle", fill="black", font=('Helvetica 15 bold'))
canvas.old_coords = None
list_of_x = []
list_of_y = []
canvas.abc = 0
mous = win.bind('<B1-Motion>', draw_line)




# for i in range(10):
#    draw_line()

win.mainloop()