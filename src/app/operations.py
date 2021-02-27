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


def dodawanie_opinii(o_liczba, o_opis, o_firma, o_uzytkownik):
    mycursor = mydb.cursor()
    sql = "INSERT INTO opinie (id_opinia, liczba_gwiazdek, opis, FirmaID, UzytkownikID)" \
          "VALUES (%s, %s, %s, %s, %s)"
    args = ("NULL", o_liczba, o_opis, o_firma, o_uzytkownik[0],)
    mycursor.execute(sql, args)
    mydb.commit()


def wyswietlanie_firm():
    mycursor = mydb.cursor()
    sql = "SELECT id_firma, nazwa, branza, miasto FROM firma"
    mycursor.execute(sql)
    temp = mycursor.fetchall()
    for row in temp:
        print(row[0], row[1])

    mydb.commit()
    mycursor.close()
    # mydb.close
    # return temp


def wyswietlanie_opinii(idfirmy):
    mycursor = mydb.cursor()
    print(idfirmy)
    sql = 'SELECT opis, liczba_gwiazdek FROM opinie WHERE FirmaID = %s ORDER BY liczba_gwiazdek ASC'
    args = (idfirmy,)
    mycursor.execute(sql, args)
    temp = mycursor.fetchall()
    for row in temp:
        print(row[0], row[1])

    mydb.commit()
    mycursor.close()


# tu mozna dodac zeby z user input wybierac branze
def ranking_fryzjerow(branza):
    sql = "SELECT nazwa, AVG(liczba_gwiazdek) FROM opinie INNER JOIN firma ON opinie.FirmaID=firma.id_firma WHERE firma.branza = %s GROUP BY nazwa ORDER BY liczba_gwiazdek DESC"
    args = (branza,)
    mycursor.execute(sql, args)
    temp = mycursor.fetchall()
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


def wyswietlanie_branz():
    mycursor = mydb.cursor()
    sql = "SELECT branza FROM firma GROUP BY branza"
    mycursor.execute(sql)
    temp = mycursor.fetchall()
    for row in temp:
        print(row[0])

    mydb.commit()
    mycursor.close()


def moje_opinie(iduzytkownika):
    mycursor = mydb.cursor()
    sql = 'SELECT opinie.id_opinia, opinie.liczba_gwiazdek, opinie.opis, firma.nazwa FROM opinie INNER JOIN firma ON opinie.FirmaID=firma.id_firma WHERE opinie.UzytkownikID = %s'
    mycursor.execute(sql, iduzytkownika, )
    temp = mycursor.fetchall()
    for row in temp:
        print(row[0], row[1], row[2], row[3])

    mydb.commit()
    mycursor.close()


def usuwanie_firmy(idfirma):
    mycursor = mydb.cursor()
    sql = "DELETE FROM firma WHERE id_firma = %s"
    args = (str(idfirma),)
    mycursor.execute(sql, args)
    mydb.commit()
    mycursor.close()


def ranking_uzytkownikow():
    mycursor = mydb.cursor()
    sql = "SELECT `UzytkownikID`, COUNT(UzytkownikID) AS `liczba opinii tego uzytkownika` FROM `opinie` GROUP BY `UzytkownikID` ORDER BY `liczba opinii tego uzytkownika` DESC"
    mycursor.execute(sql)
    temp = mycursor.fetchall()
    i = 1
    for row in temp:
        print(str(i) + " miejsce... ID uzytkownika:" + str(row[0]))
        print("             liczba opinii:" + str(row[1]))
        print("")
        i = i + 1
    mydb.commit()


def edytuj_o(ido, opis, gwiazdki):
    mycursor = mydb.cursor()
    sql = "UPDATE opinie SET opis = %s, liczba_gwiazdek = %s WHERE id_opinia = %s"
    args = (str(opis), str(gwiazdki), str(ido),)
    mycursor.execute(sql, args)
    mydb.commit()
    mycursor.close()

# def wyswietl_opinie_opis(idf, idu):
#     mycursor = mydb.cursor()
#     sql = 'SELECT opinie.opis, opinie.liczba_gwiazdek, uzytkownik.login FROM opinie INNER JOIN uzytkownik WHERE opinie.opis IS NOT NULL AND opinie.FirmaID = %s AND opinie.UzytkownikID = %s'
#     args = (str(idf), str(idu), str(idu),)
#     mycursor.execute(sql, args)
#     temp = mycursor.fetchall()
#     for row in temp:
#         print(row[0], row[1])
#
#     mydb.commit()
#     mycursor.close()
