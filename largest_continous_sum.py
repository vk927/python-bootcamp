#this program has time complexity O(N)

l=[1,2,3,4,-1,2,-10,2,3]
print(l)

if len(l)==0:
    print("no elements in list")
else:
    max_sum=local_sum=l[0]
    for i in l[1:]:
        local_sum=max(local_sum+i,i)
        max_sum=max(max_sum,local_sum)
    print("Max sum is ",max_sum)





