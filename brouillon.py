def product(a,b):
    if b==1:
        return a
    return product(a,b-1)+a

print(product(5,2)) # 10 5+5
print(product(9,3)) # 27  9+9+9
