# this program creates  a class queue

class queue(object):
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        print("queue is empty ",self.items==[])

    def enqueue(self,item):
        self.items.insert(0,item)
        print(self.items)

    def dequeue(self):
        self.items.pop()
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