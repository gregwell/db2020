import mysql.connector
import sys

from src.app import operations, functions

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="trustnet")

mycursor = mydb.cursor()

def menu():


    print(("Co chcesz teraz zrobić? "))
    print("0 - wyjscie z programu")
    print("1 - obsluga uzytkownika")
    print("2 - obsluga firmy")
    print("3 - dodaj opinie")
    print("4 - przegladaj opinie i rankingi")
    temp = input("Wpisz cyfre: ")

    if temp == "4":
        print(("Co chcesz teraz zrobić? "))
        print("0 - wyjscie z programu")
        print("1 - przegladaj opinie o wybranej firmie")
        print("2 - wyswietl ranking fryzjerow")
        temp = input("Wpisz cyfre: ")

        if temp == "2":
            operations.ranking_fryzjerow()
            menu()
        elif temp == "1":
            functions.przegladaj_opinie()
            menu()
        elif temp == "0":
            sys.exit(0)
        else:
            print("bledny wybor")
            menu()


    if temp == "3":
        print(("Co chcesz teraz zrobić? "))
        print("0 - wyjscie z programu")
        print("1 - dodawanie opinii")
        temp = input("Wpisz cyfre: ")

        if temp == "1":
            functions.dodaj_opinie()
            menu()
        elif temp == "0":
            sys.exit(0)
        else:
            print("bledny wybor")
            menu()

    if temp == "2":
        print(("Co chcesz teraz zrobić? "))
        print("0 - wyjscie z programu")
        print("1 - dodawanie firmy")
        temp = input("Wpisz cyfre: ")

        if temp == "1":
            functions.dodawanie_firmy()
            menu()
        elif temp == "0":
            sys.exit(0)
        else:
            print("bledny wybor")
            menu()

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
