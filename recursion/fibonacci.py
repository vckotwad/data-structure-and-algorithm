def fib(n):
    assert n>=0 and int(n)==n,"fibonnaci number can't be negative or non integer" #checking for unintentional case
    if n in [0,1]: #defining base case
        return n
    else:
        return fib(n-1)+fib(n-2) #defining recursive case 
print(fib(0))