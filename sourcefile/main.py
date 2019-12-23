import tkinter as tk


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

    def frame3_inter(self, frame3):
        frame3.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame3, text=" Bit         Input").pack(side=tk.TOP, anchor=tk.W)
        scroll = tk.Scrollbar(frame3)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.inputBox = tk.Listbox(frame3, bd=1, selectmode=tk.SINGLE, yscrollcommand=scroll.set, height=8)
        self.inputBox.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, expand=tk.YES)
        scroll.config(command=self.inputBox.yview)

        # Input setting
        width = 10
        frameInputSet = tk.Frame(frame3, bg="white")
        frameInputSet.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        tk.Label(frameInputSet, text="  Input Setting").grid(row=0, column=0, pady=5)
        tk.Label(frameInputSet, text="  Signal Type", width=width).grid(row=1, column=0)
        # Tpye: 0 --> clock; 1 --> reset; 2 --> custom
        type = tk.IntVar()
        tk.Radiobutton(frameInputSet, text="Clock", variable=type, value=0,
                       command=lambda: self.change_type(0, clockSet, resetSet, customSet), bd=1,
                       indicatoron=0, width=width).grid(row=1, column=1, padx=10)
        tk.Radiobutton(frameInputSet, text="Reset", variable=type, value=1,
                       command=lambda: self.change_type(1, clockSet, resetSet, customSet), bd=1,
                       indicatoron=0, width=width).grid(row=1, column=2, padx=10)
        tk.Radiobutton(frameInputSet, text="Custom", variable=type, value=2,
                       command=lambda: self.change_type(2, clockSet, resetSet, customSet), bd=1,
                       indicatoron=0, width=width).grid(row=1, column=3, padx=10)
        # Clock setting
        clockSet, initalValue, converse = self.clock_set(frame3)
        # Reset setting
        resetSet = self.reset_set(frame3, initalValue, converse)
        # Custom setting
        customSet = self.custom_set(frame3, initalValue)
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

        # Tag: 0 --> input; 1 --> output; 2 --> other
        frame2 = tk.Frame(window)
        frame2.pack(fill=tk.Y, pady=10)
        tag = tk.IntVar()
        tag_width = 23
        tk.Radiobutton(frame2, text="Input", command=lambda: change_tag(0), width=tag_width,
                       variable=tag, value=0, bd=1,
                       indicatoron=0).grid(column=0, row=1)
        tk.Radiobutton(frame2, text="Output", command=lambda: change_tag(1), variable=tag,
                       width=tag_width, value=1, bd=1,
                       indicatoron=0).grid(column=1, row=1)
        tk.Radiobutton(frame2, text="Other", command=lambda: change_tag(2), variable=tag,
                       width=tag_width, value=2, bd=1,
                       indicatoron=0).grid(column=2, row=1)

        # frame3 --> Input
        frame3 = tk.Frame(window, height=300, bg="red")
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
