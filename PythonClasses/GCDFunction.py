def gcdFunction(a = 100, b = 90):
    if a > b:
        upper = b
    elif b >= a:
        upper = a
    
    gcd = 1

    for i in range (2, upper+1):
        if a % i == 0:
            if b % i == 0:
                gcd = i

    print("GCD of {} and {} = {}".format(a, b, gcd))