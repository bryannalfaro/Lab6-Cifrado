import hashlib
import hmac
from Crypto import Random
import csv


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

#3ra parte - Login y registro

def register(username,password):
    salt = Random.get_random_bytes(32)

    text = (password+salt.hex()).encode('utf-8')
    hashf = hashlib.sha256(text).hexdigest()

    with open('db.csv', mode='a',newline='') as user_f:
        user_writer = csv.writer(user_f)

        user_writer.writerow([username,salt.hex(),hashf])

def login(username,password):
    csv_file = csv.reader(open('db.csv', "r"))
    find = False
    for row in csv_file:

        if username == row[0]:
            find = True
            text = (password+row[1]).encode('utf-8')
            hashf = hashlib.sha256(text).hexdigest()
            if(hashf==row[2]):
                return 'Bienvenido al servidor ' + username
            else:
                return 'Contraseña incorrecta'
    if find == False:
        return 'Usuario no encontrado'






