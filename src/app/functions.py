from src.app import operations


def rejestracja_uzytkownika():
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    login = input("Podaj login: ")
    haslo = input("Podaj haslo: ")

    operations.dodaj_uzytkownika(imie, nazwisko, login, haslo)

def dodawanie_firmy():
    nazwa = input("Podaj nazwe firmy: ")
    branza = input("Podaj branze: ")
    miasto = input("Podaj miasto, w ktorym sie znajduje: ")
    liczba_opinii = "0"
    srednia = "0"

    operations.dodaj_firme(nazwa, branza, miasto)


def dodaj_opinie():
    print("Oto firmy istniejace w naszej bazie, wybierz interesujaca Cie: ")
    operations.wyswietlanie_firm()

    firma_id = input("Podaj id firmy sposrob wyswietlonych")
    print("Podaj ocene od 1-5")
    while 1:
        liczba_gwiazdek = input()
        if int(liczba_gwiazdek) >= 1 and int(liczba_gwiazdek) <= 5:
            break
        else:
            print("Ocena poza skala")
    opinia = input("Dodaj opis opinii")
    operations.dodawanie_opinii(liczba_gwiazdek, opinia, firma_id)

def przegladaj_opinie():
    print("Oto firmy istniejace w naszej bazie, wybierz interesujaca Cie: ")
    operations.wyswietlanie_firm()
    id_firma_id = input("Podaj id firmy sposrob wyswietlonych")
    operations.wyswietlanie_opinii(id_firma_id)

def zaloguj():
    print("Zaloguj sie: ")
    while 1:
        login = input("Podaj login ")
        haslo = input("Podaj haslo ")
        iduzytkownika = operations.logowanie(str(login), str(haslo))
        if (iduzytkownika is not None):
            break
        else:
            print("Bledne dane, sprobuj jeszcze raz")

def wyswietl_ranking():
    print("Oto firmy istniejace w naszej bazie, wybierz interesujaca Cie: ")
    operations.wyswietlanie_branz()
    branza= input("Podaj branze do przegladniecia opinii")
    operations.ranking_fryzjerow(branza)