#this is damn complex way of writing a program
#I used mostly lambda , map ,reduce concepts to write this  program
from functools import reduce
import re
import sys


def cc_format(card_no):
    # replace any white spaces and -
    card_no=card_no.replace(" ","")
    card_no = card_no.replace("-","")
    return card_no

def reduce_cc(a,func):
    #here we are adding the digits of the number supplied
    l=list(str(a))
    l=map(func,l)
    return reduce(lambda x,y:x+y,l)

def odd_double(i):
    # a credit card logic ,even numbers are multipled by 2 and if it is > 9 then we add that numbers digit i.e reduce
    i=int(i)*2
    if i>9:
        i=reduce_cc(i,int)
    return i

def cc_luhn_check(card_no):
    #split the card
    odd=card_no[0::2]
    even=card_no[1::2]

    odd_sum=reduce_cc(odd,odd_double)
    print(odd_sum)
    even_sum=reduce_cc(even,int)
    print(even_sum)
    total_sum=odd_sum+even_sum
    if total_sum%10==0:
        return True
    else:
        return False

if __name__=='__main__':
    """Enter the credit card number although we enter a number it will be converted to string by default"""
    card_no=input("Enter the credit card number \n")
    print("your credit card number is",card_no)
    card_no=cc_format(card_no)
    if cc_luhn_check(card_no):
        print("Credit Card Number is Valid")
    else:
        print("Credit Card Number is Invalid")