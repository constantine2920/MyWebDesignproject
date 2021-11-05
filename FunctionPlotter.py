
import matplotlib.pyplot as plt

def ThreeXSubtractTwo(x):
    returnVal = 3*x-2
    return returnVal

def VectorGenerator(ArrayOfX):
    returnVal = []
    for x in ArrayOfX:
        returnVal.append(ThreeXSubtractTwo(x))
    return returnVal

ArrayOfX = [3,2,1,0,-1,-2,-3]


print(ThreeXSubtractTwo(3))
ArrayOfY = VectorGenerator(ArrayOfX)

print(ArrayOfX)
print(ArrayOfY)
