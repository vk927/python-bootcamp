def shell_sort(arr):
    sublist_len=len(arr)//2

    while sublist_len>0:
        for start in range(sublist_len):
            gap_insert_sort(arr,start,sublist_len)
        sublist_len=sublist_len//2

    return arr

def gap_insert_sort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):
        currentcal=arr[i]
        pos=i
        while pos>=gap and arr[pos-gap]>currentcal:
            arr[pos]=arr[pos-gap]
            pos=pos-gap

        arr[pos]=currentcal

l=[6,56,67,54,23,44,13,11,19,91,4,7,3,9,1]
print(shell_sort(l))


