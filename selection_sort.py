#selection sort is somewhat similar to bubble sort
#but here is selection sort we don't swap all elements in list for each main loop
#here we only do one swap that also we first find highest element in list
# and then we should place at last of list

#next we should loop n-1 elements and find highest element and place it at n-1 position
def selection_sort(arr):
    #loop from n-1 to 0
    #using this we will create sublists
    for i in range(len(arr)-1,0,-1):
        #take max pos as 0 - current max element by default is 0th element
        pos_max=0
        #loop from 1 to n+1
        for location in range(1,i+1):
            #compare peresent element and  current max element
            if arr[location]>arr[pos_max]:
                pos_max=location
        #after finding the max current element of the sublist swap it to the last element of the sublist
        tmp=arr[pos_max]
        arr[pos_max]=arr[i]
        arr[i]=tmp

    return arr

l=[6,4,7,3,9,1]
print(selection_sort(l))
