import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="trustnet")

mycursor = mydb.cursor()

def dodaj_uzytkownika(t_imie, t_nazwisko, t_login, t_haslo):
   sql = "INSERT INTO uzytkownik (id_uzytkownik, imie, nazwisko, login, haslo)" \
         "VALUES (%s, %s, %s, %s, %s)"
   args = ("NULL", t_imie, t_nazwisko, t_login, t_haslo)
   mycursor.execute(sql, args)
   mydb.commit()

def dodaj_firme(f_nazwa, f_branza, f_miasto):
   sql = "INSERT INTO firma (id_firma, nazwa, branza, miasto)" \
         "VALUES (%s, %s, %s, %s)"
   args = ("NULL", f_nazwa, f_branza, f_miasto)
   mycursor.execute(sql, args)
   mydb.commit()

def dodawanie_opinii(o_liczba, o_opis, o_firma):
    mycursor = mydb.cursor()
    sql = "INSERT INTO opinie (id_opinia, liczba_gwiazdek, opis, FirmaID)" \
         "VALUES (%s, %s, %s, %s)"
    args = ("NULL", o_liczba, o_opis, o_firma)
    mycursor.execute(sql, args)
    mydb.commit()

def wyswietlanie_firm():
    mycursor = mydb.cursor()
    sql = "SELECT id_firma, nazwa, branza, miasto FROM firma"
    mycursor.execute(sql)
    temp=mycursor.fetchall()
    for row in temp:
        print(row[0], row[1])

    mydb.commit()
    mycursor.close()
    # mydb.close
    # return temp

def wyswietlanie_opinii(idfirmy):
    mycursor = mydb.cursor()
    print(idfirmy)
    sql = 'SELECT opis, liczba_gwiazdek FROM opinie WHERE FirmaID = %s'
    args = (idfirmy,)
    mycursor.execute(sql, args)
    temp = mycursor.fetchall()
    for row in temp:
        print(row[0], row[1])

    mydb.commit()
    mycursor.close()

# tu mozna dodac zeby z user input wybierac branze
def ranking_fryzjerow():
    sql = "SELECT nazwa, AVG(liczba_gwiazdek) FROM opinie INNER JOIN firma ON opinie.FirmaID=firma.id_firma WHERE firma.branza='Fryzjer' GROUP BY nazwa ORDER BY liczba_gwiazdek DESC"
    mycursor.execute(sql)
    temp=mycursor.fetchall()
    for row in temp:
        print(row[0], row[1])
    mydb.commit()

def logowanie(l_login, l_haslo):
    mycursor = mydb.cursor()
    # temp = l_login
    # temp2= l_haslo
    sql = "SELECT id_uzytkownik FROM uzytkownik WHERE login = %s AND haslo = %s"
    args = (str(l_login), str(l_haslo),)
    mycursor.execute(sql, args)
    # id to zmienna majaca w sobie informacje o osobie zalogowanej w naszym programie. Za kazdym razem nadpisywana.
    iduzytkownika = mycursor.fetchone()
    mydb.commit()
    mycursor.close()

    return iduzytkownika

    # mydb.close