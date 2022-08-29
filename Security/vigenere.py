'''
Code to implement Vignere's Cipher and to Decipher it. 

Ana Paula Katsuda Zalce, A01025303
Karla Valeria Mondragón Rosas, A01025108

'''
#Import library for array
from array import array
from caesar import rotateAlphabet

# function that counts occurency of each letter in an array
def countOccurrency(array):
    # Array for the letters in the alphabet (includes a space)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    # start array that starts count in 0 for each letter
    occurenceArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # iterate though array
    for i in array:
        # iterate through 0 to 27
        for j in range (0, 27):
            # if the element in the array is the same as the element in alphabet
            if i == alphabet[j]:
                # add 1 to occurrency in corresponding index
                occurenceArray[j]+=1
    # Return
    return occurenceArray

# function that creates key for cipher --> repeats key until len reaches message len
def keyForCipher(key, message):
    # new key array
    newKey = []
    # Stablish that key cannot be greater than length of message
    if len(key) > len(message):
        print('Invalid key')
        return 0
    # While length of new key is less than length of message
    while len(newKey) < len(message):
        # for every element in the key
        for i in key:
            # add element to newKey
            newKey.append(i)
            # once new key is the same length as message
            if len(newKey) == len(message):
                # break cicle
                break
    #Return
    return newKey

# Function that ciphers using vigenere's method
def vigenereCipher(key, message):
    # New key that has length message
    newKey = keyForCipher(key, message)
    encryptedMessage = '' # final result of the encryption, starts empty
    #lowercase message 
    message = message.lower()
    # Array for the letters in the alphabet (includes a space)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    # iterate through len in message 
    for i in range (0, len(message)):
        # rotate alphabet using each element of the new key as the key
        rotate = rotateAlphabet(newKey[i])
        # iterate though length of alphabet
        for j in range (0, 27):
            # if the element in message matches the element on alphabet
            if message[i] == alphabet[j]:
                # add letter from rotate to encrypted message using index j
                encryptedMessage = encryptedMessage + rotate[j];
                # break inner for
                break
    # Return 
    return encryptedMessage

# function used to decipher key only
def vigenerKeyDecipher(keySize, message):
    # Array for the letters in the alphabet (includes a space)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    # lower letters in message --> to be able to match
    message = message.lower()
    # Initialize index and key array
    index = 0
    key = []
    # while index is lower than keySize
    while (index < keySize):
        # new array
        new  = []
        # iterate from index to length of message every keySize
        for i in range (index, len(message), keySize):
            # add element to new array
            new.append(message[i])
        # count frequency of each letter within the new array
        occurrance = countOccurrency(new)
        # get the index of the letter with maximum frequence (if many letters
        # have the same frequency, it takes the first one)
        max_index = occurrance.index(max(occurrance))
        # Assuming the most common char is ' ', it becomes evident that the key 
        # will be max_index + 1 as, ' ' is the last element in the alphabet
        if max_index == 26: # if max_index = 26, then the key will be 'a'
            key.append(alphabet[0])
        # if max_index < 26
        else: 
            key.append(alphabet[max_index + 1])
        # add 1 to index to continue iteration
        index += 1
    # Return array converted into string
    return ''.join(key)

# Function that deciphers vigenere's cipher
def vigenereDecipher(keySize, message): 
    # determine key using vigenereKeyDecipher function
    key = vigenerKeyDecipher(keySize, message)
    # Array for the letters in the alphabet (includes a space)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    # convert key so that it has the same length as message
    newKey = keyForCipher(key, message)
    # initialize decrypted message
    decryptedMessage = ''
    # iterate though the length of message 
    for i in range (0, len(message)): 
        # rotate alphabet for every element in newKey (every loop)
        rotate = rotateAlphabet(newKey[i])
        # iterate though the length of alphabet
        for j in range (0, 27):
            # if the element of the message matches an element of the rotate array
            if message[i] == rotate[j]:
                # update decrypted message using alphabet in the corresponding index
                decryptedMessage += alphabet[j]
    # Return decrypted message
    return decryptedMessage
