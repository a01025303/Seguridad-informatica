'''
Code to test Encryption and Decryption with implemented methods 

Ana Paula Katsuda Zalce, A01025303
Karla Valeria Mondragón Rosas, A01025108

'''

# Import caesar's method functions
from caesar import *

# Testing Caesar's Method
# Read test file
cipher1 = open('/Users/akemi/Desktop/TEC/Semestre5/Seguridad-informatica/Security/cipher1.txt', 'r')
# Test cipher
caesarCipher('n', 'wuwuwu')
# Teste decifer
caesarDecipher(cipher1.read())