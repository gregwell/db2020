#1. Dodawanie do bazy uzytkownikow
INSERT INTO uzytkownik (id_uzytkownik, imie, nazwisko) VALUES (%s, %s, %s)

#2. Dodawanie do bazy firm
INSERT INTO firma (id_firma, nazwa, branza, miasto) VALUES (%s, %s, %s, %s)

#3. Dodawanie opinii do bazy odnosnie konkretnej firmy przez konkretnego uzytkownika
INSERT INTO opinie (id_opinia, liczba_gwiazdek, opis, FirmaID) VALUES (%s, %s, %s, %s)

#4. Pokazywanie detali firmy
SELECT id_firma, nazwa, branza, miasto, liczba_opinii, srednia FROM firma

#5. Wyszukiwanie rankingu konkretnych firm w podanej branzy w wybranym miescie //tutaj dodane z góry - trzeba zmienić
SELECT nazwa, AVG(liczba_gwiazdek) FROM opinie INNER JOIN firma ON opinie.FirmaID=firma.id_firma WHERE firma.miasto="Krakow" AND firma.branza="Fryzjer" GROUP BY nazwa ORDER BY liczba_gwiazdek DESC

#6. Wyswietlanie opinii
SELECT opis, liczba_gwiazdek FROM opinie WHERE FirmaID = %s
