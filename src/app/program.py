import mysql.connector
import sys

from src.app import operations, functions

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="trustnet")

mycursor = mydb.cursor()

def menu():
    print(("Co chcesz teraz zrobić? "))
    print("0 - wyjscie z programu")
    print("1 - obsluga uzytkownika")
    temp = input("Wpisz cyfre: ")


    if temp == "1":
        print(("Co chcesz teraz zrobić? "))
        print("0 - wyjscie z programu")
        print("1 - rejestracja uzytkownika")
        temp = input("Wpisz cyfre: ")
        if temp == "1":
            functions.rejestracja_uzytkownika()
            menu()
        elif temp == "0":
            sys.exit(0)
        else:
            print("bledny wybor")
            menu()
    elif temp == "0":
        sys.exit(0)
    else:
        print("bledny wybor")
        menu()

menu()
