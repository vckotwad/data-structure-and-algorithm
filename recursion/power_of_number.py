def power(base,exp):
    if exp==0:
        return 1
    if exp==1:
        return base
    return base*power(base,exp-1)

print(power(2,5))