class Account:

    def __init__(self, id = 0, balance = 100.0, annualInterestRate = 0.0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id

    def setId(self, id = 0):
        self.__id = id

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance = 100.0):
        self.__balance = balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self, annualInterestRate = 0.0):
        self.__annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12

    def getMonthlyInterest(self):
        interest = self.__balance * self.getMonthlyInterestRate()
        self.__balance += interest
        return interest

    def withdraw(self, amount = 0.0):
        self.__balance -= amount

    def deposit(self, amount = 0.0):
        self.__balance += amount


id, balance, rate = input().split()
w = (input().split())[1]
d = (input().split())[1]
myAccount = Account(int(id), float(balance), float(rate))
myAccount.withdraw(float(w))
myAccount.deposit(float(d))
interest = myAccount.getMonthlyInterest()
print(myAccount.getId(), myAccount.getBalance(), myAccount.getMonthlyInterestRate(), interest)