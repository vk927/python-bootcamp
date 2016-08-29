#this program has the time complexity of O(N^2)

s=input("Enter the input string for which you want to check the ")
l=[]
x=True
for i in s:
    if i in l:
        x=False
        break
    else:
        l.append(i)
if x:
    print("Reached end of loop so there are no duplicate chars")
else:
    print("break up")


# if len(set(s))==len(s):
#     print("set function is working and there are no duplicates")
# else:
#     print("there are duplicates")
