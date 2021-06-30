import time

import connexion
import six
from werkzeug.exceptions import Unauthorized

from jose import JWTError, jwt

#JWT_ISSUER = 'com.zalando.connexion'
JWT_SECRET = 'secret'
JWT_LIFETIME_SECONDS = 600
JWT_ALGORITHM = 'HS256'


def _current_timestamp() -> int:
    return int(time.time())

def generate_token(username):
    timestamp = _current_timestamp()
    payload = {
        #"iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "sub": str(username),
    }

    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)

def get_secret(user, token_info) -> str:
    return '''
    You are username {user} and the secret is 'wbevuec'.
    Decoded token claims: {token_info}.
    '''.format(user=user, token_info=token_info)


def login(body):
    print("login")
    #TODO: comprobamos su existencia en bbdd y generamos token
    result=generate_token(body["username"])  
    #TODO: si no está enviar mensaje
    return {"username":body["username"], "token": result},200

def register(body):
    print("register")
    #TODO:antes de registrar en bbdd comprobar que existe
    # si no está creado se registra en bbdd
    # si existe generamos el token unicamente 
    result=generate_token(body["username"])  

    print(result)
    return {"username":body["username"], "token": result},200



    
if __name__ == "__main__" or __name__ == "auth":
    pass