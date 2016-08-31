#with the fallowing program we can find wether a sentence has words from a given list
s=input("Enter the sentence \n")
s=s.replace(" ","")
def word_split(sent,list,op=[]):
    for w in list:
        if sent.startswith(w):
            op.append(w)
            return word_split(sent[len(w):],list,op)
    return op

x=word_split(s,['hi','hello','bye'])
print(x)

