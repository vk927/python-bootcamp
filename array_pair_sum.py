import re
s = input("eneter the list of numbers")
s=s.replace(" ","")
s=re.sub(r"\[\]","",s)
l = list(map(int,s[0::1]))
k=int(input("Enter the input "))

test=set()
result=set()

for i in l:
    target=k-i

    if target not in test:
        test.add(i)
    else:
        result.add(((min(i,target)),(max(i,target))))
print("There are ",len(result),"pairs of numbers in list")
print(test,"------------")
print(result)
