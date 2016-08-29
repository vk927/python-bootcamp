# This is a class to create stack program
# stack uses LIFO concept
# In Stack we add and remove elements only from one end i.e from top
# Stacks are used for reverse order

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

