def anagram(str1,str2):
    str1=str1.replace(" ","")
    str2=str2.replace(" ","")

    if len(str1)!=len(str2):
        return False

    count={}

    for i in str1:
        if i in count:
            count[i]+=1
        else:
            count[i]=1

    for i in str2:
        if i in count:
            count[i]-=1
        else:
            count[i]=1

    for k in count:
        if count[k]!=0:
            return False

    return True

test=anagram("maanoj","manoj")
print("Anagram test is",test)

