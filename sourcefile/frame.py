import tkinter as tk


class FrameOne:
    def __init__(self, master):
        self.master = master
        self.master.config(bg='blue')
        self.face1 = tk.Frame(self.master, )
        self.face1.pack()
        btn1 = tk.Button(self.face1, text='frame1', command=lambda: self.change(1)).grid(row=0, column=0)
        btn2 = tk.Button(self.face1, text='frame2', command=lambda: self.change(2)).grid(row=0, column=1)

    def change(self, num):
        switch = {
            1: FrameOne,
            2: FrameTwo
        }
        self.face1.destroy()
        switch[num](self.master)


class FrameTwo:
    def __init__(self, master):
        self.master = master
        self.master.config(bg='red')
        self.face2 = tk.Frame(self.master, )
        self.face2.pack()
        btn1 = tk.Button(self.face2, text='frame1', command=lambda: self.change(1)).grid(row=0, column=0)
        btn2 = tk.Button(self.face2, text='frame2', command=lambda: self.change(2)).grid(row=0, column=1)

    def change(self, num):
        switch = {
            1: FrameOne,
            2: FrameTwo
        }
        self.face2.destroy()
        switch[num](self.master)
