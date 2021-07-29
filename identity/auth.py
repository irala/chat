import time

import connexion
import six
from werkzeug.exceptions import Unauthorized
from bbdd import bbdd

from jose import JWTError, jwt

import state
#JWT_ISSUER = 'com.zalando.connexion'
JWT_SECRET = state.conf.get("JWT_PASS",'secret')
JWT_LIFETIME_SECONDS = 600
JWT_ALGORITHM = 'HS256'


_bbdd = bbdd()


def _current_timestamp() -> int:
    return int(time.time())

def generate_token(additional_payload):
    timestamp = _current_timestamp()
    payload = {
        #"iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
    }
    payload={**payload,**additional_payload}

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


def signIn(body):
    print("login")
    msg,code=_bbdd.signIn(body["username"],body["password"])
    if code >299:
        return msg,code
    access_token=generate_token({
    "sub":msg.get("user_id"),
    "user_id":msg.get("user_id"),
    "username":body["username"]
    }
    )  
    msg["access_token"]=access_token
    return msg,200

def signUp(body):
    print("register")
    msg,code=_bbdd.signUp(body["username"],body["password"])
    if code >299:
        return msg,code
    access_token=generate_token({
        "sub":msg.get("user_id"),
        "user_id":msg.get("user_id"),
        "username":body["username"]
        }
        )  
    print(access_token)
    msg["access_token"]=access_token
    return msg,200



    
if __name__ == "__main__" or __name__ == "auth":
    pass