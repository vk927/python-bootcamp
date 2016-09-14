#quick sort has worst case O(n^2) time complexity
# but best case and avg case is O(nlogn)
#in all APIs' we use quick_sort as implicit function

def quick_sort(arr):
    start=0
    end=len(arr)-1
    quick_helper(arr, start, end)
    return arr

def quick_helper(arr,start,end):
    if(start<end):
        pIndex=part(arr,start,end)
        quick_helper(arr,start,pIndex-1)
        quick_helper(arr,pIndex+1,end)

def part(arr,start,end):
    pivot=arr[end]
    split_Point=start
    for i in range(start,end):
        if(arr[i]<=pivot):
            tmp=arr[i]
            arr[i]=arr[split_Point]
            arr[split_Point]=tmp
            split_Point+=1

    tmp = arr[split_Point]
    arr[split_Point] = arr[end]
    arr[end] = tmp

    return split_Point


l=[6,56,67,54,23,44,13,11,19,91,4,7,3,9,1]
print(quick_sort(l))


