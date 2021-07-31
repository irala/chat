import time
import jwt
import requests
import six
from werkzeug.exceptions import Unauthorized
from bbdd import bbdd

import state
db = bbdd()

def get_messages(token_info):
    user_id = token_info.get("sub")
    msg,code =db.getMsg(user_id)
    if code > 299:
        return msg,code
    return msg, 200




def send_message(body,destinataryid, token_info):
    user_id = token_info.get("sub")
    msg,code=db.setMsg(user_id,destinataryid,body)
    if code > 299:
        return msg,code
    return msg , 200

    
def check_token(token):
    utf8token = token
    data = None
    try:
        print(utf8token, state.conf["JWT_PASS"] )

        data = jwt.decode(jwt=utf8token, key=state.conf["JWT_PASS"], algorithms=["HS256"])
    except jwt.exceptions.InvalidSignatureError as e:
        print( "Invalid signature token", str(e))
        six.raise_from( Unauthorized,e )
        return None
    except jwt.exceptions.ExpiredSignatureError as e:
        print( "Expired token")
        six.raise_from( Unauthorized,e )
        return None
    except jwt.InvalidTokenError as e:
        print( "Invalid token", str(e))
        six.raise_from( Unauthorized,e )
        return None
    except Exception as e:
        print( f"Other token error: {str(e)}")
        six.raise_from( Unauthorized,e )
        return None
    return data