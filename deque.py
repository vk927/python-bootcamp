class deque(object):
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        print("deque is empty ",self.items==[])

    def addFront(self,item):
        self.items.append(item)
        print(self.items)

    def addRear(self,item):
        self.items.insert(0,item)
        print(self.items)

    def removeFront(self):
        self.items.pop()
        print(self.items)

    def removeRear(self):
        self.items.pop(0)
        print(self.items)

    def size(self):
        print(len(self.items))

d=deque()
d.isEmpty()
d.addFront("hi-f1")
d.addFront("hell0-f2")
d.addRear("bye-r1")
d.addRear("goodbye-r2")
d.removeFront()
d.removeRear()
d.size()