s=input("enter the string to compress \n")
l=len(s)

if l==0:
    print("String is empty")
elif l==1:
    print("compressed string is",s[0],"1")
else:
    r=''
    cnt=1
    i=1
    while i<l:
        if s[i]==s[i-1]:
            cnt+=1
        else:
            r=r+s[i-1]+str(cnt)
            cnt=1
        i+=1
    r = r + s[i - 1] + str(cnt)
    print("compressed string is",r)






