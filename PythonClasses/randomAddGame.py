import random

def main():
    print("Your Choices: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Calculate BMI")
    choice = input("\nEnter your choice: ")

    if(choice == '1'):
        addition()
    elif(choice == '2'):
        subtraction()
    elif(choice == '3'):
        calculateBMI()
    else:
        print("lol")


def addition():
    a = random.randrange(0,10)
    b = random.randrange(0,10)
    actualSum = a + b
    print("If a = {} and b = {}".format(a, b))
    userSum = input("Answer = ")
    print(userSum)
    if (int)(userSum) == actualSum:
        print("Congratulations you were right!")
    else:
        print("Sorry, the answer was {}".format(actualSum))

def subtraction():
    a = random.randrange(0,10)
    b = random.randrange(0,a+1)
    actualDiff = a - b
    print("If a = {} and b = {}".format(a, b))
    userDiff = input("Answer = ")
        
    if (int)(userDiff) == actualDiff:
        print("Congratulations you were right!")
    else:
        print("Sorry, the answer was {}".format(actualDiff))


def calculateBMI():
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))
    bmi = weight/height**2
    print("Your BMI = {}".format(bmi))
    if(bmi < 18.5):
        print("Underweight")
    
def lotteryGame():
    randomLotteryNumber = random.randrange(10, 100)
    userLotteryNumber = input("Enter your lottery number: ")
    splitLotteryNumber = list(str(randomLotteryNumber))
    splitUserLotteryNumber = list(str(userLotteryNumber))
    if userLotteryNumber < 10 or userLotteryNumber > 99:
        print("Invalid lottery number, you lost!")
    elif userLotteryNumber == randomLotteryNumber:
        print("You have won $10,000!")
    elif 

main()