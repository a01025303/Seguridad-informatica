'''
Code to implement Vignere's Cipher and to Decipher it. 

Ana Paula Katsuda Zalce, A01025303
Karla Valeria Mondragón Rosas, A01025108

'''

import secrets
from vigenere import vigenereCipher

# Function that generates one time pad and cipher message
def oneTimePad(message):
    #lower letters in message
    message = message.lower();
    # initialize one time path
    otp = ''
    # iterate through length of message
    for i in range(len(message)):
        # use secrets library to randomize and add to otp
        otp += secrets.choice("abcdefghijklmnopqrstuvwxyz ")
    # use vigenereCipher using otp
    cipherMessage = vigenereCipher(otp, message)
    # return both one time path and ciphered message
    return otp, cipherMessage
