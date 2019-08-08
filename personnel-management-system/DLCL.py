class DLNode:  # 结点类

    def __init__(self, elem, pre=None, nxt=None):
        self.elem = elem
        self.pre = pre
        self.nxt = nxt


class DLCList:

    def __init__(self):  # 由尾结点和首结点控制
        self.rear = None
        self.head = None

    def delList(self):
        self.rear = None
        self.head = None

    def isEmpty(self):
        return self.rear is None

    def prepend(self, elem):
        p = DLNode(elem)
        if self.rear is None:  # 空表单独考虑
            p.nxt = p
            p.pre = p
            self.rear = p
            self.head = p
        else:
            p.nxt = self.head
            p.pre = self.rear
            self.rear.nxt = p
            self.head.pre = p
            self.head = p

    def append(self, elem):
        self.prepend(elem)
        self.rear = self.rear.nxt
        self.head = self.head.nxt

    def insert(self, elem, index):
        for i in range(index):
            self.head = self.head.nxt
            self.rear = self.rear.nxt

        self.prepend(elem)

        for i in range(index):
            self.head = self.head.pre
            self.rear = self.rear.pre

    def delHead(self):
        if self.rear.nxt is self.rear:
            self.delList()
        else:
            self.rear.nxt = self.rear.nxt.nxt
            self.head = self.head.nxt
            self.head.pre = self.rear

    def delRear(self):
        self.head = self.rear
        self.rear = self.rear.pre
        self.delHead()

    def dele(self, index):
        for i in range(index):
            self.head = self.head.nxt
            self.rear = self.rear.nxt

        self.delHead()

        for i in range(index):
            self.head = self.head.pre
            self.rear = self.rear.pre

    def forEach(self, proc):
        p = self.head.nxt
        proc(self.head.elem)
        while p is not self.head:
            proc(p.elem)
            p = p.nxt

    def rev(self):
        def inv(p): # 前驱和后继改变方向
            p1 = p.pre
            p2 = p.nxt
            p.pre = p2
            p.nxt = p1

        p = self.head
        while p is not self.rear:
            inv(p)
            p = p.pre
        inv(self.rear)

        # 交换首尾结点
        p1 = self.rear
        self.rear = self.head
        self.head = p1

    def print(self):
        if self.isEmpty():
            print()
            return
        p = self.head
        while p is not self.rear:
            print(p.elem)
            p = p.nxt
        print(self.rear.elem)
