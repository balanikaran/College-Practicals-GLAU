# code for dynamic checking of a card number entered by user either valid or invalid
# FROM RIGHT ELEMENT > DOUBLE EVERY SECOND ELEMENT IN THE CARD NUMBER > IF THE NUMBER BECOMES GREATER THAN 10
# AFTER DOUBLING, ADD ITS DIGITS TO MAKE IT LESS THAN 10 > SOME ALL THE ELEMENTS > IF SUM MOD 10 IS 0 THEN NUMBER IS VALID

# if the size of card length is odd: double odd indexed elements
# for even: double even indexed elements


############################################################################
# FUNCTION FOR CHECKING EVEN SIZED CARD NUMBER
def checkForEvenCardNumbers(cardNumberList):
    checkForCardIssuer(cardNumberList)
    for i in range(0, len(cardNumberList), 2):
            doubledNumber = cardNumberList[i] * 2
            if(doubledNumber > 9):
                cardNumberList[i] = sumOfDigits(doubledNumber)
            else:
                cardNumberList[i] = sumOfDigits(doubledNumber)
    return luhnLastStepModTen(cardNumberList)

############################################################################
# FUNCTION FOR CHECKING EVEN SIZED CARD NUMBER
def checkForOddCardNumbers(cardNumberList):
    checkForCardIssuer(cardNumberList)
    for i in range(1, len(cardNumberList), 2):
            doubledNumber = cardNumberList[i] * 2
            if(doubledNumber > 9):
                cardNumberList[i] = sumOfDigits(doubledNumber)
            else:
                cardNumberList[i] = sumOfDigits(doubledNumber)
    return luhnLastStepModTen(cardNumberList)

############################################################################
# FUNCTION FOR ADDING DIGITS OF A NUMBER
def sumOfDigits(num):
   sum = 0
   while num:
       sum, num = sum + num % 10, num // 10
   return sum

############################################################################
# FUNCTION FOR ADDING DIGITS OF A NUMBER
def luhnLastStepModTen(cardNumberList):
    sum = 0
    for i in range (0, len(cardNumberList)):
        sum = sum + cardNumberList[i]
    
    if(sum % 10 == 0):
        return True
    else:
        return False

############################################################################
# FUNTION FOR CHECKING THE ISSUER OF THE CARD
def checkForCardIssuer(cardNumberList):
    cardIssuer = ""
    if(cardNumberList[0] == 3 and cardNumberList[1] == 7):
        cardIssuer = "American"
    if(cardNumberList[0] == 6 and cardNumberList[1] == 5 and cardNumberList[2] == 2 and cardNumberList[3] == 1):
        cardIssuer = "American"
    if(cardNumberList[0] == 4):
        cardIssuer = "VISA"
    if(cardNumberList[0] == 5):
        cardIssuer = "MasterCard"
    if(cardNumberList[0] == 6):
        cardIssuer = "Discover"

    print("Card Issuer: ",cardIssuer)

############################################################################
# START OF CODE, PROMPT FOR CARD NUMBER
print("enter the card number:")
cardNumberString = input("Card Number: ")

if len(cardNumberString) >= 13 and len(cardNumberString) <= 19:
    cardNumberList = list(map(int, cardNumberString))
    print(cardNumberList)

    if(len(cardNumberList) % 2 == 0):
        if(checkForEvenCardNumbers(cardNumberList)):
            print("CARD NUMBER IS VALID")
        else:
            print("CARD NUMBER IS INVALID")
    else:
        if(checkForOddCardNumbers(cardNumberList)):
            print("CARD NUMBER IS VALID")
        else:
            print("CARD NUMBER IS INVALID")
        
else:
    print("INVALID INPUT TYPE, LENGTH OF CARD INCORRECT!")

