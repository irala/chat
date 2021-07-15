from pprint import pprint


import pymysql
from pymysql.err import DatabaseError
from pymysql.cursors import DictCursor
import bcrypt



class bbdd():
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='example',
            db='chat'
        )
        self.cursor = self.connection.cursor(DictCursor)


    def checkPassword(to_check_pwd,password):
        if not bcrypt.checkpw(password.encode("utf-8"), to_check_pwd.encode("utf-8")):
            return "404"
        else:
            return "200"

    #CRUD
    def getAll(self):
        try:
            self.cursor.execute("SELECT * FROM user_account")
            users=self.cursor.fetchall()
            self.connection.commit()

            for user in users:
                print("user "+ user.get("username") + " password "+user.get("password"))

        except Exception as e:
            return "400"

    def readUser(self, username, password):
      
        try:
            self.cursor.execute(f"SELECT id,username, password FROM user_account WHERE USERNAME ={username}")
            user = self.cursor.fetchone()
            self.connection.commit()
            if not user :
                return "404"
            else:
                self.checkPassword(user.get("password"), password)        

        except Exception as e:
            return "400"

	
    def createUser(self,id,username, password):	

        try:

            with self.connection.cursor() as cur:
                passBcrypt=bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
                cur.execute('INSERT INTO user_account VALUES(%s, %s, %s)', 
                (id,username,passBcrypt)) 
                self.connection.commit()

                print('new user inserted')

        except Exception as e:
            print('error'+ str(e))
            return "400"

    
    def deleteUser(self, username):
        try:
            self.cursor.execute(f"DELETE FROM user_account WHERE USERNAME = {username}")
            self.connection.commit()
            
            print('delete user: '+ username)
        except Exception as e:
            return "400"

    def close(self):
        self.connection.close()


database = bbdd()
database.getAll()
database.readUser("cosa","cosapa") 

#database.createUser(5,'cosa', 'cosapass')
#database.deleteUser('pepito')
