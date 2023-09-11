from tkinter import *


root = Tk()
root.geometry("1617x1296")
root.title("Mine Sweeper")

#Creates Canvas for background Image
def title_canvas():
    #Globals need for title_canvas and title_backgroud so root.mainloop can read and display info
    global title_canvas, title_background
    #Canvas creation
    title_canvas = Canvas(root, width=1617, height=1296)
    title_canvas.place(x=0,y=0, relwidth=1,relheight=1)
    #Assign image to var
    title_background = PhotoImage(file="Assets/background.png")
    #Add image to canvas
    title_canvas.create_image(0,0, image=title_background, anchor="nw",) 


#Start-up funtions
title_canvas()
title_canvas.create_text(808,100,text="Mine Sweeper", font=("Arial",50))

root.mainloop()

