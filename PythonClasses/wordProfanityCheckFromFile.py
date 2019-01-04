import urllib2
import requests
import os

def checkProfanityOnline(word):
    url = "http://wdylike.appspot.com/?q=" + word
    requestObject = urllib2.Request(url)
    response = urllib2.urlopen(requestObject)
    result = response.read()
    if(result == "true"):
        return True
    else:
        return False

def checkIfFileIsEmpty():
    size = os.path.getsize("/Users/karanbalani/Documents/CollegePracticals/PythonClasses/Files/prafanityParagraph.txt")
    if(size == 0):
        return False #empty
    else:
        return True #non-empty

# def checkFileForOffensiveWords():
#     with open("/Users/karanbalani/Documents/CollegePracticals/PythonClasses/Files/prafanityParagraph.txt", "r") as filePointer:
        

def main():
    print(checkIfFileIsEmpty())

main()