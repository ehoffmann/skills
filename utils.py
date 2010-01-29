# Some "in house" utilities functions

def facto(n):
    if n == 1:
        return 1
    else:
        return facto( n - 1) * n 
