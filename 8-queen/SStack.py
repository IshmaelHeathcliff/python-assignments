class StackUnderflow(ValueError):
    pass


class SStack():

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def top(self):
        if self.elems == []:
            raise StackUnderflow
        return self.elems[len(self.elems) - 1]

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        if self.elems == []:
            raise StackUnderflow
        return self.elems.pop()
