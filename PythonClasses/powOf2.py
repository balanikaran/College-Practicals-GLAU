import math

def powerOfTwo(n):
    result = math.log(n, 2)
    if result%1 == 0:
        return True
    return False

print(powerOfTwo(9))