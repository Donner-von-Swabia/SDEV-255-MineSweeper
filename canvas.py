from tkinter import *
import sweeper_screen
#Creates Canvas for background Image
def title_canvas_build(root):
    #Globals need for title_canvas and title_backgroud so root.mainloop can read and display info
    global title_canvas, title_background
    #Canvas creation
    title_canvas = Canvas(root, width=1617, height=1296)
    title_canvas.place(x=0,y=0, relwidth=1,relheight=1)
    #Assign image to var
    title_background = PhotoImage(file="Assets/background.png")
    #Add image to canvas
    title_canvas.create_image(0,0, image=title_background, anchor="nw",)
    build_layout(root)

def build_miner(root):
    min = 0
    max = 15
    rows = []
    global buttonsx

    rows = sweeper_screen.build_mines(min,max,rows)
    rows = sweeper_screen.build_number(min,max,rows)
    buttonsx = sweeper_screen.build_button(min,max,rows,root)


def start_click(start_button,exit_button,settings_button,root):
    start_button.destroy()
    exit_button.destroy()
    settings_button.destroy()
    build_miner(root)
 
  

def run_quit(root):
    root.quit()

def build_layout(root):
    title_canvas.create_text(808,100,text="Mine Sweeper", font=("Arial",50))
    settings_button = Button(root, text="Settings", font=("Arial", 50), padx=100)
    settings_button.place(x=600,y=550)
    exit_button = Button(root, text="Exit",font=("Arial",50),command= lambda: run_quit(root),padx=100)
    exit_button.place(x=650,y=700)
    start_button = Button(root, text= "Play", font=("Arial",50), command= lambda: start_click(start_button,exit_button,settings_button,root), padx = 100)
    start_button.place(x=650,y=400)