# ***RAPORT Z PROJEKTU POŁĄCZENIA MPK KRAKÓW***

## **Założenia**
Ogólnym założeniem mojego projektu było wyszukiwanie połączeń tramwajowych i autobusowych na podstawie bazy MPK Kraków z 2012 roku (niestety bardziej aktualna wersja nie była dostępna) oraz policzenie kosztów podróży.
Do realizacji tego zadania musiałam zaimplementować funkcje wyszukujące połączenia zarówno bezpośrednie jak i pośrednie. W obu przypadkach musiałam wczytać pobraną bazę danych MPK Kraków  i następnie napisać zapytania do niej (używałam w tym celu biblioteki sqlite3).

 ## **Ogólny opis kodu**
 
- **Algorytm połączenia bezpośredniego:**
1. Użytkownik wpisuje skąd i dokąd chce jechać. 
2. Wpisane dane są wyszukiwane za pomocą zapytania do bazy danych i w rezultacie otrzymujemy numery linii, którymi dojedziemy do celu.
3. Użytkownik wybiera numer linii, którą chce dojechać do celu.
4.  Następuje zapytanie do bazy o wypisanie kolejnych przystanków wpisanej linii.
5.  Wyświetlenie ile przystanków dzieli podróżnika do celu.
Aby algorytm działał w obie strony ( dojazdy w tę i z powrotem) zastosowałam sprawdzanie indeksu danego przystanku. Jeśli indeks przystanku „skąd” był wyższy niż „dokąd” to  przystanki wypisują się w odwrotnej kolejności, w przeciwnym wypadku – w takiej jakiej są.

- **Algorytm połączenia pośredniego:**
1.	Użytkownik wpisuje skąd i dokąd chce jechać.
2.	Tworzony jest graf { nr_ lini: kolejne_przystanki} – warto zwrócić uwagę na fakt, że z uwagi na wydajność programu postanowiłam dokonać jednokrotnego zapisu do pliku .json tego grafu.
3.	Odczytywanie wyżej wymieniononego grafu w programie i tworzenie na jego bazie nowego, a mianowicie połączenia danych linii pomiędzy parami sąsiednich przystanków.
4.	Następnie korzystam z algorytmu BFS do przeszukiwania grafu i optymalnej drogi do celu.
5.	Użytkownikowi po wciśnięciu „ show stops ” ukazują się połączenia wraz z poszczególnymi liniami sugerujące w których miejscach należy dokonać przesiadki.
Oprócz realizacji połączeń są obliczane koszty podróży – biorę  pod uwagę tylko bilety jednoprzejazdowe z racji tego, że w bazie danych MPK Kraków brakuje czasu odjazdów i przyjazdów.
Bilety są ulgowe i normalne – użytkownik wpisuje,czy jest studentem , czy też dorosłym. Jeśli chodzi o połączenia bezpośrednie to bilet nalicza się raz z racji, że jest jeden przejazd. W przypadku połączenia pośredniego biletów jest więcej i koszty się sumują z racji tego, że dojazd już jest kilkuprzejazdowy.

## **Co udało się zrobić, problemy, elementy specjalne, problemy z testami**

 - **Udało się**
 
Udało się zrealizować główne cele,czyli:
- [x] wyszukiwanie połaczeń pośrednich (za pomocą przeszukiwania grafu), 
- [x] wyszukiwanie połączeń bezpośrednich 
- [x] obliczanie kosztów podróży (przy pomocy dekoratorów). 

- **Napotkane problemy:**

Pierwszy problem napotkałam z zapisem do pliku .json grafu, który był tworzony na podstawie danych zwróconych z zapytań do bazy danych.
Początkowo używałam za każdym razem metodę .fetchall(), aby móc uzyskać zwrócone dane przez zapytanie. Przez tę metodę zamiast zwykłej listy przystanków tworzyła mi się listy w których był jeden przystanek w jednej dużej liście, czyli przykładowo: [[„Mydlniki”],[„Zakliki”],[„Godlewskiego”]] zamiast [„Mydlniki”,”Zakliki”,”Godlewskiego”]. 
 Tutaj znacząco pomógł mi Pan Dr Ciura, który pokazał, że dane należy wczytywać przy pomocy pętli for czyli przykładowo [tutaj](https://github.com/wokalove/MPK/blob/ad8acbab0cdb53dfb2e73d09f0366ebcb6e627ce/MPK.py#L211-L217)
 
Problemy również napotkałam przy połączeniu algorytmu BFS w dojazdach pośrednich z racji tego, że oprócz tego, że musiałam stworzyć nowy graf na podstawie wcześniej stworzonego to musiałam dodatkowo go uaktualniać, żeby dodać numery liniii do poszczególnych kluczy, które były niezbędne do informowania użytkownika, którymi liniami dojedzie do celu.
Napisłam testy do klasy Traveler i Pan Dr Ciura dodatkowo zlecił dopisanie dwóch testów do funkcji find_shortest_path , czyli do funkcji wyszukującej połączenia bezpośrednie. Z testami raczej nie napotkałam większych problemów i wyniki wychodziły zgodne z oczekiwanymi.

- **Elementy specjalne**

Myślę, że elementami specjalnymi mojego programu jest użycie dekoratorów, algorytmu BFS przeszukiwania grafu oraz zapisywanie,  wczytywanie z pliku .json. oraz korzystanie z biblioteki sqlite3, czyli importowanie bazy oraz operowanie na niej.

## **Opisane linki do istotnych fragmentów kodu:**
1.	Lambda
2.	List comprehensions
3.	Klasy
4.	Wyjątki
5.	Moduły

Wszystkie linki zawarłam w [jednym issue](https://github.com/wokalove/MPK/issues/3).
