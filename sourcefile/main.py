import tkinter as tk
import threading
import time
from tkinter import ttk


class TestBenchMaker:

    def __init__(self):
        self.TITLE = "Test"
        self.WIDTH = 1024
        self.HEIGHT = 768
        self.parseDic = {}

    def click(self):
        print(self.TITLE)

    def menu_set(self, window):
        # 菜单选项
        menubar = tk.Menu(window)
        window.config(menu=menubar)
        filemenu1 = tk.Menu(menubar, tearoff=0)
        filemenu2 = tk.Menu(menubar, tearoff=0)
        filemenu3 = tk.Menu(menubar, tearoff=0)
        filemenu4 = tk.Menu(menubar, tearoff=0)
        # 给menu添加一个选项
        menubar.add_cascade(label='menu1', menu=filemenu1)
        menubar.add_cascade(label='menu2', menu=filemenu2)
        menubar.add_cascade(label='menu3', menu=filemenu3)
        menubar.add_cascade(label='menu4', menu=filemenu4)
        # menu1添加子选项
        filemenu1.add_command(label='新建...', command=self.click())
        filemenu1.add_command(label='打开...', command=self.click())
        filemenu1.add_command(label='保存...', command=self.click())
        filemenu1.add_command(label='关闭填写...', command=window.quit)

    def place_gui(self, window):
        self.ws = window.winfo_screenwidth()
        self.hs = window.winfo_screenheight()
        x = (self.ws / 2) - (self.WIDTH / 2)
        y = (self.hs / 2) - (self.HEIGHT / 2)
        window.geometry('%dx%d+%d+%d' % (self.WIDTH, self.HEIGHT, x, y))

    # Change type
    @staticmethod
    def change_type(tag, clockSet, resetSet, customSet):
        clockSet.pack_forget()
        resetSet.pack_forget()
        customSet.pack_forget()
        if tag == 0:
            clockSet.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, pady=5, padx=10)
        elif tag == 1:
            resetSet.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, pady=5, padx=10)
        elif tag == 2:
            customSet.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, pady=5, padx=10)

    @staticmethod
    def clock_set(frame3):
        # Clock setting
        initalValue = tk.StringVar()
        initalValue.set("1'b0")
        cycle = tk.StringVar()
        converse = tk.StringVar()
        clockSet = tk.Frame(frame3, bg="white")
        # clockSet.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, pady=5, padx=10)
        tk.Label(clockSet, text="Initial Value").grid(row=0, column=0, pady=5)
        tk.Radiobutton(clockSet, text="1'b0", variable=initalValue, value="1'b0").grid(row=0, column=1, padx=5)
        tk.Radiobutton(clockSet, text="1'b1", variable=initalValue, value="1'b1").grid(row=0, column=2, padx=5)
        tk.Label(clockSet, text="", width=10).grid(row=0, column=3)
        tk.Label(clockSet, text="Cycle").grid(row=0, column=4, pady=5, padx=10)
        tk.Entry(clockSet, textvariable=cycle, width=10, bd=2, bg="white").grid(row=0, column=5)
        return clockSet, initalValue, converse

    @staticmethod
    def reset_set(frame3, initalValue, converse):
        resetSet = tk.Frame(frame3, bg="white")
        tk.Label(resetSet, text="Initial Value").grid(row=0, column=0, pady=5)
        tk.Radiobutton(resetSet, text="1'b0", variable=initalValue, value="1'b0").grid(row=0, column=1, padx=5)
        tk.Radiobutton(resetSet, text="1'b1", variable=initalValue, value="1'b1").grid(row=0, column=2, padx=5)
        tk.Label(resetSet, text="", width=10).grid(row=0, column=3)
        tk.Label(resetSet, text="Converse").grid(row=0, column=4, pady=5, padx=10)
        tk.Entry(resetSet, textvariable=converse, width=10, bd=2, bg="white").grid(row=0, column=5)
        return resetSet

    @staticmethod
    def custom_set(frame3, initalValue):
        defaultValue = tk.IntVar()
        radixValue = tk.IntVar()
        radixValue.set(0)
        customSet = tk.Frame(frame3, bg="white")
        customSet.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, pady=5, padx=10)
        # Radix 0 --> b, 1 --> o, 2 --> d, 3 --> h
        tk.Label(customSet, text="Radix").grid(row=0, column=0, pady=5, padx=1)
        tk.Radiobutton(customSet, text="Binary", variable=radixValue, value=0).grid(row=0, column=1)
        tk.Radiobutton(customSet, text="Octal", variable=radixValue, value=1).grid(row=0, column=2)
        tk.Radiobutton(customSet, text="Decimal", variable=radixValue, value=2).grid(row=0, column=3)
        tk.Radiobutton(customSet, text="Hexadecimal", variable=radixValue, value=3).grid(row=0, column=4)
        # Initial value
        tk.Label(customSet, text="Default Value").grid(row=1, column=0, pady=5, padx=10)
        tk.Radiobutton(customSet, text="default 0", variable=defaultValue, value=0).grid(row=1, column=1, padx=5)
        tk.Radiobutton(customSet, text="default 1", variable=defaultValue, value=1).grid(row=1, column=2, padx=5)
        tk.Label(customSet, text="Initial Value").grid(row=1, column=3, pady=5, padx=5)
        tk.Entry(customSet, textvariable=initalValue, width=12, bd=2, bg="white", justify=tk.RIGHT).grid(row=1,
                                                                                                         column=4)
        tk.Button(customSet, text="test", command=lambda: print(initalValue.get())).grid()
        return customSet

    @staticmethod
    def update_progress_bar(sum_length, canvas_progress_bar, canvas_shape, canvas_text):
        for percent in range(1, 101):
            hour = int(percent / 3600)
            minute = int(percent / 60) - hour * 60
            second = percent % 60
            green_length = int(sum_length * percent / 100)
            canvas_progress_bar.coords(canvas_shape, (0, 0, green_length, 25))
            canvas_progress_bar.itemconfig(canvas_text, text='%0.2f %%' % percent)
            # var_progress_bar_percent.set('%0.2f %%' % percent)
            time.sleep(0.5)

    def run(self, sum_length, canvas_progress_bar, canvas_shape, canvas_text):
        th = threading.Thread(target=self.update_progress_bar, args=(
            sum_length, canvas_progress_bar, canvas_shape, canvas_text))
        th.setDaemon(True)
        th.start()

    def frame3_inter(self, frame3):
        frame3.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame3, text="TEST1 CENTER", font="Arial, 25").pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame3, text="").pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

        total_bar = tk.Frame(frame3, bg="white")
        total_bar.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        # 进度条描述
        total_bar_descrip = tk.Label(total_bar, text=" T1 Running", font="Arial, 15")
        total_bar_descrip.grid(row=0, column=0)
        # 进度条
        total_bar_pic = tk.Label(total_bar, text="", font="Arial, 15", width=88)
        total_bar_pic.grid(row=0, column=1, padx=25)
        sum_length = 680
        canvas_progress_bar = tk.Canvas(total_bar_pic, width=sum_length, height=25, bg="LightGrey")
        canvas_shape = canvas_progress_bar.create_rectangle(0, 0, 0, 25, fill='MediumSeaGreen')
        canvas_text = canvas_progress_bar.create_text(292, 4, anchor=tk.NW)
        canvas_progress_bar.itemconfig(canvas_text, text='00.00 %')
        # var_progress_bar_percent = tk.StringVar()
        # var_progress_bar_percent.set('00.00 %')
        # label_progress_bar_percent = tk.Label(total_bar_pic, textvariable=var_progress_bar_percent, fg='#F5F5F5', bg='#535353')
        # canvas_progress_bar.place(relx=0.45, rely=0.4, anchor=tk.CENTER)
        canvas_progress_bar.place(anchor=tk.NW)
        # label_progress_bar_percent.place(relx=0.89, rely=0.4, anchor=tk.CENTER)

        tk.Label(frame3, text="").pack(side=tk.TOP,  fill=tk.X)
        tk.Label(frame3, text=" Input Setting", font="Arial, 15", anchor=tk.NW).pack(side=tk.TOP, fill=tk.X)
        # scroll = tk.Scrollbar(frame3)
        # scroll.pack(side=tk.RIGHT, fill=tk.Y)
        # self.inputBox = tk.Listbox(frame3, bd=1, selectmode=tk.SINGLE, yscrollcommand=scroll.set, height=8)
        # self.inputBox.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, expand=tk.YES)
        # self.inputBox.insert(tk.END, "aaa")
        # self.inputBox.insert(tk.END, "bbb")
        # self.inputBox.insert(tk.END, "ccc")
        # self.inputBox.insert(tk.END, "ddd")
        # for i in range(0, 20):
        #     self.inputBox.insert(tk.END, i)
        # scroll.config(command=self.inputBox.yview)

        # Input setting
        """
               nw        n         ne

               w       center      e

               sw        s          se
        """
        width = 10
        frameInputSet = tk.Frame(frame3, bg="white")
        frameInputSet.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        # tk.Label(frame3, text=" Input Setting", font=("Arial, 15"), anchor=tk.NW).pack()
        tk.Label(frameInputSet, text=" column1", font=("Arial, 15"), bg="Lavender", width=32).grid(row=1, column=0, padx=1)
        tk.Label(frameInputSet, text=" column2", font=("Arial, 15"), bg="Lavender", width=68).grid(row=1, column=1, padx=1)

        # test_box = tk.Frame(frame3, bg="white")
        # test_box.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        # tk.Label(test_box, text=" test1", font=("Arial, 10"), width=45).grid(row=1, column=0, padx=1)
        # tk.Label(test_box, text=" test2", font=("Arial, 10"), width=90, bg="blue").grid(row=1, column=1, padx=20)

        scroll = tk.Scrollbar(frame3)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.inputBox = tk.Listbox(frame3, bd=1, selectmode=tk.SINGLE, yscrollcommand=scroll.set, height=8, width=135)
        self.inputBox.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, expand=tk.YES)
        left0 = tk.Label(self.inputBox, text="", font=("Arial, 10"), width=45, bg="white")
        left0.grid(row=0, column=0, padx=1)
        right0 = tk.Label(self.inputBox, text="", font=("Arial, 10"), width=90, bg="blue")
        right0.grid(row=0, column=1, padx=20)
        left1 = tk.Label(self.inputBox, text="", font=("Arial, 10"), width=45, bg="white")
        left1.grid(row=1, column=0, padx=1)
        right1 = tk.Label(self.inputBox, text="", font=("Arial, 10"), width=90, bg="blue")
        right1.grid(row=1, column=1, padx=20)
        left2 = tk.Label(self.inputBox, text="", font=("Arial, 10"), width=45, bg="white")
        left2.grid(row=2, column=0, padx=1)
        right2 = tk.Label(self.inputBox, text="", font=("Arial, 10"), width=90, bg="blue")
        right2.grid(row=2, column=1, padx=20)
        left3 = tk.Label(self.inputBox, text="", font=("Arial, 10"), width=45, bg="white")
        left3.grid(row=3, column=0, padx=1)
        right3 = tk.Label(self.inputBox, text="", font=("Arial, 10"), width=90, bg="blue")
        right3.grid(row=3, column=1, padx=20)
        right0["bg"] = "white"
        right1["bg"] = "white"
        right2["bg"] = "white"
        right3["bg"] = "white"
        scroll.config(command=self.inputBox.yview)

        tk.Label(frame3, text="", font=("Arial, 15"), anchor=tk.NW).pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame3, text=" BiliBili", font=("Arial, 15"), anchor=tk.NW).pack(side=tk.TOP, fill=tk.X)

        items_list = tk.Frame(frame3)
        items_list.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        # tk.Label(frame3, text=" Input Setting", font=("Arial, 15"), anchor=tk.NW).pack()
        # tk.Label(items_list, text=" item1", font=("Arial, 15"), bg="Lavender", width=20).grid(row=0, column=0, padx=1)
        # tk.Label(items_list, text=" item2", font=("Arial, 15"), bg="Lavender", width=8).grid(row=0, column=1, padx=1)
        t1 = tk.Text(items_list, width=45, height=28)
        t1.grid(row=0, column=0, padx=10)
        # t1.config(state=tk.DISABLED)
        t2 = tk.Text(items_list, width=45, height=28)
        t2.grid(row=0, column=1, padx=10)
        # t2.config(state=tk.DISABLED)
        t3 = tk.Text(items_list, width=45, height=28)
        t3.grid(row=0, column=2, padx=10)
        # t3.config(state=tk.DISABLED)

        t1.insert(tk.END, "111")
        t2.insert(tk.END, "222")
        t3.insert(tk.END, "333")

        tk.Label(frame3, text="", font="Arial, 5", anchor=tk.NW).pack(side=tk.TOP, fill=tk.X)
        blank_row = tk.Label(frame3, text="", font="Arial, 15", anchor=tk.NW)
        blank_row.pack(side=tk.TOP, fill=tk.X)
        tk.Button(blank_row, text="stop", width=15, height=2, command=lambda: self.run(
            sum_length, canvas_progress_bar, canvas_shape, canvas_text)).pack(side=tk.TOP)

        return frame3

    def frame4_inter(self, frame4):
        tk.Label(frame4, text=" Bit         Output").pack(anchor=tk.NW)
        scroll2 = tk.Scrollbar(frame4)
        scroll2.pack(side=tk.RIGHT, fill=tk.Y)

        self.outputBox = tk.Listbox(frame4, bd=1, selectmode=tk.SINGLE, yscrollcommand=scroll2.set, height=8, width=65)
        self.outputBox.pack(side=tk.LEFT)
        scroll2.config(command=self.outputBox.yview)
        return frame4

    # Initial GUI
    def initial_gui(self):
        # Change tag
        def change_tag(tag):
            frame3.pack_forget()
            frame4.pack_forget()
            frame5.pack_forget()
            if tag == 0:
                frame3.pack(fill=tk.X)
            elif tag == 1:
                frame4.pack(fill=tk.X)
            elif tag == 2:
                frame5.pack(fill=tk.X)

        window = tk.Tk()
        # 设置标题
        window.title(self.TITLE)
        # 设置菜单
        self.menu_set(window)
        # Place GUI on the center of screen
        self.place_gui(window)
        # 每个页面的名字列表, 注意，有多少个label，就有多少个tk.Radiobutton
        label_list = ["Input", "Output", "Other"]
        tag_num = [0, 1, 2]

        # Tag: 0 --> input; 1 --> output; 2 --> other
        frame2 = tk.Frame(window)
        frame2.pack(fill=tk.Y, pady=10, anchor=tk.NW)
        tag = tk.IntVar()
        tag_width = 23
        tk.Radiobutton(frame2, text=label_list[tag_num[0]], command=lambda: change_tag(tag_num[0]), width=tag_width,
                       variable=tag, value=0, bd=1,
                       indicatoron=0).grid(column=0, row=1)
        tk.Radiobutton(frame2, text=label_list[tag_num[1]], command=lambda: change_tag(tag_num[1]), variable=tag,
                       width=tag_width, value=1, bd=1,
                       indicatoron=0).grid(column=1, row=1)
        tk.Radiobutton(frame2, text=label_list[tag_num[2]], command=lambda: change_tag(tag_num[2]), variable=tag,
                       width=tag_width, value=2, bd=1,
                       indicatoron=0).grid(column=2, row=1)

        # frame3 --> Input
        frame3 = tk.Frame(window, height=300, bg="white")
        frame3 = self.frame3_inter(frame3)

        # frame4 --> Output
        frame4 = tk.Frame(window, height=350, bg="blue")
        frame4 = self.frame4_inter(frame4)

        # frame5 --> Other
        frame5 = tk.Frame(window, height=350, bg="yellow")

        window.mainloop()


if __name__ == "__main__":
    tbm = TestBenchMaker()
    tbm.initial_gui()
