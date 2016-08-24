#this is damn complex way of writing a program
#
from functools import reduce
import re
import sys


def cc_format(card_no):
    card_no=card_no.replace(" ","")
    card_no = card_no.replace("-","")
    return card_no

def reduce_cc(st):
    l=list(str(st))
    l=map(int,l)
    return reduce(lambda x,y:x+y,l)

def odd_double(i):
    i=int(i)*2
    if i>9:
        i=reduce_cc(i)
    return i

def odd_map(st):
    l=list(st)
    l=map(odd_double,l)
    return reduce(lambda x, y: x + y, l)

def cc_luhn_check(card_no):
    odd=card_no[0::2]
    even=card_no[1::2]

    odd_sum=odd_map(odd)
    even_sum=reduce_cc(even)
    total_sum=odd_sum+even_sum
    if total_sum%10==0:
        return True
    else:
        return False

if __name__=='__main__':
    card_no=input("Enter the credit card number \n")
    print("your credit card number is",card_no)
    card_no=cc_format(card_no)
    if cc_luhn_check(card_no):
        print("Credit Card Number is Valid")
    else:
        print("Credit Card Number is Invalid")