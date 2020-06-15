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


def dodaj_opinie():
    print("Oto firmy istniejace w naszej bazie, wybierz interesujaca Cie: ")
    operations.wyswietlanie_firm()

    firma_id = input("Podaj id firmy sposrob wyswietlonych")
    print("Podaj ocene od 1-5")
    while 1:
        liczba_gwiazdek = input()
        if liczba_gwiazdek >= 1 and liczba_gwiazdek <= 5:
            break
        else:
            print("Ocena poza skala")
    opinia = input("Dodaj opis opinii")
    operations.dodawanie_opinii(liczba_gwiazdek, opinia, firma_id)