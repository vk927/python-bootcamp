#string rusing recursioneverse program
#I'm going to reverse a string using recursion

def reverse(s):

    #base case
    if len(s)<=1:
        return s
    #recursive case
    else:
        #here we are splitting the string and attaching the 1st element at tail
        # while recursively calling the reverse function on the rest of the string
        return reverse(s[1:]) + s[0]
s=input("Enter the Input \n")
print(reverse(s))