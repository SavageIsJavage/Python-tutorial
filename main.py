#GUI_canvas2
from tkinter import * 
class window_one:
    def __init__(self):
        Button(main_window,text="Quit",command=self.quit) .grid() 
        Button(main_window,text="Oval",command=self.oval) .grid()
        Button(main_window,text="Rectangle",command=self.rectangle) .grid()

    def quit (self):
        main_window.destroy() 

    def oval (self):
        canvas.create_oval (10,10,30,30,fill="red",outline="blue",width=5) 
        canvas.update()

    def rectangle (self):
        canvas.create_rectangle (100,100,130,130,fill="pink",outline="green",width=5) 
        canvas.update()


main_window = Tk ()
canvas = Canvas (main_window, width=400, height=300, bg='lightgrey')
canvas.grid()

window_one()