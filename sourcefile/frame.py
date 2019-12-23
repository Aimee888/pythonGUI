import time
import threading
from tkinter import *


def button_set(frame_face, func_name):
    btn1 = Button(frame_face, text='frame1', command=lambda: func_name(1)).grid(row=0, column=0)
    btn2 = Button(frame_face, text='frame2', command=lambda: func_name(2)).grid(row=0, column=1)


class FrameOne:
    def __init__(self, master):
        self.master = master
        self.master.config(bg='blue')
        self.face1 = Frame(self.master, )
        self.face1.pack(anchor=SW)
        button_set(self.face1, self.change)
        self.run()

    def change(self, num):
        switch = {
            1: FrameOne,
            2: FrameTwo
        }
        self.face1.destroy()
        switch[num](self.master)

    def run(self):
        # 设置进度条
        self.progressbar_set()

    def progressbar_set(self):
        sum_length = 630
        canvas_progress_bar = Canvas(self.face1, width=sum_length, height=20)
        # canvas_shape = canvas_progress_bar.create_rectangle(0, 0, 0, 25, fill='green')
        canvas_shape = canvas_progress_bar.create_rectangle(0, 0, 0, 25, fill='green')
        canvas_text = canvas_progress_bar.create_text(292, 4, anchor=NW)
        canvas_progress_bar.itemconfig(canvas_text, text='00:00:00')
        var_progress_bar_percent = StringVar()
        var_progress_bar_percent.set('00.00 %')
        label_progress_bar_percent = Label(self.face1, textvariable=var_progress_bar_percent, fg='#F5F5F5', bg='#535353')
        canvas_progress_bar.grid(row=2, column=3)
        label_progress_bar_percent.grid(row=2, column=50)
        # canvas_progress_bar.place(relx=0.45, rely=0.4, anchor=CENTER)
        # label_progress_bar_percent.place(relx=0.89, rely=0.4, anchor=CENTER)

        button_start = Button(
            self.face1, text='开始', fg='#F5F5F5', bg='#7A7A7A', command=lambda: self.processbar_run(
                sum_length, canvas_progress_bar, canvas_shape, canvas_text, var_progress_bar_percent
            ),
            height=1, width=15, relief=GROOVE, bd=2, activebackground='#F5F5F5', activeforeground='#535353')
        # button_start.place(relx=0.45, rely=0.5, anchor=CENTER)
        button_start.grid(row=20, column=20)

    def processbar_run(self, sum_length, canvas_progress_bar, canvas_shape, canvas_text, var_progress_bar_percent):
        th = threading.Thread(target=self.update_progress_bar,
                              args=(sum_length, canvas_progress_bar, canvas_shape, canvas_text,
                                    var_progress_bar_percent, ))
        th.setDaemon(True)
        th.start()

    def update_progress_bar(self, sum_length, canvas_progress_bar, canvas_shape, canvas_text, var_progress_bar_percent):
        for percent in range(1, 101):
            hour = int(percent / 3600)
            minute = int(percent / 60) - hour * 60
            second = percent % 60
            green_length = int(sum_length * percent / 100)
            canvas_progress_bar.coords(canvas_shape, (0, 0, green_length, 25))
            canvas_progress_bar.itemconfig(canvas_text, text='%02d:%02d:%02d' % (hour, minute, second))
            var_progress_bar_percent.set('%0.2f %%' % percent)
            time.sleep(1)


class FrameTwo:
    def __init__(self, master):
        self.master = master
        self.master.config(bg='red')
        self.face2 = Frame(self.master, )
        self.face2.pack(anchor=SW)
        button_set(self.face2, self.change)

    def change(self, num):
        switch = {
            1: FrameOne,
            2: FrameTwo
        }
        self.face2.destroy()
        switch[num](self.master)
