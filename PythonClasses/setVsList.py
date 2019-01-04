import random
import time

mainList = list(x for x in range (0, 100000))

shuffledList = mainList
random.shuffle(shuffledList)
shuffledSet = set(shuffledList)


print("Searching 10000 elements in LIST")
listAvg = 0
start = time.time()
for i in range (0, 100000):
    if i in shuffledList:
        pass
    # end = time.time()
    # listAvg += (end-start)
end = time.time()
listAvg = end-start

print("Average time in List : {}".format(listAvg))


print("Searching 10000 elements in SET")
setAvg = 0
start = time.time() #millis
for i in range (0, 100000):
    if i in shuffledSet:
        pass
    # end = time.time()
    # setAvg += (end-start)
end = time.time()
setAvg = (end-start)

print("Average time in Set : {}".format(setAvg))

print("Difference = {}".format(setAvg-listAvg))