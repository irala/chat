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
            return "error",400


    def checkPassword(self,user,password):
        to_check_pwd=user.get("password")
        print(to_check_pwd , "--", password)
        if not bcrypt.checkpw(password.encode("utf-8"), to_check_pwd.encode("utf-8")):
            return "incorrect password",404
        else:
            return "Ok",200


    def readUser(self, username, password):
      
        try:
            self.cursor.execute('SELECT id,username, password FROM user_account WHERE USERNAME =%s',username)
            user = self.cursor.fetchone()
            self.connection.commit()
            if not user :
                return "",404
            
            self.checkPassword(user, password)     
           

        except Exception as e:
            return "error",400

	
    def createUser(self,id,username, password):	

        try:

            with self.connection.cursor() as cur:
                passBcrypt=bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
                cur.execute('INSERT INTO user_account VALUES(%s, %s, %s)', 
                (id,username,passBcrypt)) 
                self.connection.commit()

                return "new user inserted",200

        except Exception as e:
            print('error'+ str(e))
            return "error",400

    
    def deleteUser(self, username):
        try:
            self.cursor.execute('DELETE FROM user_account WHERE USERNAME = %s',username)
            self.connection.commit()
            
            print('delete user: '+ username)
        except Exception as e:
            return "400"

    def signUp(self, username, password):
        user=self.readUser(username,password)
        print("respuesta", user)
        if user == "":
            print("not user")
            newUser=self.createUser(8,username,password)
            return newUser
        else:
            return user


    def signIn(self, username, password):
        user=self.readUser(username,password)
        if not user:
            return ""
        else:
            return user

    def close(self):
        self.connection.close()


database = bbdd()

# database.getAll()

# database.signIn("cosa","cosapass") 
# database.signIn("cosa","123") 

# database.signUp("prueba","mil")
database.signUp("prueba","123") 

#database.deleteUser('pepito')
