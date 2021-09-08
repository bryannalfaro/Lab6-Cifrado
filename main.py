import hashlib
import base64
from producer import *


# sha256
text =  'Hola'.encode('utf-8')
print(hashlib.sha256(text).digest())
print(hashlib.sha256(text).hexdigest())
print(base64.b64encode(hashlib.sha256(text).digest()).decode())

#sha512
text =  'Hola'.encode('utf-8')
print(hashlib.sha512(text).digest())
print(hashlib.sha512(text).hexdigest())
print(base64.b64encode(hashlib.sha256(text).digest()).decode())

#blake2b
text =  'Hola'.encode('utf-8')
digest_size = 32
print(hashlib.blake2b(text,digest_size=digest_size).digest())
print(hashlib.blake2b(text,digest_size=digest_size).hexdigest())
print(base64.b64encode(hashlib.blake2b(text,digest_size=digest_size).digest()).decode())

# sha256
text =  'Hola este es texto para cifrado 2'.encode('utf-8')
print(hashlib.sha256(text).digest())
print(hashlib.sha256(text).hexdigest())
print(base64.b64encode(hashlib.sha256(text).digest()).decode())

#sha512
text =  'Hola este es texto para cifrado 2'.encode('utf-8')
print(hashlib.sha512(text).digest())
print(hashlib.sha512(text).hexdigest())
print(base64.b64encode(hashlib.sha256(text).digest()).decode())

#blake2b
text =  'Hola este es texto para cifrado 2'.encode('utf-8')
digest_size = 32
print(hashlib.blake2b(text,digest_size=digest_size).digest())
print(hashlib.blake2b(text,digest_size=digest_size).hexdigest())
print(base64.b64encode(hashlib.blake2b(text,digest_size=digest_size).digest()).decode())

hash1 = produce_hash('texto1.txt','h'.encode('utf-8'))
hash2 = produce_hash('texto2.txt','h'.encode('utf-8'))

print('Hash1: ',hash1)
print('Hash2: ',hash2)

print(verify('texto1.txt','h'.encode('utf-8'),hash1))
print(verify('texto1.txt','h'.encode('utf-8'),hash2))
print(verify('texto2.txt','h'.encode('utf-8'),hash1))
print(verify('texto2.txt','h'.encode('utf-8'),hash2))