#insertion sort is the best time complexity for some cases
#insertion sort we take ist element as a list and then we compare 2nd element with it
#if 2nd greater than 1 then place 2nd at its position if not then we need to keep it left side

#same for rest of elements ,so left side we make a sorted list at the end we make a fully sorted list

def insertion_sort(arr):
    for i in range(1,len(arr)):
        currentvalue=arr[i]
        while i>0 and arr[i-1]>currentvalue:
            arr[i]=arr[i-1]
            i=i-1
        arr[i]=currentvalue
    return arr

l=[6,56,67,54,23,44,13,11,19,91,4,7,3,9,1]
print(insertion_sort(l))

# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         currentvalue=arr[i]
#         pos=i
#         while pos>0 and arr[pos-1]>currentvalue:
#             arr[pos]=arr[pos-1]
#             pos=pos-1
#         arr[pos]=currentvalue
#     return arr
#
# l=[6,4,7,3,9,1]
# print(insertion_sort(l))