def binary(n):
    assert int(n)==n,'the parameters must be an integer'
    if n==0:
        return 0
    else:
        return n%2 + 10*binary(int(n/2))
print(binary(13))