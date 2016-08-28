#we can reverse a string in 3 ways, but for interviews purpose don't prefer python in built methods
string=input("Enter the sentence you want to reverse")

l=[]
x=0
y=''
for i in string:
    if i != ' ':
        y=y+i
    else:
        x+=1
        l.append(y)
        y=''
l.append(y)
print("The reversed sentence is"," ".join(reversed(l)))


# x=s.split()
# x.reverse()
# print(" ".join(x))

# x=s.split()
# y=x[::-1]
# print(" ".join(y))
