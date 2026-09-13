---
name: reklama-z-referencji
description: "Twórz reklamy produktowe UGC z linku lub zdjęcia produktu: najpierw własna postać, następnie adaptacja filmu referencyjnego, scenariusz sekundowy i produkcja. Używaj także do kontynuacji tej reklamy i jej wariantów. Nie używaj do samego montażu istniejącego filmu ani do ogólnej analizy marketingowej."
---

# Reklama z referencji

Prowadź użytkownika od produktu do reklamy z własnym bohaterem. Film referencyjny wyznacza rytm i sposób prezentacji; powstaje nowa scena, nowy tekst i własna demonstracja produktu. Rozmawiaj i zapisuj dokumentację po polsku. Język wypowiedzi w filmie wynika z briefu; domyślnie polski.

## Prosty start

Przyjmij link albo zdjęcie produktu oraz podany wybór postaci: kobieta lub mężczyzna. Nie wymagaj filmu referencyjnego, żeby zacząć tworzyć bohatera. Jeśli użytkownik od razu dostarczył komplet, wykorzystaj go bez ponownego zbierania danych.

Nie zadawaj ankiety. Ustal tylko brak, który zmienia najbliższy krok. Przy braku wyboru postaci zadaj jedno pytanie; równolegle poznaj produkt. Pozostałe rozsądne domyślne założenia: jedna dorosła fikcyjna osoba, jeden koncept, pion 9:16, naturalna prezentacja. Gdy jest referencja, dopasuj estetykę i długość do niej, chyba że brief mówi inaczej. Bez referencji proponuj roboczo 20 sekund; nie przedstawiaj własnego pomysłu jako analizy filmu.

Zapamiętuj wybory. „Dalej” kontynuuje bieżący projekt. Nowy produkt nie dziedziczy automatycznie starej twarzy, obietnic ani zgody na wydatki.

## 1. Produkt i własna postać

Obejrzyj dostarczony obraz lub rzeczywiście otwórz stronę produktu. Zapisz krótko: co sprzedajemy, komu, jedną potwierdzoną zaletę, widoczny wariant i wezwanie do działania. Oddziel obserwacje od hipotez. Zdjęcie nie potwierdza składu, skuteczności, ceny, pojemności ani rabatu, jeśli nie są czytelne. Przy nieczytelnej etykiecie zachowaj obraz jako źródło wyglądu, bez odgadywania napisów.

Zaprojektuj jedną postać zgodną z wyborem użytkownika: przybliżony wiek osoby dorosłej, twarz, włosy, sylwetka, ubiór i sposób bycia dopasowane do reklamy. Nie wywodź jej wyglądu z twarzy autora referencyjnej reklamy. Podaj konkretny prompt portretowy z [instrukcji promptowania](references/promptowanie.md), a następnie wygeneruj obraz, jeśli wykonanie generacji jest w zakresie zlecenia i narzędzia są dostępne. Sam opis postaci nie jest gotowym obrazem.

Domyślnie wystarczy jeden czytelny portret do pasa w neutralnym świetle. Dodatkowy kąt twarzy lub zdjęcie z produktem twórz tylko, gdy rozwiązuje konkretny problem sceny. Obejrzyj wynik: twarz, dłonie i ewentualny produkt. Gdy produkt jest błędny, popraw obraz przed użyciem w filmie.

Pokaż obraz i wskaż przyjęty wygląd. Przy pracy etapami użytkownik może wybrać albo poprawić postać, przesyłając następnie film referencyjny. Nie wymagaj dodatkowego zatwierdzenia, jeżeli już polecił samodzielnie wybrać postać i wykonać całość. Zachowaj jej obraz jako wzorzec tożsamości; z późniejszej referencji można dopasować ubiór i otoczenie, zachowując twarz.

## 2. Referencja i własna interpretacja

Na tym etapie wykorzystaj dostarczony film albo poproś o plik/link. Gdy użytkownik dostarcza własny wybrany obraz postaci, traktuj go jako aktualny wzorzec. Nie każ przesyłać ponownie obrazu wygenerowanego w tej samej rozmowie, jeśli nadal masz do niego dostęp.

Gdy użytkownik podaje link do reklamy, filmu lub strony z osadzonym wideo, najpierw użyj `yt-dlp`, aby pobrać wskazany film do katalogu kampanii i przeanalizować lokalny plik. Nie odsyłaj użytkownika od razu do ręcznego pobierania. Procedura i obsługa niepowodzeń: [pobieranie referencji](references/analiza-referencji.md#pobieranie-filmu-z-linku). Link do nieruchomej grafiki lub dzieła obsłuż jako obraz; jeśli strona zawiera film, zastosuj ścieżkę wideo.

Obejrzyj materiał i odsłuchaj dźwięk dostępną metodą. Agent multimodalny może wykonać analizę bez narzuconego zewnętrznego transkrybenta lub podwójnego badania. Klatki i pomiary techniczne stosuj do niejasnych cięć, tekstu i synchronizacji. Szczegóły: [analiza referencji](references/analiza-referencji.md). Brak jednego pomocniczego narzędzia nie blokuje pracy, gdy masz wystarczające dowody. Brak dostępu do samego filmu oznacza brak analizy; nie zgaduj treści z miniatury.

Zapisz zwięzłą mapę: czas → zadanie ujęcia → widoczne działanie → nasza wersja. Zachowuj np. bliskie otwarcie, opóźnione ujawnienie produktu, rytm cięć lub demonstrację podczas mówienia. Zmieniaj słowa, szczegóły inscenizacji i wykonanie. Nie kopiuj charakterystycznego scenariusza ani cudzej tożsamości. Domyślnie film służy do obserwacji; nie przesyłaj go automatycznie do generatora.

Wybierz format z materiału: wypowiedź do kamery, demonstracja, rozpakowanie, produkt bez twarzy albo prezentacja aplikacji. Nie narzucaj wszystkich formatów naraz. Rozpakowanie wymaga spójnej kolejności stanów opakowania; aplikacja wymaga rzeczywistych materiałów ekranu. Przy formacie bez twarzy pomiń casting, jeśli taki jest cel użytkownika.

## 3. Plan gotowy do generacji

Przeczytaj [promptowanie](references/promptowanie.md) i dopasuj wykonanie według [możliwości modeli](references/mozliwosci-modeli.md). Rdzeń nie wymaga konkretnego modelu. Higgsfield jest opcjonalnym, preferowanym połączeniem do produkcji; nie wprowadzaj innych obowiązkowych platform generacji.

Najpierw napisz jeden spójny scenariusz. Dopiero potem wybierz jedną generację lub podział na klipy, zgodnie z faktycznym limitem czasu, referencji i jakością wymaganej mowy. Potężniejszy agent upraszcza organizację pracy; nie zmienia limitów generatora wideo.

Każdy klip dostaje samodzielny prompt: czas i format, przypisanie referencji, postać i produkt, otoczenie, lokalną oś czasu od 0 s, dokładny dialog, dźwięk, początek i koniec ruchu oraz warunki ciągłości. Dla każdej wypowiedzi wyznacz rzeczywiste okno mowy z miejscem na oddech. Dłuższy film ma także jedną globalną oś montażu. Nie tnij zdania między generacjami.

Przy limicie 7 zdjęć najpierw rezerwuj miejsca dla tożsamości i produktu. Można dołączyć wybrane klatki, jeśli zostaje miejsce; pozostałe zdarzenia opisz czasowo. Nie wysyłaj całej siatki klatek w nadziei na obejście limitu. Przy większym limicie użyj tylko tych klatek, które niosą nową informację.

Pokaż użytkownikowi: obraz bohatera, krótki koncept, scenariusz z czasami, przypisanie zdjęć i konkretny zakres generacji z dostępną wyceną. Pliki techniczne obsługuj sam. Pełne prompty zachowaj jako edytowalne pliki, dostępne do wglądu. W trybie „tylko prompty” tu kończy się zadanie.

## 4. Produkcja i odbiór

Wykonuj już zlecone generacje bez powtarzania pytań o zgodę. Samo zlecenie analizy lub promptów nie obejmuje generacji. Gdy zakres płatnej produkcji nie jest ustalony, najpierw przygotuj dostępne bez generacji materiały i wycenę dla konkretnego etapu; zapytaj wyłącznie o brakującą decyzję. Nie dokupuj kredytów ani nie uruchamiaj nieograniczonych wariantów. Wymagany przez narzędzie wybór sposobu rozliczenia przekaż użytkownikowi.

Przed wywołaniem sprawdź aktualny schemat narzędzia, tryb i rolę każdego pliku. Portret jest referencją tożsamości, nie automatycznie pierwszą klatką filmu. Po estymacji porównaj skorygowane parametry z planem; automatyczne skrócenie czasu wymaga przeplanowania. Zapisuj identyfikator zadania od razu. Po przerwaniu sprawdź istniejące zadanie, zamiast wysyłać drugie.

Obejrzyj każdy wynik i odsłuchaj dialog przed montażem. Wykonaj [kontrolę jakości](references/odbior.md). Poprawiaj konkretny błąd i tylko dotknięty klip. Domyślnie najwyżej jedna ponowna generacja na wadliwy klip, wyłącznie w już ustalonym zakresie i budżecie; potem pokaż problem i możliwą zmianę sceny. Awaria nie oznacza automatycznie moderacji. Nie obchodź odrzucenia przez ukrywanie treści.

Połącz klipy, jeśli zadanie obejmuje gotowy film, i sprawdź całość: rzeczywisty czas, dźwięk na łączeniach, tożsamość, produkt, ostatnie słowo i wezwanie do działania. Napisy dodawaj w montażu, gdy są zamówione, na podstawie gotowego dźwięku. Zachowuj prawdziwy nadruk na produkcie; nie utożsamiaj go z napisami ekranowymi.

Zwróć odtwarzalny film albo jasno nazwany rezultat częściowy, wraz z promptami i krótką informacją o sprawdzonych elementach oraz pozostałych wadach. Gdy brakuje narzędzi, dostarcz gotowe prompty i listę załączników, bez twierdzenia, że render powstał. Nie publikuj reklamy automatycznie.

## Pamięć projektu

W katalogu kampanii poza dystrybuowanym skillem przechowuj `projekt.md`: brief, potwierdzone informacje, wybrana postać, wzorce produktu, źródła, plan, wersja i następny krok. Dodaj prompty oraz `generacje.json` dopiero przy produkcji: parametry bez sekretów, zakres zlecenia, koszt znany/szacowany, identyfikatory zadań, statusy i pliki wynikowe. Nie nadpisuj przyjętych wersji. Zmiana twarzy unieważnia zależne ujęcia; zmiana samego wezwania do działania nie wymaga ponownego castingu.

Do planów wieloklipowych użyj pomocniczego [sprawdzania planu](references/sprawdzanie-planu.md), które wykrywa błędny czas i nadmiar referencji. Przykład przejścia przez workflow: [próba bez generacji](references/przyklad.md). Nie ładuj tych materiałów, jeśli bieżący krok ich nie wymaga.
