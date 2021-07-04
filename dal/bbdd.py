import datetime
import json
import traceback
from pprint import pprint

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

silent = True
conf = {}


class bbdd():

	def get_db_conn(self):
		db_conn = mysql.connector.connect(
			host=self.conf["DATABASE_HOST"],
			user=self.conf["DATABASE_USER"],
			passwd=self.conf["DATABASE_PASS"],
			database= self.current_database,#"prot",
			use_pure=True,
			use_unicode=True, 
			charset='utf8mb4'
		)
		return db_conn

    def createUser():
        pass

    def readUser():
        pass
