def fib_rec(n):
    #base case
    if n==0 or n==1:
        return n
    #recursion
    else:
        return fib_rec(n-1)+fib_rec(n-2)

print(fib_rec(10),"- with recursion")

def fib_itr(n):
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    return a

print(fib_itr(10),"- with iteration")

cache={}
def fib_mem(n):

    #base case
    if n==0 or n==1:
        return n
    #from memoize
    if n in cache:
        return cache[n]
    #recursive case when we didn't find in memoize
    cache[n]=fib_mem(n-1)+fib_mem(n-2)

    return cache[n]

print(fib_mem(10),"- with dynamic programming")