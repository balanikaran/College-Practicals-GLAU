sortedArray = [1,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,5,6]
#sortedArray = [1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,4,5,6]

# majorityLength = (len(sortedArray)//2) - 1
# for i in range(0, len(sortedArray)-1):
#     if(sortedArray[i] == sortedArray[i+(majorityLength-1)]):
#         print("{} is in majority... :)".format(sortedArray[i]))
#         print("{}".format(i+(majorityLength-1)))
#         break

def searchBound(sortedArray, left, right, midElementValue):
    middleInd = left + (right-left)//2
    middleVal = sortedArray[middleInd]
    while(left < right):
        if middleVal == midElementValue:
            return searchBound(sortedArray, left, middleInd-1, midElementValue)
        if middleVal < midElementValue:
            return searchBound(sortedArray, middleInd+1, right, midElementValue)
    return left


def main():
    lengthOfArray = len(sortedArray)
    midElementIndex = 0 + (lengthOfArray-0)//2
    midElementValue = sortedArray[midElementIndex]
    print("{} {}".format(midElementIndex, midElementValue))
    leftBound = searchBound(sortedArray, 0, midElementIndex, midElementValue)
    print(leftBound)

main()