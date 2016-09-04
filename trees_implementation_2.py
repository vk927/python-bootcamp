#trees implementation using OOPS concepts
#here every node is object ,you can't call it with field name ,you should use reference

class tree(object):
    def __init__(self,value):
        self.key=value
        self.leftNode=None
        self.rightNode=None

    def insertLeft(self,newNode):
        if self.leftNode==None:
            self.leftNode=tree(newNode)
        else:
            t=tree(newNode)
            t.leftNode=self.leftNode
            self.leftNode=t

    def insertRight(self,newNode):
        if self.rightNode==None:
            self.rightNode=tree(newNode)
        else:
            t=tree(newNode)
            t.rightNode=self.rightNode
            self.rightNode=t

    def getRight(self):
        return self.rightNode

    def getLeft(self):
        return self.leftNode

    def setRoot(self,root):
        self.key=root

    def getRoot(self):
        return self.key

r=tree(10)
print("Initial root element is",r.key)

r.insertLeft(5)

print("left node is ",r.getLeft().key)

print("left node is ",r.getLeft().getRoot())

r.insertRight(15)

print("Right node is ",r.getRight().key)

print("Right node is ",r.getRight().getRoot())