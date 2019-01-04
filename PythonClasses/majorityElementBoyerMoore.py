unsortedArray = [2,1,4,4,1,3]

# method to find the majority candidate
def majorityCandidate(unsortedArray):
    sizeOfArray = len(unsortedArray)
    majorCandidate = unsortedArray[0]
    countOfMajor = 1

    # loop through for count
    for i in range (1, sizeOfArray-1):
        if unsortedArray[i] == majorCandidate:
            countOfMajor = countOfMajor + 1
        else:
            countOfMajor = countOfMajor - 1
        
        if countOfMajor == 0:
            majorCandidate = unsortedArray[i]
            countOfMajor = 1
    
    confirmMajority(unsortedArray, sizeOfArray, majorCandidate)
    

# confirming the majority of the major candidate
def confirmMajority(unsortedArray, sizeOfArray, majorCandidate):
    countOfMajor = 0
    for i in range (0, sizeOfArray):
        if unsortedArray[i] == majorCandidate:
            countOfMajor = countOfMajor + 1
    
    if countOfMajor > sizeOfArray//2:
        print("Major candidate = {}".format(majorCandidate))
    else:
        print("No major candidate found...")

majorityCandidate(unsortedArray)