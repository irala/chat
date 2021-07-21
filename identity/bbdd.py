from pprint import pprint


import pymysql
from pymysql.err import DatabaseError
from pymysql.cursors import DictCursor
import bcrypt
import uuid

conf={}
class bbdd():
    def __init__(self,conf=conf):
        self.conf = conf
        self.connection = pymysql.connect(
            host=self.conf["DATABASE_HOST"],
            user=self.conf["DATABASE_USER"],
            password=self.conf["DATABASE_PASS"],
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
            return "incorrect password",401
        else:
            return "Ok",200


    def readUser(self, username, password):
      
        try:
            self.cursor.execute('SELECT id as user_id,username, password FROM user_account WHERE USERNAME =%s',username)
            user = self.cursor.fetchone()
            self.connection.commit()
            if not user :
                return "",401
            
            return user,200     
            

        except Exception as e:
            return "error",400

	
    def createUser(self,username, password):	

        try:

            with self.connection.cursor() as cur:
                passBcrypt=bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
                uuid_ = uuid.uuid4().hex
                cur.execute('INSERT INTO user_account (id,username,password) VALUES(%s,%s, %s)', 
                (uuid_,username,passBcrypt)) 
                self.connection.commit()
                return {
                    "user_id":uuid_,
                    "username":username
                },200

        except Exception as e:
            print('error'+ str(e))
            return "error",400

    
    def deleteUser(self, username):
        try:
            self.cursor.execute('DELETE FROM user_account WHERE USERNAME = %s',username)
            self.connection.commit()
            
            print('delete user: '+ username)
        except Exception as e:
            return "error",400

    def signUp(self, username, password):
        msg, code = self.readUser(username,password)
        if code > 299:
            print("new user --->")
            msg,codeNewUser=self.createUser(username,password)
            if codeNewUser >299:
                print("error",msg)
                
            print("created ", msg)
            return msg,200
        
        print("username already user")
        return "","username already user",401


    def signIn(self, username, password):
        msg, code =self.readUser(username,password)
        if code > 299:
            print(code)
            return "error",code
        
        result, codeCheck =self.checkPassword(msg, password)
        if codeCheck > 299:
            print(result)
            return "error",result
        
        msg.pop("password")
        return msg,200

    def close(self):
        self.connection.close()


database = bbdd()

# database.getAll()

# database.signIn("cosa","cosapass") 
# database.signIn("cosa","123") 
# database.signIn("prueba","mil")

# database.signUp("cosa","cosapass") 
# database.signUp("prueba","mil")
# database.signUp("carlos","bonito") 

#database.deleteUser('pepito')
