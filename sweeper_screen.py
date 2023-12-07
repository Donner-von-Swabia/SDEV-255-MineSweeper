import random
from tkinter import *
import canvas
import time



def build_button(min,max,rows,root):
    buttonsx = []
    buttonsy = []
    frame = Frame(root)
    for x in range(min,max):
        for y in range(min,max):
            temp = ("Button" + str(x) + str(y))
            buttonsy.append(temp)
            (buttonsy[y]) = Button(frame,text=(rows[x])[y],command=lambda data = [x,y]: button_press(data,buttonsx),padx=5)
            (buttonsy[y]).grid(row= x,column=y)
            (buttonsy[y]).config(foreground="white", activeforeground="white", background="white")
        buttonsx.append(buttonsy)
        buttonsy = []
    frame.place(relx=0.5,rely=0.5, anchor=CENTER)
    global reset_button
    global back_button
    global score
    global cscore
    global etime
    global ctime
    global flag
    global check_time
    global flag_button
    check_time = True
    flag = False
    cscore = 0
    ctime = 000
    reset_button = Button(root,text="Reset Game",padx=5,pady=5,command=lambda data =[frame,root]: game_reset(data))
    reset_button.place(relx=0.5,rely=0.75, anchor=CENTER)
    reset_button.config(state=DISABLED)
    back_button = Button(root,text="Back",padx=5,pady=5,command=lambda data =[frame,root]:back_click(data))
    back_button.place(relx=0.75,rely=0.75, anchor=CENTER)
    score = Label(root,text="Score:   " + str(cscore))
    etime = Label(root,text="Time:   " + str(int(ctime)))
    score.place(relx=0.25,rely=0.25, anchor=CENTER)
    etime.place(relx=0.75,rely=0.25, anchor=CENTER)
    flag_button = Button(root, text="Flag", command=setchange)
    flag_button.place(relx=0.25,rely=0.75, anchor=CENTER)
    return buttonsx

def setchange():
    global flag
    if (flag):
        flag = False
    else:
        flag = True
def back_click(data):
    frame = data[0]
    root = data[1]
    frame.destroy()
    reset_button.destroy()
    back_button.destroy()
    flag_button.destroy()
    score.destroy()
    etime.destroy()
    canvas.build_layout(root)

def game_reset(data):
    frame = data[0]
    root = data[1]
    frame.destroy()
    canvas.build_miner(root)

def button_press(data,buttonsx):
    if (flag  == False):
        (buttonsx[ data[0]])[data[1]].config(state=DISABLED)
        print((buttonsx[ data[0]])[data[1]].cget('text'))
        mine_logic(((buttonsx[ data[0]])[data[1]].cget('text')),data,buttonsx)
    else:
        (buttonsx[ data[0]])[data[1]].config(foreground="black", background="black")

def mine_logic(value,data, buttonsx):
    match value:
        case 9:
            #((buttonsx[ data[0]])[data[1]]).config(foreground="red", background="red")
            end_game(buttonsx)
        case 0:
            ((buttonsx[ data[0]])[data[1]]).config(foreground="blue", background="blue")
        case _:
           ((buttonsx[ data[0]])[data[1]]).config(foreground="yellow", background="yellow")


def end_game(buttonsx):
    min = 0
    max = len(buttonsx)
    for x in range(min,max):
        for y in range(min,max):
            buttonsx[x][y].config(background="Blue",activeforeground="Red")
            buttonsx[x][y].config(state=DISABLED)
    reset_button.config(state=NORMAL)

def clear_sea():
    return
def warning():
    return

def build_mines(min,max,rows):
    list1=[0,1,0,0,0,0,0,0]
    column = []
    for i in range(min,max):
        for j in range(min,max):
            num = random.choice(list1)
            if num == 1:
                column.append(9)
            else:
                column.append(0)  
        rows.append(column)
        column = []
    return rows

def build_number(min,max,rows):
    for i in range(min,max):
        for j in range(min,max):
            if (rows[i])[j] == 9:
                if i > 0 and i < len(rows):
                    if (rows[(i-1)])[j-1] != 9:
                        (rows[(i-1)])[j-1]+= 1
                    if (rows[i-1])[j] != 9:
                        (rows[i-1])[j]+= 1
                    if j < (max -1):
                        if (rows[i-1])[j+1] != 9:
                            (rows[i-1])[j+1]+= 1
                        if i < (max-1):
                            if (rows[i+1])[j+1] != 9:
                                (rows[i+1])[j+1]+= 1
                    if i < (max-1):
                        if (rows[(i+1)])[j-1] != 9:
                            (rows[(i+1)])[j-1]+= 1
                        if (rows[(i+1)])[j] != 9:
                            (rows[(i+1)])[j]+= 1
                if j > 0 and j < max-1:
                    if (rows[(i)])[j-1] != 9:
                        (rows[(i)])[j-1]+= 1
                    if (rows[(i)])[j+1] != 9:
                        (rows[(i)])[j+1]+= 1
    return rows
