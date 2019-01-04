import time
import math

def checkPrimeKB(number):
    #true =  prime false = not prime
    if(number%2 == 0 and number != 2):
        return False
    else:
        for i in range (3, int(math.sqrt(number)) + 1):
            if(number%i == 0):
                return False
    return True

def checkPrimeHS(n):
    #true = prime false = not prime
    if (n == 2 or n == 3 or n == 5 or n == 7):
        return True
    elif (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0):
        return False
    elif (n == 1):
        return False
    else:
        return True

upRange = input("Enter the max number to find primes: ")
start = time.time()
count = 0
for i in range (2, upRange + 1):
    if(checkPrimeHS(i) != checkPrimeKB(i)):
        print("Result KB: {}".format(checkPrimeKB(i)))
        print("Result HS: {}".format(checkPrimeHS(i)))
        print("{} Glitch".format(i))
        count = count + 1
print("Time taken in seconds: {}".format(time.time() - start))
print(count)
