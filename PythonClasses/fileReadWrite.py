def writeToFile(message):
    with open("/Users/karanbalani/Documents/CollegePracticals/PythonClasses/Files/fileReadWrite.txt", "a") as fileObject:
        fileObject.write(message + "\n")

def readFromFile():
    with open("/Users/karanbalani/Documents/CollegePracticals/PythonClasses/Files/fileReadWrite.txt", "r") as fileObject:
        return fileObject.read()

def main():
    writeToFile("Hello, I'm Karan Balani")
    print(readFromFile())

main()