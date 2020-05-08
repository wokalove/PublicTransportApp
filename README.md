# Połączenia MPK Kraków
połączenia autobusowe i tramwajowe, bus and tram routes app

PL
--

Opis działania: 
-

Aplikacja służąca do wyszukiwania połączeń autobusowych i tramwajowych MPK Kraków w języku Python.
Po uruchomieniu programu pojawia się okno  możliwością wyszukiwania połączenia albo zakończenia programu. Jeśli użytkownik wybierze wyszukiwanie połączenia to pojawia się nowe okno z miejscami na wpisanie przystanku początkowego i przystanku końcowego. Następnie po kliknięciu przycisku wyszukiwania pojawiają się dostępne linie tramwajowe czy autobusowe za pomocą których dojedziemy do celu.
Wybieramy, którą linią chcemy dojechać do celu i pokazują nam się kolejno przystanki autobusowe po drodze do końcowej stacji.
Aplikacja pyta również, czy jest studentem czy dorosłym i na końcu oblicza koszty podróży. 

Testy
-
1. Wprowadzenie danych (stacja początkowa i końcowa) przez uzytkownika i sprawdzenie czy istnieją w bazie MPK Kraków - w przeciwnym wypadku aplikacja "upomina", że mogły zostać wpisane niepoprawne dane.
2. Wybranie rodzaju biletu - możliwe warianty: student lub dorosły. Jeśli użytkownik nie wybierze żadnego z nich wypisuje się komunikat o wybraniu nieistniejącej opcji i pojawia się możliwość ponownego wyboru.
3.Na podstawie wpisanych danych przez użytkownika wyszukiwanie numerów linii pojazdów w bazie danych.
4. Wsciśnięcie przycisku odpowiadającego za szukanie - wyświetlenie na ekran możliwych linii autobusowych/tramwajowych prowadzących do celu. 
5. Realizacja połączenia z punktu A do B i wypisywanie przystanków prowadzących do celu.
6. Realizacja połączenia  z punktu B do A (jazda w "drugą stronę") i wypisywanie przystanków prowadzących do celu.
7. Kliknięcie przycisku odpowiadającego za zakończenie programu spowoduje wyjście z niego.


W tej aplikacji skorzystano z bazy danych MPK, bibliotek: sqlite3, tkinter. Stosuję również w programie podstawowe zapytania do bazy (MySQL).
Aplikacja nie uwzględnia korzystania z czasów odjazdów i przyjazdów z racji tego, że w tej bazie MPK ich brakuje.
Aplikacja będzie również napisana w języku angielskim w celu doskonalenia znajomości od strony techniczno -programistycznej tego języka.

-----------------------------------------------------------------------------
EN

Application which is used for finding MPK Cracow bus and tram connections in Python's language.

Shortened app description:
1. User enters bus stop and destination
2. App looks for direct and indirect tram/bus connections from A to B and from B to A 

direct:
- shows which one bus/tram we should choose to reach our final destination
- shows stops respectively which leads to our final destination

indirect:
- shows which one bus/tram we should choose to reach our destination
- shows stops respectively which leads to our intermidiate destination
- shows stops respectively which leads from our intermidiate destination to our final destination

App doesn't include time departures and arrivals usage because of not complited data base from MPK Cracov.
