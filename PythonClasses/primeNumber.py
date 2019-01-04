import time
import math

count = 0

def checkPrimeKB(number):
    #true =  prime false = not prime
    if(number%2 == 0 and number != 2):
        return False
    else:
        for i in range (3, int(math.sqrt(number)) + 1):
            if(number%i == 0):
                return False
    global count
    count = count + 1
    return True

def checkPrimeHS(n):
    #true = prime false = not prime
    if (n == 2 or n == 3 or n == 5 or n == 7):
        # print("{} is a Prime Number".format(n))
        return True
    elif (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0):
        # print("{} is not a Prime Number".format(n))
        return False
    elif (n == 1):
        # print("{} is not a Prime Number".format(n))
        return False
    else:
        # print("{} is a Prime Number".format(n))
        return True


upRange = input("Enter the max number to find primes: ")
start = time.time()
for i in range (2, upRange + 1):
    print("{} >> {}".format(i, checkPrimeKB(i)))
print("Time taken in seconds: {}".format(time.time() - start))
print("Total primes in range: {}".format(count))