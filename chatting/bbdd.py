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

    def getId(self, user_id):

        self.cursor.execute(
            'SELECT id FROM user_account WHERE id =%s', user_id)
        msg = self.cursor.fetchone()
        self.connection.commit()
        print("getid -->", msg)
        if not msg:
            print("not id")
            return "not such user", 400
        return msg, 200

    def setMsg(self, user_id, destinataryid, body):
        with self.connection.cursor() as cur:
            try:
                uuid_ = uuid.uuid4().hex
                today = date.today()
                msg, code = self.getId(destinataryid)
                print("msg:", body.get("message"))

                if code > 299:
                    return msg, code

                cur.execute('INSERT INTO messages (id, user_id, destinatary_id, message) VALUES (%s, %s, %s, %s)',
                            (uuid_, user_id, destinataryid, body.get("message")))
                self.connection.commit()

                return "Ok", 200

            except Exception as e:
                print(cur._last_executed)
                print(e)
                return "error", 400

    def getMsg(self, user_id):
        try:
            self.cursor.execute(
                'SELECT * FROM messages WHERE destinatary_id =%s or user_id = %s', (user_id,user_id))
            result = self.cursor.fetchall()
            self.connection.commit()
            if not result:
                return "", 400

            return result, 200

        except Exception as e:
            return "error", 400

    def close(self):
        self.connection.close()
