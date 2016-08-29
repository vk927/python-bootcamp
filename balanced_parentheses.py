#how to balance parentheses

s="hi hello (fhs)fuh [hfsjfh] hsj) hshfbjh"
stack=[]
open="([{"
close=")]}"
matches=(('(',')'),('[',']'),('{','}'))
for i in s:
    if i in open:
        stack.append(i)
    elif i in close:
        if len(stack)==0:
            print("mis placed")
            break
        else:
            last_open=stack.pop()
            if(last_open,i) not in matches:
                print("again misplaced")
                break
    else:
        continue


