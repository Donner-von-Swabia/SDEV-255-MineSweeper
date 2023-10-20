import random
from tkinter import *

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
        buttonsx.append(buttonsy)
        buttonsy = []
    frame.place(relx=0.5,rely=0.5, anchor=CENTER)
    #Place buttons for reset and quit here
    return buttonsx

def button_press(data,buttonsx):
    (buttonsx[ data[0]])[data[1]].config(state=DISABLED)

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
