def powerOfTwo(n):
    if n & (n-1) == 0:
        return True
    else:
        return False


print(powerOfTwo(4))