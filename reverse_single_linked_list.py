class Node(object):
    def __init__(self,value):
        self.value=value
        self.nextNode=None

def reverse(node):
    current=node
    previous=None
    nextNode=None

    while current:
        nextNode=current.nextNode
        current.nextNode=previous
        previous=current
        current=nextNode

    return previous

x=Node(1)
y=Node(2)
z=Node(3)

x.nextNode=y
y.nextNode=z

print(x.value)
print(x.nextNode.value)
print(y.nextNode.value)

reverse(x)
print(z.value)
print(z.nextNode.value)
print(y.nextNode.value)
