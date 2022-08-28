'''
Code to implement Vignere's Cipher and to Decipher it. 

Ana Paula Katsuda Zalce, A01025303
Karla Valeria Mondragón Rosas, A01025108

'''
#Import library for array
from array import array
from caesar import rotateAlphabet

'''


'''

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