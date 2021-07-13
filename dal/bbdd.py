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



    #CRUD
    def getAll(self):
        try:
            self.cursor.execute("SELECT * FROM user_account")
            users=self.cursor.fetchall()
            self.connection.commit()

            for user in users:
                print("user "+ user.get("username") + " password "+user.get("password"))

        except Exception as e:
            raise

    def readUser(self, username, password):
        sql = "SELECT id,username, password FROM user_account WHERE USERNAME = '"+ username +"'"       
      
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            self.connection.commit()
            if not user :
                print("not exists")
            else:
                to_check_pwd = user.get("password")
                if not bcrypt.checkpw(password.encode("utf-8"), to_check_pwd.encode("utf-8")):
                    print("pass error")
                else:
                    print("correct")        

        except Exception as e:
            raise

	
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

    
    def deleteUser(self, username):
        try:
            sql=f"DELETE FROM user_account WHERE USERNAME = {username} "

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
database.readUser("cosa","cosapa") 

#database.createUser(5,'cosa', 'cosapass')
#database.deleteUser('pepito')
