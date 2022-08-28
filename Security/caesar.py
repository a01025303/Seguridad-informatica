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
    # For that iterates from 0 to 26 (number of letters in our alphabet)
    for i in range (0,27):
        # When the alphabet letter matches the key
        if alphabet[i] == keyLetter:
            # Save index
            index = i
            break
    # Array that saves the letters from index to letter with index 26
    arrayTemp1 = alphabet[index:27]
    # Array that saves the letters from 0 to index - 1
    arrayTemp2 = alphabet[0:index]
    # Rotated array: merges previous arrays to rotate the whole alphabet
    rotateArray = arrayTemp1 + arrayTemp2

    # Code to translate message into encrypted message
    # Cicle that iterates through every char in message
    for x in message:
        # Cicle that, for each char in message, looks for match in alphabet
        for y in range (0,27):
            # When the char matches a char in alphabet
            if x == alphabet[y]:
                # Update message, adding a letter from the rotated 
                # array with the corresponding index
                encryptedMessage = encryptedMessage + rotateArray[y]
    print(alphabet)
    print(rotateArray)
    # Return result
    return encryptedMessage
    

print(caesarCipher('a', 'soy bien cool'))
