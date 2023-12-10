import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.canvas = tkinter.Canvas(self.main_window,width=200,height=200)

        self.canvas.create_rectangle(20,20,180,180)

        self.canvas.create_line(20,20,180,180)
        self.canvas.create_arc(20,20,180,180,start = 45, extent = 30)

        self.canvas.pack()

        tkinter.mainloop()
mygui = MyGUI()