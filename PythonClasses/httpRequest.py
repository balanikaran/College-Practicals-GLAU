import urllib2
import requests

def makeRequest():
    url = "https://www.google.co.in"
    requestObject = urllib2.Request(url)
    response = urllib2.urlopen(requestObject)
    print(response.read())

def main():
    makeRequest()

main()