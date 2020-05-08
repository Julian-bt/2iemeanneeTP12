def listSum(l):
    if len(l)==0:
        return 0
    somme=l[-1]
    del l[-1]
    return listSum(l)+somme



print(listSum([])) # 0
print(listSum([42])) # 42
print(listSum([3,1,5,2])) # 11
