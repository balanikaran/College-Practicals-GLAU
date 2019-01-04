class Bmi :
    def __init__(self, name, weight, height, age = 20):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height
    
    def getBmi(self) :
        return (self.weight / (self.height)**2 )

    def getStatus(self) :
        bmi = self.getBmi()
        print("Name: {}\nAge: {}\nWeight: {}\nHeight: {}\nBMI: {}".format(self.name, self.age, self.weight, self.height, bmi))
        if bmi < 16 :
            print("Thin")
        elif bmi < 25 :
            print("Normal")
        elif bmi < 
    
myBmi = Bmi("Deepak", 70, 1.55, 20)
myBmi.getStatus()
