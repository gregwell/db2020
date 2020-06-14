import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="trustnet")

mycursor = mydb.cursor()

def dodaj_uzytkownika(t_imie, t_nazwisko):
   sql = "INSERT INTO uzytkownik (id_uzytkownik, imie, nazwisko)" \
         "VALUES (%s, %s, %s)"
   args = ("NULL", t_imie, t_nazwisko)
   mycursor.execute(sql, args)
   mydb.commit()

