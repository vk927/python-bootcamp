#thhis is ordered sequential search
#here the array is sorted before searching

#here what happens is we don't need to search whole array to find any element
# -we need to check the elements value and compare it with arrays elements valus if at some point
#we croos the value then we need to quit the loop as there is no chance ti find the elemenet
#as we crossed the value

def ord_seq_search(arr,ele):
    i=0
    found=False
    stopped=False
    while i<len(arr) and not found and not stopped:
        if arr[i]>6:
            found=True
        elif arr[i]>ele:
            stopped=True
        else:
            i+=1
    return found


ar=[1,3,6,9,10]

print(ord_seq_search(ar,3))

print(ord_seq_search(ar,8))






