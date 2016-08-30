#how to balance parentheses


s=input("Enter the Input String \n")
stack=[]
#take opening parantheses in one list here,I took it as string
open="([{"
#take closing parentheses in another list here,I took it as string
close=")]}"
#create a set in which we have sets of combination parentheses
matches=(('(',')'),('[',']'),('{','}'))
#loop the input string
for i in s:
    # check if char is in opening parentheses
    if i in open:
        #if char is openening parentheses then append it to the list -- here stack is a list
        stack.append(i)
    # check if char is in closing parentheses
    elif i in close:
        # if lenghth of stack list is zero then we hdon't have a openeing parentheses,so if we get a closing parentheses
        # it should be an error
        if len(stack)==0:
            print("mis placed")
            break
        else:
            #if stack has elements,then pop out the last element i.e opening parentheses
            last_open=stack.pop()
            #make a closing char i with poped out stack open in char
            #check if this pair is in matches set
            if(last_open,i) not in matches:
                #if not in matches then break the loop and program
                print("again misplaced")
                break
    # if not a parentheses then continue
    else:
        continue


