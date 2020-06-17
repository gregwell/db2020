import mysql.connector
import sys

from src.app import operations, functions

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="trustnet")

mycursor = mydb.cursor()

def menu():
    print("Zaloguj sie: ")
    while 1:
        login = input("Podaj login ")
        haslo = input("Podaj haslo ")
        iduzytkownika = operations.logowanie(str(login), str(haslo))
        if (iduzytkownika is not None):
            break
        else:
            print("Bledne dane, sprobuj jeszcze raz")


    print(("Co chcesz teraz zrobić? "))
    print("0 - wyjscie z programu")
    print("1 - obsluga uzytkownika")
    print("2 - obsluga firmy")
    print("3 - opinie")
    print("4 - przegladaj opinie i rankingi")
    temp = input("Wpisz cyfre: ")

    if temp == "4":
        print(("Co chcesz teraz zrobić? "))
        print("0 - wyjscie z programu")
        print("1 - przegladaj opinie o wybranej firmie")
        print("2 - wyswietl ranking firm")
        print("3 - wyswietl ranking uzytkownikow")
        temp = input("Wpisz cyfre: ")

        if temp == "2":
            functions.wyswietl_ranking()
            menu()
        elif temp == "1":
            functions.przegladaj_opinie()
            menu()
        elif temp == "3":
            operations.ranking_uzytkownikow()
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
        print("2 - edytuj opinie")
        temp = input("Wpisz cyfre: ")

        if temp == "1":
            functions.dodaj_opinie(iduzytkownika)
            menu()
        if temp == "2":
            print("Oto twoje opinie, wybierz id opinii, ktora chcesz zmienic")
            functions.wyswietl_moje_opinie(iduzytkownika)
            functions.edytuj_opinie()
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
        print("2 - usuwanie firmy")
        temp = input("Wpisz cyfre: ")

        if temp == "1":
            functions.dodawanie_firmy()
            menu()
        elif temp == "0":
            sys.exit(0)
        elif temp =="2":
            functions.usun_firme()
            menu()
        else:
            print("bledny wybor")
            menu()

    if temp == "1":
        print(("Co chcesz teraz zrobić? "))
        print("0 - wyjscie z programu")
        print("1 - rejestracja uzytkownika")
        print("2 - pokaz moje opinie ")
        temp = input("Wpisz cyfre: ")
        if temp == "1":
            functions.rejestracja_uzytkownika()
            menu()
        elif temp == "0":
            sys.exit(0)
        elif temp == "2":
            functions.wyswietl_moje_opinie(iduzytkownika)
            menu()
        else:
            print("bledny wybor")
            menu()
    elif temp == "0":
        sys.exit(0)
    else:
        print("bledny wybor")
        menu()

menu()
