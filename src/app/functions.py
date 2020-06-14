from src.app import operations


def rejestracja_uzytkownika():
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj imie: ")

    operations.dodaj_uzytkownika(imie, nazwisko)
