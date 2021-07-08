from pprint import pprint

import pymysql
from pymysql.err import DatabaseError


class bbdd():
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='example',
            db='chat'
        )

        self.cursor = self.connection.cursor()

        print("Conexion bien")

    def readUser(self, id):
        sql = 'SELECT id,username, password FROM user_account WHERE ID ={}'.format(
            id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print("id:", user[0])
            print("username:", user[1])
            print("password:", user[2])

        except Exception as e:
            raise

	
    def createUser(self, username, password):	
        try:
			self.cursor.execute('INSERT INTO user_account VALUES(%s, %s)',(username, password) )
			self.connection.commit()

			print('new user inserted')

        except Exception as e:
            raise

    def close(self):
        self.connection.close()


database = bbdd()
database.createUser("pepito", "hola")
