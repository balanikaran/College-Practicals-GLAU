# sum of digits of a number using recursion...

def superDigitSum(superNumber):
    sum = 0
    if superNumber <= 0:
        sum = 0
    elif superNumber == 1:
        sum = 1
    else:
        sum = superNumber%10 + superDigitSum(superNumber//10)
    
    if(sum > 9):
        sum = superDigitSum(sum)

    return sum

print(superDigitSum(9875987598759875))