# Prompty, które opisują wykonanie

Dobry prompt rozstrzyga, kto robi co, w jakim kadrze i czasie. Unikaj długich list przymiotników. Nie stosuj sztywnej liczby słów, zakazanych określeń estetycznych ani obowiązkowej formuły końcowej. Styl wynika z briefu i obserwowanego obrazu.

## Wzorzec postaci

Napisz naturalny opis, na przykład:

> Fikcyjna dorosła kobieta około 30 lat, owalna twarz, brązowe oczy, ciemnobrązowe włosy do ramion z przedziałkiem po lewej. Oliwkowa koszula bez wzorów. Portret do pasa na neutralnym jasnym tle, miękkie światło z lewej, widoczna naturalna faktura skóry, spokojna mimika i kontakt wzrokowy z obiektywem. Perspektywa na wysokości oczu, bez szerokokątnego zniekształcenia. Jedna osoba, bez kolażu i napisów.

To przykład, nie stały casting. Dla mężczyzny lub innego briefu napisz własny opis. Nie wymuszaj identycznej urody we wszystkich kampaniach. Jeśli postać ma trzymać produkt, podaj wzorzec produktu, realistyczną skalę oraz dłoń i sposób chwytu. Nie łącz kilku niezależnie wygenerowanych twarzy w jeden „pakiet tej samej osoby”.

## Kontrakt pojedynczego klipu

Każdy prompt powinien dać się uruchomić bez historii rozmowy:

1. **Wynik:** długość, proporcje, estetyka, język mowy i ewentualny brak mowy.
2. **Referencje:** mapa plik → rola. Oznaczenia robocze `POSTAC`, `PRODUKT`, `SCENA` są nazwami w planie, nie magicznymi tagami API. W wywołaniu użyj składni aktualnego narzędzia i zachowaj kolejność.
3. **Stan początkowy:** ciało, dłonie, produkt, ubiór, tło, kierunek światła, perspektywa kamery.
4. **Oś czasu:** niepokrywające się przedziały obejmujące cały klip. Przybliżone okna obejmują całe czynności; fazy gestu przechodzą płynnie jedna w drugą. Zaznacz cięcia i celowe pauzy, bez obowiązkowego zatrzymywania na każdej klatce referencyjnej. Określ, co zmienia się w scenie wskutek działania, jego kierunek, zakres i tempo oraz cel ewentualnego ruchu kamery. Przy pracy dłoni i dynamicznych demonstracjach zastosuj [naturalny ruch i dynamikę sceny](ruch-i-klatki.md).
5. **Dźwięk:** dokładne słowa w cudzysłowie, okna czasowe, tempo, barwa, pauzy i odgłosy. Muzyka nie zagłusza głosu.
6. **Stan końcowy i stałe cechy:** pozycja produktu i dłoni do montażu, twarz, głos, światło, geometria i nadruk.

Przykład fragmentu 10-sekundowego promptu:

> 0,0–1,0 s: półzbliżenie, kamera na wysokości oczu. Bohaterka trzyma zamknięty produkt przy klatce piersiowej, etykietą do obiektywu. Krótki wdech.
> 1,0–4,0 s: unosi produkt o kilka centymetrów, chwyt pozostaje pewny, nadgarstek naturalnie dopasowuje ustawienie. Mówi: „Zobacz, jak otwiera się ten kubek”.
> 4,0–7,0 s: cięcie na dłonie. Jedną dłonią stabilizuje kubek, kciukiem drugiej otwiera mechanizm zgodnie z jego prawdziwą konstrukcją. Brak mowy, słychać kliknięcie.
> 7,0–9,3 s: wraca półzbliżenie, produkt w tej samej orientacji. Mówi: „Sprawdź szczegóły na stronie”.
> 9,3–10,0 s: spokojny końcowy kadr, usta zamknięte, produkt pozostaje widoczny.

Demonstrację stosuj tylko, gdy konstrukcja jest potwierdzona. Jeśli nie znamy mechanizmu, zastąp otwarcie prostym obrotem produktu. Znaczniki czasu są instrukcją reżyserii, nie gwarancją wykonania z dokładnością do klatki; dokładne trafienia poprawiaj w montażu.

## Mowa po polsku i angielsku

Na początku wybierz źródło głosu: aktor mówiący w kadrze albo osobny lektor. „Narration voice” określa tryb, nie język. Jeśli język filmu nie został podany, zapytaj o niego przed napisaniem wypowiedzi. Zastosuj [dobór silnika głosu](dobor-glosu.md): angielski korzysta z wbudowanego głosu Higgsfield, polski i bardziej charakterystyczne głosy z ElevenLabs. Dla narracji po polsku zastosuj [polską narrację](polska-narracja.md). Tekst lektora trafia do wybranej syntezy mowy; prompt wybranego generatora wideo opisuje obraz, brak mówienia i brak generowanego audio, jeśli tryb to obsługuje. Nie wkładaj tekstu w usta aktora, który ma tylko prezentować produkt. Gotową ścieżkę lektora dołącz do filmu w montażu.

Język technicznego promptu nie jest językiem dialogu. Dokumentacja pozostaje polska. Jeśli wybrany model korzysta na angielskich instrukcjach wizualnych, można przetłumaczyć tylko te instrukcje, zachowując dokładny tekst wypowiedzi w języku wybranym przez użytkownika i jawną komendę języka mowy.

W polskim tekście używaj naturalnej składni, poprawnych końcówek i krótkich zdań. Liczby i skróty zapisuj w dialogu tak, jak mają być wypowiedziane; nazwę marki zachowaj prawidłowo, wymowę opisz osobno, gdy jest niejednoznaczna. Nie dodawaj doświadczenia typu „używam od miesiąca”, jeśli jest to fikcyjny prezenter, a doświadczenie nie zostało potwierdzone.

Do roboczego oszacowania przyjmij około 2 słów na sekundę faktycznej mowy. To ostrożny punkt wyjścia, nie limit języka ani obietnica modelu. W 10 sekundach z gestami i pauzami może zostać tylko 6–7 sekund na zdanie. Zostaw około 0,5–1 sekundy bez mowy przy ważnych łączeniach. Długie polskie słowa, liczby i nazwy własne wymagają więcej czasu. Ostateczną decyzję opieraj na odsłuchu, nie samym liczniku.

Przy przeładowaniu skróć zdanie albo rozdziel scenę na samodzielne wypowiedzi. Nie przyspieszaj głosu, żeby ukryć błąd planu. Jeśli polska wymowa lub synchronizacja ust zawodzi, przetestuj krótkie reprezentatywne zdanie w już zleconym pierwszym klipie. Alternatywą jest lektor nad demonstracją bez widocznej mówiącej twarzy; zmiana formatu wymaga zgodności z intencją użytkownika.

## Ciągłość i odmiany

Kolejne generacje nie pamiętają poprzednich. Wysyłaj wybrane wzorce i powtarzaj istotne cechy. Samo „ta sama kobieta” jest niewystarczające. Klatkę końca poprzedniego klipu dodaj tylko, gdy pomaga dopasować ruch i nie wypiera kluczowego zdjęcia produktu. Głos opisany identycznie może nadal się różnić — sprawdź go na połączeniu.

Nie wymagaj od jednego ujęcia jednocześnie mówienia do kamery, otwierania skomplikowanego pudełka i szybkiego najazdu na drobny napis. Rozdziel funkcje pomiędzy kadry. Przy wariantach reklam zmieniaj jeden istotny element, np. pierwsze zdanie albo demonstrację, aby wynik dało się porównać. Nie generuj zestawu wariantów bez zlecenia.
