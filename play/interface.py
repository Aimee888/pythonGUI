from tkinter import *
from tkinter.tix import Tk, Control, ComboBox  # 升级的组合控件包
from tkinter.messagebox import showinfo, showwarning, showerror #各种类型的提示框


def resize(ev=None):
    lable.config(font='Helvetica -%d bold' % scale.get())


def click():
    print("点击了一次")


if __name__ == "__main__":
    # root是布局的根节点
    root = Tk()  # 初始化tk
    # 设置窗口标题
    root.title("hello tkinter")
    # 设置窗口大小 注意：是X 不是*
    root.geometry("1024x768")
    # 设置窗口是否可以变化长/宽，False不可变，True可变
    root.resizable(width=True, height=True)
    # 引入升级包，这样才能使用升级的组合控件
    root.tk.eval('package require Tix')
    lable = Label(root, text="label", bg="pink", bd=10, font=("Arial", 12), width=8, height=3)
    lable.pack(side=LEFT)

    # 按钮
    """
    command: 点击调用的方法
    activeforeground: 点击时按钮上字的颜色
    activebackground: 点击时按钮的背景颜色
    """
    button = Button(root, text='QUIT', command=root.quit, activeforeground="black", activebackground='blue', bg='red',
                    fg='white')
    button.pack(fill=Y, expand=1)

    # 滑动条
    """
    from_: 滑动条起始值
    to: 滑动条终点值
    origent: 样式 两种样式 一横一竖
    """
    scale = Scale(root, from_=10, to=40, orient=HORIZONTAL, command=resize)
    scale.set(12)
    scale.pack()

    # 数字选择框
    """
    integer: 是否为整数
    max: 最大值
    min: 最小值
    value: 初始值
    step: 步长
    """
    ct = Control(root, label='Number:', integer=True, max=12, min=2, value=2, step=2)
    ct.label.config(font='Helvetica 14 bold')
    ct.pack()

    # 下拉选择框
    """
    label: 前面要显示的字
    editable: 控制是否可更改
    insert(): 给下拉选择框添加选项
    """
    cb = ComboBox(root, label='Type:', editable=True)
    for animal in ('dog', 'cat', 'hamster', 'python'):
        cb.insert(END, animal)
    cb.pack()

    # 菜单选项
    menubar = Menu(root)
    root.config(menu=menubar)
    filemenu = Menu(menubar, tearoff=0)
    # 给menu添加一个选项
    menubar.add_cascade(label='文件', menu=filemenu)
    # 添加子选项
    filemenu.add_command(label='新建...', command=click())
    filemenu.add_command(label='打开...', command=click())
    filemenu.add_command(label='保存...', command=click())
    filemenu.add_command(label='关闭填写...', command=root.quit)

    # frame相当于一个局部的窗体，可以用来装载其他控件
    frame1 = Frame(root)
    frame1.pack(fill=X)
    label1 = Label(frame1, text='您的花名：')
    label1.grid(row=1, column=0)

    # 单选框
    frame2 = Frame(root)
    frame2.pack(fill=X)
    label2 = Label(frame2, text='您的性别：')
    label2.grid(row=1, column=0)
    sex = StringVar()
    sex_male = Radiobutton(frame2, text='男', fg='blue', variable=sex, value='男')
    sex_male.grid(row=1, column=2)
    sex_female = Radiobutton(frame2, text='女', fg='red', variable=sex, value='女')
    sex_female.grid(row=1, column=4)

    # 列表
    frame4 = Frame(root)
    frame4.pack(fill=X)
    label4 = Label(frame4, text='4、请删除您不会的变成语言：')
    label4.grid(row=1, column=0)
    listbox = Listbox(frame4)
    listbox.grid(row=1, column=1)
    for item in ["C", "C++", "JAVA", "PYTHON", "R", "SQL", "JS"]:
        listbox.insert(END, item)

    DELETE = Button(frame4, text='删除', command=lambda listbox=listbox: listbox.delete(ANCHOR))
    DELETE.grid(row=1, column=2)
    language = Button(frame4, text='确定')
    language.grid(row=2, column=1)

    # 多选框，onvalue代表被勾选时的值，offvalue代表不被勾选时的值
    frame8 = Frame(root)
    frame8.pack()
    agree = StringVar()
    agree = Checkbutton(frame8, text='我同意', variable=agree, onvalue='确定', offvalue='不确定',)
    agree.grid()
    
    # 容器框
    frame10 = Frame(root)
    frame10.pack()
    group = LabelFrame(frame10, text='特别鸣谢', padx=5, pady=5)
    group.grid()
    w = Label(group, text='容器框')
    w.pack()

    # # 画板
    # window = Tk()
    # canvas = Canvas(window, width=200, height=100, bg="White")
    # canvas.pack()

    # 程序进入消息循环
    # window.mainloop()
    root.mainloop()

