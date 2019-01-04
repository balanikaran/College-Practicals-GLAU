#prove the value of pi = 3.14 using monte carlo method?
import random
import math

totalHits = 100000.00
successHits = 0
radius = 5.00

for i in range (0, 100000):
    randomX = random.uniform(-5.0,5.0)
    randomY = random.uniform(-5.0,5.0)
    calculatedDistance = math.sqrt(randomX*randomX + randomY*randomY)
    if(radius >= calculatedDistance):
        successHits = successHits + 1

print (((float(successHits))/totalHits)*4.00)