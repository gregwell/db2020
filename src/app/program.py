import mysql.connector

from src.app import operations, functions

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="trustnet")

mycursor = mydb.cursor()

functions.rejestracja_uzytkownika()
