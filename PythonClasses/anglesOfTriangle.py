#take 3 CO-ORDINATES AS INPUT AND CALCULATE DISTANCE BETWEEN AND ANGLE BETWEEN THEM
import math

def calculateAngles(a, b, c):
    angleA = round(math.degrees(math.acos((a*a - b*b - c*c) / (-2 * b * c))), 2)
    angleB = round(math.degrees(math.acos((b*b - c*c - a*a) / (-2 * a * c))), 2)
    angleC = round(math.degrees(math.acos((c*c - a*a - b*b) / (-2 * a * b))), 2)

    print("Angles are:")
    print("A: {}".format(angleA))
    print("B: {}".format(angleB))
    print("C: {}".format(angleC))

def calculateSides(x1, y1, x2, y2, x3, y3):
    a = math.sqrt( (y2-y1)**2 + (x2-x1)**2 )
    b = math.sqrt( (y3-y2)**2 + (x3-x2)**2 )
    c = math.sqrt( (y3-y1)**2 + (x3-x1)**2 )

    print("Length of sides:")
    print("a: {}".format(a))
    print("b: {}".format(b))
    print("c: {}".format(c))

    calculateAngles(a, b, c)

def main():
    x1 = input("Enter x1: ")
    y1 = input("Enter y1: ")
    x2 = input("Enter x2: ")
    y2 = input("Enter y2: ")
    x3 = input("Enter x3: ")
    y3 = input("Enter y3: ")

    calculateSides(x1, y1, x2, y2, x3, y3)


main() 