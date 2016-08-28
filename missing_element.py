l=[1,3,2]
q=[1,2]

# finding the missing element in O(n^2)
# for i in l:  # O(n)
#     if i not in q: # O(n)
#         print("Missing element is",i)
# so total  O(n*n) = O(n^2)


############################################################################


#finding the missing element in O(NlogN)
# l=sorted(l) #O(logN)
# q=sorted(q)
#
# for i,j in zip(l,q):  #O(N)
#     if i != j:
#         print(i)
#         break
#     print(l[-1])

#so total is O(NlogN)


#############################################################################


# finding the element in O(N)
dc={}

for i in q:
    if i in dc:
        dc[i]+=1
    else:
        dc[i]=1

for i in l:
    if i in dc:
        dc[i]-=1
    else:
        dc[i]=1

for k in dc:
    if dc[k]!=0:
        print(k,"is the missing element")



# another way is to sum up the the arrays  and find the difference between them this also has the O(N)
# but this method is not good for too large numbers and some errors mioght araise with decimals in arrays(lists)


# l_sum=sum(l)
# q_sum=sum(q)
# print("Missed number is ",l_sum-q_sum)
