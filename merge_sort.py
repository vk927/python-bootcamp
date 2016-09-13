def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        lefthalf=arr[:mid]
        righthalf=arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                arr[k]=lefthalf[i]
                i+=1
            else:
                arr[k]=righthalf[j]
                j+=1

            k+=1

        while i<len(lefthalf):
            arr[k]=lefthalf[i]
            i+=1
            k+=1

        while j<len(righthalf):
            arr[k]=righthalf[j]
            j+=1
            k+=1

    return arr

l=[6,56,67,54,23,44,13,11,19,91,4,7,3,9,1]
print(merge_sort(l))

