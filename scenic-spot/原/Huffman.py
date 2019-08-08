from PrioQueue import PrioQueue, PrioQueueError
from BiTree import BiTNode, print_BiTNodes


class HTNode(BiTNode):

    def __lt__(self, othernode):
        return self.data < othernode.data


class HuffmanPrioQ(PrioQueue):

    def number(self):
        return len(self.elems)


def HuffmanTree(weights):
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()
