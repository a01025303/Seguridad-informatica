'''
Code to implement Vignere's Cipher and to Decipher it. 

Ana Paula Katsuda Zalce, A01025303
Karla Valeria Mondragón Rosas, A01025108

'''
#Import library for array
from array import array
from caesar import rotateAlphabet
import numpy as np
from itertools import combinations


'''


'''

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


def keyForCipher(key, message):
    newKey = []
    if len(key) > len(message):
        print('Invalid key')
        return 0
    while len(newKey) < len(message):
        for i in key:
            newKey.append(i)
            if len(newKey) == len(message):
                break
    return newKey

def vigenereCipher(key, message):
    newKey = keyForCipher(key, message)
    encryptedMessage = '' # final result of the encryption, starts empty
    #lowercase message 
    message.lower()
    # Array for the letters in the alphabet (includes a space)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    for i in range (0, len(message)):
        rotate = rotateAlphabet(newKey[i])
        for j in range (0, 27):
            if message[i] == alphabet[j]:
                encryptedMessage = encryptedMessage + rotate[j];
                break
    return encryptedMessage
        
print(vigenereCipher('tbt', 'hola'))

#decipher key only
def vigenerKeyDecipher(keySize, message):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    message = message.lower()
    messageArray = list(message)
    maxV = []
    key = []
    occurrance = countOccurrency(messageArray)
    for i in range (0, keySize):
        max_index = occurrance.index(max(occurrance))
        maxV.append(max_index)
        occurrance[max_index] = 0
    for i in range (0, keySize):
        key.append(alphabet[maxV[i]])
        
    print(combinations(key, keySize))
    print(key)

    '''key = []
    while (index < keySize):
        new  = []
        product = []
        for i in range (index, len(message), keySize):
            new.append(message[i])
        occurrance = countOccurrency(new)
        for i in range(0, len(occurrance)):
            occurrance[i]/=len(new)
        for i in range (0, 27):
            product.append(np.dot(occurrance, new))
            occurrance = rotateLeft(occurrance)'''
    print(occurrance)
        #index += 1
    return 0