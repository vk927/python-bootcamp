class Stack(object):
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        print(self.items==[])

    def push(self,item):
        self.items.append(item)
        print(self.items)

    def pop(self):
        self.items.pop()
        print(self.items)

    def peek(self):
        print(self.items[len(self.items)-1])

    def size(self):
        print(len(self.items))

s=Stack()

s.isEmpty()
s.push("hi")
s.push(1)
s.push(True)
s.push("bye")
s.pop()
s.peek()
s.size()

