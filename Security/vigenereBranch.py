#from vigenere import *
#from caesar import * 

from itertools import count


def countOccurrency(array):
    # Array for the letters in the alphabet (includes a space)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    occurenceArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in array:
        for j in range (0, 27):
            if i == alphabet[j]:
                occurenceArray[j]+=1
    return occurenceArray

def rotateLeft(array): 
    newArray = array[1 : len(array)]
    newArray.append(array[0])
    return newArray

print(countOccurrency(['a', 'a', 'b', 'z', 'a']))
print(rotateLeft([1,2,3,4,5]))
str = "hola mundo"
print(list(str))