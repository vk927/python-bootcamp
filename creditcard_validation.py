from functools import reduce
import re
import sys


def cc_format(card_no):
    card_no=card_no.replace(" ","")
    card_no = card_no.replace("-","")
    return card_no
def xyz(l):
    l=list(l)
    l=map(int,l)
    return reduce(lambda x,y:x+y,l)


def cc_luhn(card_no):
    odd=card_no[0::2]
    even=card_no[1::2]

    odd_sum=

    even_sum=map(x,())




if __name__=='__main__':
    card_no=input("Enter the credit card number \n")
    print("your credit card number is",card_no)
    card_no=cc_format(card_no)
    cc_luhn(card_no)