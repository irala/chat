import time

import six
from werkzeug.exceptions import Unauthorized
from ddbb import ddbb


_ddbb= ddbb()

def getMsg(username):
    msg, code= _ddbb.setMsg(username)
    if code >299:
        return "error",code
    return msg


def sendMsg(body):
    msg,code= _ddbb.getMsg(body)
    if code >299:
        return "error",code
    return msg

    
if __name__ == "__main__" or __name__ == "messaging":
    pass