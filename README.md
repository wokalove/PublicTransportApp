# MPK - niedokończona, not complited!
bus and tram routes app

Aplikacja służąca do wyszukiwania połączeń autobusowych i tramwajowych MPK Kraków w języku Python

Krótki opis działania:
1. Użytkownik wpisuje gdzie wsiada i dokąd jedzie
2. Aplikacja wyszukuje dojazdy bezpośrednie jak i pośrednie z punktu A do B i z B do A ( " w tę i z powrotem")

bezpośrednie:
- którym tramawjem dojedziemy
- pokazuje kolejno przystanki prowadzące do celu

pośrednie:
- którymi tramwajami dojedziemy
- pokazuje przystanki prowadzące do celu pośredniego
- pokazuje przystanki od celu pośredniego do ostatecznego celu

W aplikacji skorzystano z bazy danych MPK, sqlite3, bibiloteki tkinter.
Aplikacja nie uwzględnia korzystania z czasów odjazdów i przyjazdów z racji tego, że w tej bazie MPK ich brakuje.

-----------------------------------------------------------------------------
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
