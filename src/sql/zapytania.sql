#1. Dodawanie do bazy uzytkownikow
INSERT INTO uzytkownik (id_uzytkownik, imie, nazwisko, login, haslo) VALUES (%s, %s, %s, %s, %s)

#2. Dodawanie do bazy firm
INSERT INTO firma (id_firma, nazwa, branza, miasto) VALUES (%s, %s, %s, %s)

#3. Dodawanie opinii do bazy odnosnie konkretnej firmy przez konkretnego uzytkownika
INSERT INTO opinie (id_opinia, liczba_gwiazdek, opis, FirmaID, UzytkownikID) VALUES (%s, %s, %s, %s, %s)

#4. Pokazywanie detali firmy
SELECT id_firma, nazwa, branza, miasto, liczba_opinii, srednia FROM firma

#5. Wyszukiwanie rankingu konkretnych firm w podanej branzy
SELECT nazwa, AVG(liczba_gwiazdek) FROM opinie INNER JOIN firma ON opinie.FirmaID=firma.id_firma WHERE firma.branza= %s GROUP BY nazwa ORDER BY liczba_gwiazdek DESC

#6. Wyswietlanie opinii
SELECT opis, liczba_gwiazdek FROM opinie WHERE FirmaID = %s

#7. Logowanie
SELECT id_uzytkownik FROM uzytkownik WHERE login = %s AND haslo = %s

#8. Wyswietlanie branz
SELECT branza FROM firma

#9. Wyswietlanie wszystkich opinii zalogowanego uzytkownika
SELECT opinie.liczba_gwiazdek, opinie.opis, firma.nazwa FROM opinie INNER JOIN firma ON opinie.FirmaID=firma.id_firma WHERE opinie.UzytkownikID = %s

#10. Usuwanie opinii
DELETE FROM firma WHERE id_firma = %s

#11. Edycja opinii

#12. Ranking uzytkownikow kto dodal najwiecej opinii
SELECT `UzytkownikID`, COUNT(UzytkownikID) AS `liczba opinii tego uzytkownika` FROM `opinie` GROUP BY `UzytkownikID` ORDER BY `liczba opinii tego uzytkownika` DESC
