#this is a tree implementation
#tree is a special kind of list where  0th element is root and 1st element is list(left tree) ,2nd eleemnt is list(right tree)

def tree(r):
    return [r,[],[]]

def insertLeft(r,newBranch):
    t=r.pop(1)
    if len(t)>1:
        r.insert(1,[newBranch,t,[]])
    else:
        r.insert(1,[newBranch,[],[]])
    return r

def insertRight(r,newBranch):
    t=r.pop(2)
    if len(t)>1:
        r.insert(2,[newBranch,[],t])
    else:
        r.insert(2,[newBranch,[],[]])
    return r

def getRoot(r):
    return r[0]

def setRoot(r,val):
    r[0]=val

def getRight(r):
    return r[2]

def getLeft(r):
    return r[1]

r=int(input("Enter the root element of the tree \n"))
r=tree(r)

print("the current tree is",r)

x=input("Enter the value of left tree \n")
r=insertLeft(r,x)
print("Now the current tree is ",r)

x=input("Enter the value of right tree \n")
r=insertRight(r,x)
print("Now the current tree is ",r)

print("The left tree is",getLeft(r))

print("The Right tree is",getRight(r))