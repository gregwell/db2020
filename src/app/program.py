import mysql.connector

from src.app import operations, functions

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="trustnet")

mycursor = mydb.cursor()

print(("Co chcesz teraz zrobić? "))
print("1 - obsluga uzytkownika")
temp = input("Wpisz cyfre: ")

if temp == "1":
    print(("Co chcesz teraz zrobić? "))
    print("1 - rejestracja uzytkownika")
    temp = input("Wpisz cyfre: ")
    if temp == "1":
        functions.rejestracja_uzytkownika()
    else:
        print("bledny wybor")
else:
    print("bledny wybor")


