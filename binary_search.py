# def binary_search(arr,ele):
#     first=0
#     last=len(arr)-1
#     found=False
#     while first<=last and not found:
#         mid=(first+last)//2
#         if arr[mid]==ele:
#             found=True
#         elif arr[mid] < ele:
#             first=mid+1
#         else:
#             last=mid-1
#     return found
#
# ar=[1,3,6,9,10]
#
# print(binary_search(ar,3))

#print(binary_search(ar,8))


def rec_binary_search(arr,ele):
    if len(arr)==0:
        return False
    else:
        mid =(len(arr)-1)//2

        if arr[mid]==ele:
            return True
        elif arr[mid]>ele:
            return rec_binary_search(arr[:mid],ele)
        else:
            return rec_binary_search(arr[mid+1:],ele)

ar=[1,3,6,9,10]

print(rec_binary_search(ar,13))


