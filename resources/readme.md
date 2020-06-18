# Trustnet


| Nazwisko i imię | Wydział | Kierunek | Semestr | Grupa | Rok akademicki |
| :-------------: | :-----: | :------: | :-----: | :---: | :------------: |
| Grzegorz Studziński         | WIMiIP  | IS       |   4     | 4     | 2019/2020      |
| Michał Stawarski         | WIMiIP  | IS       |   4     | 4     | 2019/2020      |

## Struktura projektu
```bash
.
├── /resources/    # Pliki zasobów w projekcie (SS, rysunki, schematy)
│   └── /README.md # Opis projektu w formie pliku markdown
├── /src/          # Katalog główny projektu
│   ├── /app/      # Kod źródłowy aplikacji
│   └── /sql/      # Zapytania SQL
├── /.gitignore    # Pliki i foldery pomijane przy commitowaniu do repozytorium
└── /README.md     # Opis projektu: wytyczne
```
### Projekt bazy danych

<img src="/resources/bazadanychplik.png">

Przykładowe tworzenie tabeli:
```
CREATE TABLE `firma` (
  `id_firma` int(11) NOT NULL,
  `nazwa` text COLLATE utf8_polish_ci NOT NULL,
  `branza` text COLLATE utf8_polish_ci NOT NULL,
  `miasto` text COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
```

### Implementacja zapytań SQL
W pliku zapytania.sql

#1. Dodawanie do bazy uzytkownikow
```
INSERT INTO uzytkownik (id_uzytkownik, imie, nazwisko, login, haslo) VALUES (%s, %s, %s, %s, %s)
```

#2. Dodawanie do bazy firm
```
INSERT INTO firma (id_firma, nazwa, branza, miasto) VALUES (%s, %s, %s, %s)
```

#3. Dodawanie opinii do bazy odnosnie konkretnej firmy przez konkretnego uzytkownika
```
INSERT INTO opinie (id_opinia, liczba_gwiazdek, opis, FirmaID, UzytkownikID) VALUES (%s, %s, %s, %s, %s)
```

#4. Pokazywanie detali firmy
```
SELECT id_firma, nazwa, branza, miasto, liczba_opinii, srednia FROM firma
```

#5. Wyszukiwanie rankingu konkretnych firm w podanej branzy
```
SELECT nazwa, AVG(liczba_gwiazdek) FROM opinie INNER JOIN firma ON opinie.FirmaID=firma.id_firma WHERE firma.branza= %s GROUP BY nazwa ORDER BY liczba_gwiazdek DESC
```

#6. Wyswietlanie opinii, rosnaco
```
SELECT opis, liczba_gwiazdek FROM opinie WHERE FirmaID = %s ORDER BY liczba_gwiazdek ASC
```

#7. Logowanie

```
SELECT id_uzytkownik FROM uzytkownik WHERE login = %s AND haslo = %s
```

#8. Wyswietlanie branz
```
SELECT branza FROM firma GROUP BY branza
```

#9. Wyswietlanie wszystkich opinii zalogowanego uzytkownika
```
SELECT opinie.liczba_gwiazdek, opinie.opis, firma.nazwa FROM opinie INNER JOIN firma ON opinie.FirmaID=firma.id_firma WHERE opinie.UzytkownikID = %s
```

#10. Usuwanie firmy
```
DELETE FROM firma WHERE id_firma = %s
```

#11. Edycja opinii
```
UPDATE opinie SET opis = %s, liczba_gwiazdek = %s WHERE id_opinia = %s
```

#12. Ranking uzytkownikow kto dodal najwiecej opinii
```
SELECT `UzytkownikID`, COUNT(UzytkownikID) AS `liczba opinii tego uzytkownika` FROM `opinie` GROUP BY `UzytkownikID` ORDER BY `liczba opinii tego uzytkownika` DESC
```

-- #13. Wyswietlanie opinii firmy, w ktorej istnieje opis
```
-- SELECT opinie.opis, opinie.liczba_gwiazdek, uzytkownik.login FROM opinie INNER JOIN uzytkownik WHERE opinie.opis IS NOT NULL AND opinie.FirmaID = %s AND opinie.UzytkownikID = %s'' ||
```

### Aplikacja
Aplikacja konsolowa
