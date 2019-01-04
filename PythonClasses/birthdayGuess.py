matrixSetA = [ [1,3,5,7], [9,11,13,15], [17,19,21,23], [25,27,29,31] ]
matrixSetB = [ [2,3,6,7], [10,11,14,15], [18,19,22,23], [26,27,30,31] ]
matrixSetC = [ [4,5,6,7], [12,13,14,15], [20,21,22,23], [28,29,30,31] ]
matrixSetD = [ [8,9,10,11], [12,13,14,15], [24,25,26,27], [28,29,30,31] ]
matrixSetE = [ [16,17,18,19], [20,21,22,23], [24,25,26,27], [28,29,30,31] ]

def guessTheBirthday():
    
    for i in range(0, len(matrixSetA)):
        print(matrixSetA[i])

    print("\n")

    for i in range(0, len(matrixSetA)):
        print(matrixSetB[i])

    for i in range(0, len(matrixSetA)):
        print(matrixSetC[i])

    for i in range(0, len(matrixSetA)):
        print(matrixSetD[i])

    for i in range(0, len(matrixSetA)):
        print(matrixSetE[i])    

guessTheBirthday()