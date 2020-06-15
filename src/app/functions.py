from src.app import operations


def rejestracja_uzytkownika():
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj imie: ")

    operations.dodaj_uzytkownika(imie, nazwisko)

def dodawanie_firmy():
    nazwa = input("Podaj nazwe firmy: ")
    branza = input("Podaj branze: ")
    miasto = input("Podaj miasto, w ktorym sie znajduje: ")
    liczba_opinii = "0"
    srednia = "0"


    operations.dodaj_firme(nazwa, branza, miasto, liczba_opinii, srednia)