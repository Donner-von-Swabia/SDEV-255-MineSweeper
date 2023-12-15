import random
from tkinter import *
import canvas
import time



def build_button(min,max,rows,root):
    #Main function to build tiles
    buttonsx = []
    buttonsy = []
    frame = Frame(root)

    #For loops creates all the tiles as buttons with command linking to button_press
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
    #Declaring globals for time, score, and flag
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


    # Adds all other buttons to the main game page
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
    #Allows the user to activate flag mode
    global flag
    if (flag):
        flag = False
    else:
        flag = True

def back_click(data):
    #Basically destroys everything from main game page and calls the tile building function
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
    #Called when game is over, allows player to play again
    frame = data[0]
    root = data[1]
    frame.destroy()
    #Destroys the tile frame then rebuilds it with a new set of mines
    canvas.build_miner(root)

def button_press(data,buttonsx):
    #Called when tile is pressed
    # Checks if flag mode is active
    if (flag  == False):
        #Disables tile then checks what number is associated with it
        (buttonsx[ data[0]])[data[1]].config(state=DISABLED)
        print((buttonsx[ data[0]])[data[1]].cget('text'))
        mine_logic(((buttonsx[ data[0]])[data[1]].cget('text')),data,buttonsx)
    else:
        #Blacks out the tile / flagging
        (buttonsx[ data[0]])[data[1]].config(foreground="black", background="black")

def mine_logic(value,data, buttonsx):
    #Function called from button press to check what the value the tile is and update score and time
    global score
    global cscore
    global etime
    global ctime
    match value:
        case 9:
            #The user has struck a mine, the game is over.
            #((buttonsx[ data[0]])[data[1]]).config(foreground="red", background="red")
            end_game(buttonsx)
        case 0:
            #If tile number is 0
            ((buttonsx[ data[0]])[data[1]]).config(foreground="blue", background="blue")
            
            cscore = cscore + 100
            ctime = ctime + 1
            score.config(text="Score:  " + str(cscore))
            etime.config(text="Time:   " + str(ctime))
            score.place()
            etime.place()

        case _:
           #If tile number is any warning number
           ((buttonsx[ data[0]])[data[1]]).config(foreground="yellow", background="yellow")
           cscore = cscore + 100
           ctime = ctime + 1
           score.config(text="Score:  " + str(cscore))
           etime.config(text="Time:   " + str(ctime))
           score.place()
           etime.place()


def end_game(buttonsx):
    #Called when player clicks tile number with a 9
    min = 0
    max = len(buttonsx)
    #Disables all tiles and changes color to blue
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
    #Function creates 2D array and fills  in where mines are
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
    #Looks very confusing but basically adds all warning numbers so all adjacent tiles around a mine have numbers
    #Basically goes through 2D array, checks if value is a 0 or 9
        # If the location in the 2D  array has a 9 then the script will add a 1 to all adjacent tiles
        #However it checks before adding a 1 if the adjacent tile is a 9 then it will not add a 1 as it is mine
        
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
