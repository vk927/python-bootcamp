#sequential search of the array for an element
# time complexity is O(N) as it needs to search whole arreay to find the element

def seq_search(arr,element):
    i=0
    found=False
    while i<len(arr) and not found:
        if arr[i]==element:
            found=True
        else:
            i+=1

    return found


x=list(input("Enter the input array \n"))
e=input("Enter the input search element \n")
print("Element is in array",seq_search(x,e))




