#1. Dodawanie do bazy uzytkownikow
INSERT INTO uzytkownik (id_uzytkownik, imie, nazwisko) VALUES (%s, %s, %s)

#2. Dodawanie do bazy firm

#3. Dodawanie opinii do bazy odnosnie konkretnej firmy przez konkretnego uzytkownika


#4. Wyszukiwanie rankingu konkretnych firm w podanej branzy w wybranym miescie //tutaj dodane z góry - trzeba zmienić
SELECT nazwa, AVG(liczba_gwiazdek) FROM opinie INNER JOIN firma ON opinie.FirmaID=firma.id_firma WHERE firma.miasto="Krakow" AND firma.branza="Fryzjer" GROUP BY nazwa ORDER BY liczba_gwiazdek DESC


