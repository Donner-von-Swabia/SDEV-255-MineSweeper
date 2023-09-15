from tkinter import *
import canvas

root = Tk()
root.geometry("1617x1296")
root.title("Mine Sweeper")

#Start-up funtions
canvas.title_canvas_build(root)
canvas.title_canvas.create_text(808,100,text="Mine Sweeper", font=("Arial",50))

root.mainloop()

