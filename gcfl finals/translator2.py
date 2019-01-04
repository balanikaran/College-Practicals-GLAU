def findActual(bString, bEng):
#     qwertyuiopasdfghjklzxcvbnm
#     abcdefghijklmnopqrstuvwxyz
    actualEng = "abcdefghijklmnopqrstuvwxyz"
    eString = ""
    for character in bString:
        if character == '_':
            eString = eString + ' '
        elif not character.isalpha():
            eString = eString + character
        else:
            indexInE = actualEng.find(character.lower())
            if character.isupper():
                eString = eString + (bEng[indexInE]).upper()
            else:
                eString = eString + (bEng[indexInE])
            
    print(eString)
    

t, bEng = input().split(' ')
t = int(t)

for i in range (t):
    findActual(input(), bEng)