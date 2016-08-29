# this program creates  a class queue
# WE can do operations in two type -
#    1) add front  remove rear
#    2) add rear remove front


class queue(object):
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        print("queue is empty ",self.items==[])

    # add rear and remove front
    # def enqueue(self,item):
    #     self.items.insert(0,item)
    #     print(self.items)
    #
    # def dequeue(self):
    #     self.items.pop()
    #     print(self.items)

    # add front and remove rear
    def enqueue(self, item):
        self.items.append(item)
        print(self.items)

    def dequeue(self):
        self.items.pop(0)
        print(self.items)

    def size(self):
        print(len(self.items))

q=queue()
q.isEmpty()
q.enqueue("hi")
q.enqueue("hello")
q.enqueue("bye")
q.dequeue()
q.size()