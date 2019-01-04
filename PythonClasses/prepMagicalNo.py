from math import sqrt

def main():
    x = 100
    y = 400

    for i in range (x, y+1):
        count = 0
        for j in range (2, int(sqrt(i)) + 1):
            if i % j == 0:
                count = count + 1
        
        if count == 1:
            print(i)

main()