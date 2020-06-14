import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="trustnet")

mycursor = mydb.cursor()

# mycursor.execute("show databases;")

sql = "Insert into `uzytkownik`(`id_uzytkownik`, `imie`, `nazwisko`)  values(%s,%s,%s)"
user = ("NULL", "jan", "kowalski")
mycursor.execute(sql, user)
mydb.commit()

# for db in mycursor:
#     print(db)

# def add_user(t_imie, t_nazwisko):
#     with trustnet.cursor() as cursor:
#         sql = "INSERT INTO uzytkownik (id_uzytkownik, imie, nazwisko)" \
#               "VALUES (%s, %s, %s)"
#         args = (NULL, t_imie, t_nazwisko)
#         cursor.execute(sql, args)
#         trustnet.commit()
#
# add_user(grzegorz, studzinowski)
#
# mycursor.execute("select imie from uzytkownik where nazwisko='well'")
#
# for db in mycursor:
#     print(db)
