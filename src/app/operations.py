import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="trustnet")

mycursor = mydb.cursor()

def dodaj_uzytkownika(t_imie, t_nazwisko):
   sql = "INSERT INTO uzytkownik (id_uzytkownik, imie, nazwisko)" \
         "VALUES (%s, %s, %s)"
   args = ("NULL", t_imie, t_nazwisko)
   mycursor.execute(sql, args)
   mydb.commit()

def dodaj_firme(f_nazwa, f_branza, f_miasto, f_liczba_opinii, f_srednia):
   sql = "INSERT INTO firma (id_firma, nazwa, branza, miasto, liczba_opinii, srednia)" \
         "VALUES (%s, %s, %s, %s, %s, %s)"
   args = ("NULL", f_nazwa, f_branza, f_miasto, f_liczba_opinii, f_srednia)
   mycursor.execute(sql, args)
   mydb.commit()