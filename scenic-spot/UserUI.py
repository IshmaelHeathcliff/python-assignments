from tkinter import *
import tkinter.messagebox
from User import *
from search_by_sth import *
from main_way import *

mainweb = AEdges()
rlist = []
rlist_ind = []

def sta(): # 确认最近景点窗口
    global rlist_ind, rlist
    rlist.append(start.get())
    rlist_ind.append(contentdict.get(start.get()))
    tkinter.messagebox.showinfo('', '已确认！')

def name(): # 名称搜索窗口
    def relis(event):
        global rlist, rlist_ind
        result = event.widget['text']
        rlist.append(result)
        ind = contentdict.get(result)
        rlist_ind.append(ind)
        na, dis, ty = clist[0][ind], clist[1][ind], clist[2][ind]

        begin = contentdict.get(start.get())
        ti, mo, li = shortest_many_str_mathe_three(mainweb, begin, ind)
        tkinter.messagebox.showinfo('', '景点信息:\n{} {} {}\n\n路线：\n时间最短:{}\n'
                                    '费用最少:{}\n换乘最少:{}\n\n已选择景点：\n{}'.format(na, dis, ty, ti, mo, li, ' '.join(rlist)))

    namelist = find_by_word(clist[0], nam.get())
    select_name = Tk()
    select_name.title('搜索结果')
    Label(select_name, text='请选择结果').grid(ipadx=30)
    for na in namelist:
        button = Button(select_name, text=na, command=relis)
        button.grid()
        button.bind('<Button-1>', relis)


def dist(): # 按地区搜索窗口
    def name_dist(event):
        def relis(event):
            global rlist, rlist_ind
            result = event.widget['text']
            rlist.append(result)
            ind = contentdict.get(result)
            rlist_ind.append(ind)
            na, dis, ty = clist[0][ind], clist[1][ind], clist[2][ind]

            begin = contentdict.get(start.get())
            ti, mo, li = shortest_many_str_mathe_three(mainweb, begin, ind)
            tkinter.messagebox.showinfo('', '景点信息:\n{} {} {}\n\n路线：\n时间最短:{}\n'
                                        '费用最少:{}\n换乘最少:{}\n\n已选择景点：\n{}'.format(na, dis, ty, ti, mo, li, ' '.join(rlist)))

        dis = event.widget['text']
        namelist = find_by_dist(clist[0], clist[1], dis, nam.get())
        select_name = Tk()
        select_name.title('搜索结果')
        Label(select_name, text='请选择结果').grid(ipadx=30)
        for na in namelist:
            button = Button(select_name, text=na, command=relis)
            button.grid()
            button.bind('<Button-1>', relis)

    district = Tk()
    district.title("按地区搜索")
    Label(district, text='请输入名称，并选择一个地区').grid(columnspan=3, sticky=W)
    nam = Entry(district)
    nam.grid(columnspan=3)
    Label(district, text='可选地区：').grid(columnspan=3, sticky=W)
    c1, c2 = 0, 0
    dists = sorted(set(clist[1]))
    for d in dists:
        button = Button(district, text=d)
        button.grid(row=(9 + c1) // 3, column=c2, sticky=W)
        button.bind('<Button-1>', name_dist)
        if c2 < 2:
            c2 += 1
        else:
            c2 = 0
        c1 += 1


def typ(): # 按类型搜索窗口
    def name_typ(event):
        def relis(event):
            global rlist, rlist_ind
            result = event.widget['text']
            rlist.append(result)
            ind = contentdict.get(result)
            rlist_ind.append(ind)
            na, dis, ty = clist[0][ind], clist[1][ind], clist[2][ind]

            begin = contentdict.get(start.get())
            ti, mo, li = shortest_many_str_mathe_three(mainweb, begin, ind)
            tkinter.messagebox.showinfo('', '景点信息:\n{} {} {}\n\n路线：\n时间最短:{}\n'
                                        '费用最少:{}\n换乘最少:{}\n\n已选择景点：\n{}'.format(na, dis, ty, ti, mo, li, ' '.join(rlist)))

        sort = event.widget['text']
        namelist = find_by_sort(clist[0], clist[2], sort, nam.get())
        select_name = Tk()
        select_name.title('搜索结果')
        Label(select_name, text='请选择结果').grid(ipadx=30)
        for na in namelist:
            button = Button(select_name, text=na, command=relis)
            button.grid()
            button.bind('<Button-1>', relis)

    tp = Tk()
    tp.title('按类型搜索')
    Label(tp, text='请输入名称，并选择一个类型').grid(columnspan=5, sticky=W)
    nam = Entry(tp)
    nam.grid(columnspan=5)
    Label(tp, text='可选地区：').grid(columnspan=5, sticky=W)
    sortlist = ['历史文化', '现代都市', '山区', '海景', '综合']
    for i in range(len(sortlist)):
        button = Button(tp, text=sortlist[i])
        button.grid(row=3, column=i)
        button.bind('<Button-1>', name_typ)


def shortest(event): # 最短路径窗口
    ty = event.widget['text']
    sho = Tk()
    sho.title('路线规划')
    Label(sho, text='已选择景点:').grid(sticky=W)
    Label(sho, text=' '.join(rlist)).grid(sticky=W)
    ind = categ.index(ty)
    sort = ['time', 'money', 'line']
    way = muti_many_solve_str_mathe(
        mainweb, rlist_ind, contentdict.get(start.get()), sort[ind])
    Label(sho, text = ty + ':').grid(stick=W)
    Label(sho, text = way).grid(sticky=W)

    sho.mainloop()


top = Tk()
top.title("旅游通")
Label(top, text='请输入最近景点名称:').grid(columnspan=3, sticky=W)
start = Entry(top)
start.grid(columnspan=3, sticky=W)
Button(top, text='确认', command=sta).grid(columnspan=3)
Label(top, text='搜索景点名称:').grid(columnspan=3, sticky=W)
nam = Entry(top)
nam.grid(columnspan=3, sticky=W)
Button(top, text='确认', command=name).grid(columnspan=3)
Label(top, text='其他搜索方式：').grid(columnspan=3, sticky=W)
Button(top, text='地区', command=dist).grid(row=7, column=0, columnspan=2, sticky=E)
Button(top, text='类型', command=typ).grid(row=7, column=1, sticky=W)
Label(top, text='已选好景点集？规划路线:').grid(columnspan=3, sticky=W)
categ = ['时间最短', '费用最少', '换乘最少']
for i in range(len(categ)):
    button = Button(top, text=categ[i])
    button.grid(row=9, column=i)
    button.bind('<Button-1>', shortest)
top.mainloop()
