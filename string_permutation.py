def permute(s):
    op=[]

    #base case
    if len(s)==1:
        op=[s]
    else:
        #here we will enumerate i.e we take out index and the char from the input string
        for i,char in enumerate(s):
            #now take out the ith char and concate rest of the rest of elements into a string
            #pass this rest of elements string as arguments to the recusion permute ()
            #permute decreses string to 1 char and returns that as base case

            for perm in permute(s[:i]+s[i+1:]):
                #we get to this point only after the we found all permutations of  rest of elements of s when i is removed
                #perute of 1 char return basecase
                #i.e permute(a) returns a
                #permute(ab) reurns b when i is a and returns a when i is b
                #add the ith char to all permutations
                op+=[char+perm]
                #concats make a+b and b+a

    return op

print(permute(input("Enter the input string you want to find chars combination \n")))