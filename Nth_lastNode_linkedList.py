#With this program we can find the nth node from the tail of the linked list
# here the concept is simple
#take two pointers
def nth_to_last(n,head):
    #let's call one pointer as jumpNode and another as regularNode
    jumpNode=head
    regNode=head

    #now let's move the jump pointer to nth place , for ex 5th position
    for i in range(n-1):
        if not jumpNode.nextNode:
            raise LookupError("Error: n is larger than linked list")
        jumpNode=jumpNode.nextNode

    #now lets move jumpNode and regNode
    #loop will be breaked when jumpNode reaches the tail and by that time regNode will be n nodes far from the tail
    while jumpNode.nextNode:
        jumpNode=jumpNode.nextNode
        regNode=regNode.nextNode
    return regNode

class Node(object):
    def __init__(self,value):
        self.value=value
        self.nextNode=None

x=Node(1)
y=Node(2)
z=Node(3)
a=Node(11)
b=Node(21)
c=Node(31)

x.nextNode=y
y.nextNode=z
z.nextNode=a
a.nextNode=b
b.nextNode=c

d=nth_to_last(3,x)
print(d.value)


