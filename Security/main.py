'''
Code to test Encryption and Decryption with implemented methods 

Ana Paula Katsuda Zalce, A01025303
Karla Valeria Mondragón Rosas, A01025108

'''

# Import caesar's method functions
from caesar import *
from vigenere import *
from oneTimePad import * 

# Testing Caesar's Method
# Read test file
cipher1 = open('/Users/akemi/Desktop/TEC/Semestre5/Seguridad-informatica/Security/cipher1.txt', 'r')
# Test decipher
caesarDecipher(cipher1.read())
print()
print()
print()
# Test cipher
caesarCipher('n', 'hola me llamo karla y me pongo roja')
print()
print()
print()

# Testing Vigenere's Method
# Read test file
cipher2 = open('/Users/akemi/Desktop/TEC/Semestre5/Seguridad-informatica/Security/cipher2.txt', 'r')
# Test decipher
print(vigenereDecipher(4, cipher2.read()))
print()
print()
print()
# Test cipher
print(vigenereCipher('haeg', 'hola soy akemi y tengo miopia aparentemente'))
print()
print()
print()
# Testing One Time Pad
print(oneTimePad('hola prof como estas'))
