from tkinter import *
import tkinter.messagebox
from Administrator import *


def addc(): # 添加景点窗口
    def adc():
        AddContent(' '.join([name.get(), dist.get(), typ.get()]))
        tkinter.messagebox.showinfo('', '添加成功！')
        global contentdict
        contentdict = ContentDict()
    ac = Tk()
    ac.title('添加景点内容')
    Label(ac, text='景点名称:').grid(row=0, column=0)
    name = Entry(ac, width=10)
    name.grid(row=0, column=1)
    Label(ac, text='景点地区:').grid(row=1, column=0)
    dist = Entry(ac, width=10)
    dist.grid(row=1, column=1)
    Label(ac, text='景点类型:').grid(row=2, column=0)
    typ = Entry(ac, width=10)
    typ.grid(row=2, column=1)
    Button(ac, text='确认', command=adc).grid(columnspan=2)
    ac.mainloop()


def editc(): # 修改景点窗口
    def edc():
        p = contentdict.get(name.get())
        if p == None:
            tkinter.messagebox.showwarning('', '没有这个景点！')
        else:
            EditContent(p, ' '.join([name.get(), dist.get(), typ.get()]))
            tkinter.messagebox.showinfo('', '修改成功！')
            global contentdict
            contentdict = ContentDict()

    ec = Tk()
    ec.title('修改景点内容')
    Label(ec, text='景点名称').grid(row=0, column=0)
    name = Entry(ec, width=10)
    name.grid(row=0, column=1)
    Label(ec, text='景点地区').grid(row=1, column=0)
    dist = Entry(ec, width=10)
    dist.grid(row=1, column=1)
    Label(ec, text='景点类型').grid(row=2, column=0)
    typ = Entry(ec, width=10)
    typ.grid(row=2, column=1)
    Button(ec, text='确认', command=edc).grid(columnspan=2)
    ec.mainloop()


def delc(): # 删除景点窗口
    def dec():
        p = contentdict.get(name.get())
        if p == None:
            tkinter.messagebox.showwarning('', '没有这个景点！')
        else:
            DelContent(p)
            tkinter.messagebox.showinfo('', '删除成功！')
            global contentdict
            contentdict = ContentDict()

    dc = Tk()
    dc.title('删除景点内容')
    Label(dc, text='景点名称').grid(row=0, column=0)
    name = Entry(dc, width=10)
    name.grid(row=0, column=1)
    Button(dc, text='确认', command=dec).grid(columnspan=2)
    dc.mainloop()


def adedl(): # 添加修改路线窗口
    def aedl():
        p = contentdict.get(start.get())
        if p == None:
            tkinter.messagebox.showwarning('', '没有这个景点！')
        else:
            AELink(p, [end.get(), time.get(), money.get(), line.get()])
            tkinter.messagebox.showinfo('', '修改成功！')

    ael = Tk()
    ael.title('添加路线')
    Label(ael, text='出发地').grid(row=0, column=0)
    start = Entry(ael, width=10)
    start.grid(row=0, column=1)
    Label(ael, text='目的地').grid(row=1, column=0)
    end = Entry(ael, width=10)
    end.grid(row=1, column=1)
    Label(ael, text='金钱花费').grid(row=2, column=0)
    money = Entry(ael, width=10)
    money.grid(row=2, column=1)
    Label(ael, text='时间花费').grid(row=3, column=0)
    time = Entry(ael, width=10)
    time.grid(row=3, column=1)
    Label(ael, text='换乘次数').grid(row=4, column=0)
    line = Entry(ael, width=10)
    line.grid(row=4, column=1)
    Button(ael, text='确认', command=aedl).grid(columnspan=2)
    ael.mainloop()


def dell(): # 删除路线
    def dll():
        p = contentdict.get(start.get())
        q = contentdict.get(end.get())
        if p == None or q == None:
            tkinter.messagebox.showwarning('', '没有这条路线！')
        else:
            DelLink(p, q)
            tkinter.messagebox.showinfo('', '删除成功！')

    dl = Tk()
    dl.title('删除路线')
    Label(dl, text='出发地').grid(row=0, column=0)
    start = Entry(dl, width=10)
    start.grid(row=0, column=1)
    Label(dl, text='目的地').grid(row=1, column=0)
    end = Entry(dl, width=10)
    end.grid(row=1, column=1)
    Button(dl, text='确认', command=dll).grid(columnspan=2)
    dl.mainloop()

top = Tk()
top.title('旅游通数据管理')
top.minsize(170, 90)
Label(top, text='景点内容修改：').grid(columnspan=3, sticky=W)
Button(top, text='添加', command=addc).grid(padx=10, row=1, column=0)
Button(top, text='修改', command=editc).grid(padx=10, row=1, column=1)
Button(top, text='删除', command=delc).grid(padx=10, row=1, column=2)
Label(top, text='景点路线修改：').grid(columnspan=3, sticky=W)
Button(top, text='添加', command=adedl).grid(padx=10, row=3, column=0)
Button(top, text='修改', command=adedl).grid(padx=10, row=3, column=1)
Button(top, text='删除', command=dell).grid(padx=10, row=3, column=2)
top.mainloop()
