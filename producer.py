import hashlib
import hmac


def produce_hash(filename,key):
    file = open(filename,'r')
    texto = bytes(file.read(),'utf-8')
    hash= hmac.new(key,texto,hashlib.sha256).hexdigest()
    file.close()
    return hash

def verify(filename,key,hashf):
    file = open(filename,'r')
    texto = bytes(file.read(),'utf-8')
    hash= hmac.new(key,texto,hashlib.sha256).hexdigest()

    if hash == hashf:
        file.close()
        return 'Es igual'

    else:
        file.close()
        return 'No es igual'



