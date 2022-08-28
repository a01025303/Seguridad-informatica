'''
Code to implement Caesar's Cipher and to Decipher it. 

Ana Paula Katsuda Zalce, A01025303
Karla Valeria Mondragón Rosas, A01025108

'''

#Import library for array
from array import array

# Function to cipher using ceasar's method
def caesarCipher(keyLetter, message):
    # Array for the letters in the alphabet (includes a space)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    # Initialize variables
    index = 0 # will determine the index of the Key to rotate alphabet 
    encryptedMessage = '' # final result of the encryption, starts empty
    for i in range (0,27):
        if alphabet[i] == keyLetter:
            index = i
            break
    arrayTemp1 = alphabet[index:28]
    arrayTemp2 = alphabet[0:index]
    rotateArray = arrayTemp1 + arrayTemp2
    for x in message:
        for y in range (0,27):
            if x == alphabet[y]:
                encryptedMessage = encryptedMessage + rotateArray[y]
    print(alphabet)
    print(rotateArray)
    return encryptedMessage
    

print(caesarCipher('t', 'soy bien cool'))
