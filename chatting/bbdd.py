from pprint import pprint


import pymysql
from pymysql.err import DatabaseError
from pymysql.cursors import DictCursor
import uuid
from datetime import date

import state

class bbdd():
    def __init__(self):
        self.connection = pymysql.connect(
            host=state.conf["DATABASE_HOST"],
            user=state.conf["DATABASE_USER"],
            password=state.conf["DATABASE_PASS"],
            db='chat'
        )
        self.cursor = self.connection.cursor(DictCursor)


    def setMsg(self,body):
        try:
            with self.connection.cursor() as cur:
                uuid_ = uuid.uuid4().hex
                today = date.today()
                cur.execute('INSERT INTO messaging (id, from, to, msg, creation_date) VALUES(%s,%s, %s,%s, %s)', 
                (uuid_,body.get("from"),body.get("to"),body.get("msg"),today)) 
                self.connection.commit()
                return "Ok",200

        except Exception as e:
                return "error",400

    def getMsg(self,username):
        try:
            self.cursor.execute('SELECT id, from, to, msg, creation_date FROM messaging WHERE to =%s',username)
            msg = self.cursor.fetchone()
            self.connection.commit()
            if not msg :
                return "",401
            
            return msg,200     
                

        except Exception as e:
                return "error",400



    def close(self):
        self.connection.close()


