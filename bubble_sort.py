#this is bubble sort program
#this program has complexity of O(N^2) complexity


def bubble_sort(arr):
    # range from n-1 to 0
    # i value will be from n-1 to 0 (reversing the ranges)
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                tmp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=tmp
    return arr

arr=[4,6,1,8,3]
print(bubble_sort(arr))