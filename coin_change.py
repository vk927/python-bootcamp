# def coin_change(target,coins):
#     min_coins=target
#
#     if target in coins:
#         return 1
#     else:
#         for i in [c for c in coins if c<=target]:
#             num_coins=1+coin_change(target-i,coins)
#
#             if num_coins<min_coins:
#                 min_coins=num_coins
#     return min_coins


#Thumb rule is to use a dictionary
#store the results in dictionary and next whenever you need we can resuse them
#dictionary key will be the argument of the function - if multi arguments then key is argument that changes in the recursive function
#value is the result of the recurisve function when we supply the key as argument

res={}
def coin_change(target,coins):
    min_coins=target

    if target in coins:
        res[target]=1
        return 1
    elif target in res:
        return res[target]
    else:
        for i in [c for c in coins if c<=target]:
            num_coins=1+coin_change(target-i,coins)

            if num_coins<min_coins:
                min_coins=num_coins

                res[target]=min_coins
    return min_coins

print(coin_change(74,[1,5,10,25])," - with memoization")
