import hashlib
import base64


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