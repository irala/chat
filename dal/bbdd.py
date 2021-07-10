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


    def getAll(self):
        try:
            self.cursor.execute("SELECT * FROM user_account")
            users=self.cursor.fetchall()
            self.connection.commit()

            for user in users:
                print("username "+ user[1]+ " password "+user[2])

        except Exception as e:
            raise

    def readUser(self, id):
        sql = 'SELECT id,username, password FROM user_account WHERE ID ={}'.format(
            id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            self.connection.commit()

            print("id:", user[0])
            print("username:", user[1])
            print("password:", user[2])

        except Exception as e:
            raise

	
    def createUser(self,id,username, password):	
        try:

            with self.connection.cursor() as cur:

                cur.execute('INSERT INTO user_account VALUES(%s, %s, %s)', 
                (id,username,password)) 
                self.connection.commit()

                print('new user inserted')

        except Exception as e:
            print('error'+ str(e))

    
    def deleteUser(self, username):
        try:
            sql="DELETE FROM user_account WHERE USERNAME = '"+ username + "'"
            print(sql)

            self.cursor.execute(sql)
            self.connection.commit()
            
            print('delete user: '+ username)
        except Exception as e:
            raise

    def close(self):
        self.connection.close()


database = bbdd()
database.getAll()
#database.readUser(1)
#database.createUser(1,'prueba', '1234')
#database.deleteUser('pepito')
