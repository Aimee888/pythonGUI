from play.canvasdemo import *
from frame import *


class InitFace:
    def __init__(self, master):
        self.master = master

        # 窗口标题
        self.master.title('Main Interface')
        self.master.geometry('1024x768')
        self.master.resizable(False, False)
        # window.config(bg='#535353')

        # 菜单选项
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        filemenu1 = Menu(menubar, tearoff=0)
        filemenu2 = Menu(menubar, tearoff=0)
        filemenu3 = Menu(menubar, tearoff=0)
        filemenu4 = Menu(menubar, tearoff=0)
        # 给menu添加一个选项
        menubar.add_cascade(label='menu1', menu=filemenu1)
        menubar.add_cascade(label='menu2', menu=filemenu2)
        menubar.add_cascade(label='menu3', menu=filemenu3)
        menubar.add_cascade(label='menu4', menu=filemenu4)
        # menu1添加子选项
        filemenu1.add_command(label='新建...', command=click())
        filemenu1.add_command(label='打开...', command=click())
        filemenu1.add_command(label='保存...', command=click())
        filemenu1.add_command(label='关闭填写...', command=window.quit)

        self.change(1)

    def change(self, num):
        switch = {
            1: FrameOne,
            2: FrameTwo
        }
        switch[num](self.master)


def click():
    print("点击了一次")


if __name__ == "__main__":
    window = Tk()

    InitFace(window)

    window.mainloop()
