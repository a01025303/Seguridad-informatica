'''
Code to implement Caesar's Cipher and to Decipher it. 

Ana Paula Katsuda Zalce, A01025303
Karla Valeria Mondragón Rosas, A01025108

'''

#Import library for array
from array import array

# Function that rotates alphabet
def rotateAlphabet(key):
    # Array for the letters in the alphabet (includes a space)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    # Initialize variables
    index = 0 # will determine the index of the Key to rotate alphabet 
    # For that iterates from 0 to 26 (number of letters in our alphabet)
    for i in range (0,27):
        # When the alphabet letter matches the key
        if alphabet[i] == key:
            # Save index
            index = i
            break
    # Array that saves the letters from index to letter with index 26
    arrayTemp1 = alphabet[index:27]
    # Array that saves the letters from 0 to index - 1
    arrayTemp2 = alphabet[0:index]
    # Rotated array: merges previous arrays to rotate the whole alphabet
    rotateArray = arrayTemp1 + arrayTemp2
    return rotateArray

# Function to cipher using ceasar's method
def caesarCipher(keyLetter, message):
    # Array for the letters in the alphabet (includes a space)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    
    encryptedMessage = '' # final result of the encryption, starts empty
    
    rotate = rotateAlphabet(keyLetter)
    # Code to translate message into encrypted message
    #lowercase message 
    message = message.lower()
    # Cicle that iterates through every char in message
    for x in message:
        # Cicle that, for each char in message, looks for match in alphabet
        for y in range (0,27):
            # When the char matches a char in alphabet
            if x == alphabet[y]:
                # Update message, adding a letter from the rotated 
                # array with the corresponding index
                encryptedMessage = encryptedMessage + rotate[y]
                break
    print(alphabet)
    print(rotate)
    # Print message
    print(encryptedMessage.upper())
    # Return
    return 0

def caesarDecipher(message):
    # Array for the letters in the alphabet (includes a space)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    # Lowercase message to match alphabet
    message = message.lower()
    # Variable to save decrypted message
    decryptedMessage = ''
    # Iterate through alphabet letters
    for i in alphabet:
        # Array with rotated letters --> consiering i as key
        rotate = rotateAlphabet(i)
        # Iterate through letters in message
        for j in message:
            # Cicle that goes from 0 to 26
            for k in range (0,27):
                # When the char from message matches the char from rotated array
                if j == rotate[k]:
                    # Update message, adding a letter from the alphabet 
                    # array with the corresponding index
                    decryptedMessage = decryptedMessage + alphabet[k]
                    break
        # for each key, print message
        print(decryptedMessage)
        # Ask user if text was successfully decrypted 
        makeSense = input('Does this make sense (type y only)?')
        # If text was successfully decrypted, show user text and key
        if makeSense == 'y': 
            print('The key was ' + i + ' and the message is: ' + decryptedMessage)
            break # stop cycle 
        # Else, restart message 
        decryptedMessage = ''
    # Return
    return 0
