def fact(n):
    assert n>=0 and int(n)==n,"fibonnaci number can't be negative or non integer"
    if n in [0,1]: #provinding base condition to avoid infinite loop
        return 1
    else:
        return n*fact(n-1) #getting the recursive case

print(fact(0))