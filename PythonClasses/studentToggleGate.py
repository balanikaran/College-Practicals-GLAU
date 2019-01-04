totalStudents = 100
totalGates = 100

gates = list(False for x in range (0, 100))

for i in range (0, totalStudents):
    for j in range (0, totalGates):
        if (j+1) % (i+1) == 0:
            gates[j] = not gates[j]

for i in range (0, 100):
    print("{} : {}".format(i+1, gates[i]))