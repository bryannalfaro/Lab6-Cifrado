# Universidad del Valle de Guatemala
# Criptografia y Cifrado de Informacion
# Lab 6: Hash
# Bryann Alfaro
# Julio Herrera
# Diego Arredondo

import hashlib
import base64
from producer import *

#1a parte
print("\nPRIMERA PARTE:")
word1 = "Hola"
word2 = "Hola este es texto para cifrado 2"

# sha256
print(f"\nCifrado SHA256 de la palabra '{word1}'")
text =  word1.encode('utf-8')
print("Binario:\t", hashlib.sha256(text).digest())
print("Hexadecimal:\t", hashlib.sha256(text).hexdigest())
print("Base64:\t\t", base64.b64encode(hashlib.sha256(text).digest()).decode())

#sha512
print(f"\nCifrado SHA512 de la palabra '{word1}'")
text =  word1.encode('utf-8')
print("Binario:\t", hashlib.sha512(text).digest())
print("Hexadecimal:\t", hashlib.sha512(text).hexdigest())
print("Base64:\t\t", base64.b64encode(hashlib.sha256(text).digest()).decode())

#blake2b
print(f"\nCifrado blake2b de la palabra '{word1}'")
text =  word1.encode('utf-8')
digest_size = 32
print("Binario:\t", hashlib.blake2b(text,digest_size=digest_size).digest())
print("Hexadecimal:\t", hashlib.blake2b(text,digest_size=digest_size).hexdigest())
print("Base64:\t\t", base64.b64encode(hashlib.blake2b(text,digest_size=digest_size).digest()).decode())

# sha256
print(f"\nCifrado SHA256 de la frase '{word2}'")
text =  word2.encode('utf-8')
print("Binario:\t", hashlib.sha256(text).digest())
print("Hexadecimal:\t", hashlib.sha256(text).hexdigest())
print("Base64:\t\t", base64.b64encode(hashlib.sha256(text).digest()).decode())

#sha512
print(f"\nCifrado SHA512 de la frase '{word2}'")
text =  word2.encode('utf-8')
print("Binario:\t", hashlib.sha512(text).digest())
print("Hexadecimal:\t", hashlib.sha512(text).hexdigest())
print("Base64:\t\t", base64.b64encode(hashlib.sha256(text).digest()).decode())

#blake2b
print(f"\nCifrado blake2b de la frase '{word2}'")
text =  word2.encode('utf-8')
digest_size = 32
print("Binario:\t", hashlib.blake2b(text,digest_size=digest_size).digest())
print("Hexadecimal:\t", hashlib.blake2b(text,digest_size=digest_size).hexdigest())
print("Base64:\t\t", base64.b64encode(hashlib.blake2b(text,digest_size=digest_size).digest()).decode())

input("\nPresione cualquier tecla para continuar...")

#2da parte
print("\nSEGUNDA PARTE:")
txt1 = "texto1.txt"
txt2 = "texto2.txt"
hash1 = produce_hash(txt1,'h'.encode('utf-8'))
hash2 = produce_hash(txt2,'h'.encode('utf-8'))

print(f'\nHash1 a partir del {txt1}: ',hash1)
print(f'Hash2 a partir del {txt2}: ',hash2)

print(f"\n{txt1} verificado con Hash1: ", verify('texto1.txt','h'.encode('utf-8'),hash1))
print(f"{txt1} verificado con Hash2: ", verify('texto1.txt','h'.encode('utf-8'),hash2))
print(f"{txt2} verificado con Hash1: ", verify('texto2.txt','h'.encode('utf-8'),hash1))
print(f"{txt2} verificado con Hash2: ", verify('texto2.txt','h'.encode('utf-8'),hash2))

input("\nPresione cualquier tecla para continuar...")

#3era parte
print('TERCERA PARTE: SERVIDOR CIFRADO DE LA INFORMACION')
print('1. Registrarse')
print('2. Login')
validOptions = [1,2]
opcion = 0

while opcion not in validOptions:
    try:
        opcion = int(input('Ingresa el numero de opcion: '))
    except ValueError:
        print('Opcion invalida')

if opcion ==1:
    user  = input('Ingresa usuario: ')
    password = input('Ingresa password: ')

    register(user,password)
    print('Usuario registrado')
elif opcion ==2:
    user  = input('Ingresa usuario: ')
    password = input('Ingresa password: ')
    print(login(user,password))
