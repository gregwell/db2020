import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="trustnet")

mycursor = mydb.cursor()

mycursor.execute("select nazwisko from uzytkownik;")

myresult = mycursor.fetchone()

for row in myresult:
    print(row)