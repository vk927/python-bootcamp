class single_linked_list(object):
    def __init__(self,node):
        self.node=node
        self.nextNode=None

a=single_linked_list(1)
b=single_linked_list("*")
c=single_linked_list(3)

a.nextNode=b
b.nextNode=c

x=b.node
y=a.nextNode

print(x)
#print(y)   #these are refernces
#print(a)

print(x==y.node)
