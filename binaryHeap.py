class binaryHeap(object):
    def __init__(self):
        self.heapList=[0]
        self.currentSize=0

    def insert(self,r):
        self.heapList.append(r)
        self.currentSize+=1
        self.percUp(self.currentSize)

    def pencUp(self,i):
        while i//2 > 0:
            if self.heapList[i]<self.heapList[i//2]:
                #swap the elements
                tmp=self.heapList[i//2]
                self.heapList[i//2]=self.heapList[i]
                self.heapList[i]=tmp
            i=i//2

    def pencDown(self,i):
        while (i*2)<=self.currentSize:
            mc=self.minNode(i)
            if self.heapList[mc]<self.heapList[i]:
                #swap
                tmp=self.heaplist[i]
                self.heaplist[i]=self.heapList[mc]
                self.heapList[mc]=tmp
            i=mc

    def minNode(self,i):
        if i*2+1>self.currentSize:
            return i*2
        else:
            if self.heapList[i*2]<self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        tmp=self.heapList[1]
        self.heapList[1]=self.heapList[self.currentSize]
        self.currentSize-=1
        self.heapList.pop()
        self.percDown(1)
        return tmp

    def buildHeap(self,alist):
        i=len(alist)//2
        self.currentSize=len(alist)
        self.heapList=[0]+alist[:]
        while(i>0):
            self.perDown(i)
            i=i-1




