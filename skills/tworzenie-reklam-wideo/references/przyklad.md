# Próba planowania: kubek PORANEK

To fikcyjny brief do sprawdzenia skilla. Nie przedstawia obejrzanego filmu, wygenerowanej postaci ani wykonanej reklamy. Nazwa produktu, cechy i poniższa struktura referencji zostały wymyślone na potrzeby ćwiczenia. Identyfikatory obrazów to planowane role; nie są istniejącymi mediami ani identyfikatorami API.

## Wejście w dwóch wiadomościach

**Pierwsza wiadomość:** „Mam matowy niebieski kubek PORANEK z białym napisem, pojemność 350 ml, pokrywka otwierana przyciskiem. Zrób bohaterkę około 30 lat. Reklama po polsku. Na razie tylko przygotowanie, bez generacji”.

**Reakcja:** agent zapisuje cechy jako dane briefu, nie jako wynik oglądania zdjęcia. Przygotowuje poniższy casting. Nie pyta o płeć, język ani film przed rozpoczęciem pracy. Do realnej generacji potrzebny będzie obraz produktu. Nie dopisuje szczelności, czasu utrzymywania temperatury, ceny ani opinii klientów.

**Prompt postaci:** „Fikcyjna dorosła kobieta około 30 lat, owalna twarz, brązowe oczy, ciemnobrązowe włosy do ramion z przedziałkiem po lewej. Oliwkowa koszula, bez wzorów i biżuterii. Portret do pasa, neutralne jasne tło, miękkie światło z lewej, naturalna skóra i spokojny kontakt wzrokowy. Kamera na wysokości oczu. Jedna osoba, bez produktu, kolażu i napisów”.

**Druga wiadomość:** „Wygląd pasuje. Chcę 30 sekund, dalej tylko prompty. Referencja ma zbliżenie na produkt, potem pokaz obsługi i powrót do osoby z wezwaniem do działania. Załóż generator 3–10 sekund i maksymalnie 7 obrazów”.

**Reakcja:** agent pracuje na opisie referencji, z jawną adnotacją, że nie obejrzał materiału. Nie zgłasza dokładnych cięć oryginału. Rozbudowuje wskazany mechanizm w autorski plan 3 × 10 s; dokładne czasy poniżej są jego decyzją reżyserską.

## Własny koncept

„Zobacz, jak działa” — spokojna, konkretna demonstracja bez udawanego świadectwa klientki. Produkt od początku pozostaje czytelny; główne zdarzenie to kliknięcie pokrywki. Zamiast wielu obietnic pokazujemy jedną potwierdzoną funkcję.

| Czas reklamy | Działanie | Dokładny dialog |
|---|---|---|
| 0–3 s | Półzbliżenie bohaterki z kubkiem | „Spójrz na tę pokrywkę”. |
| 3–7 s | Kubek bliżej obiektywu, palec wskazuje przycisk | „Tu jest przycisk otwierania”. |
| 7–10 s | Ustawienie dłoni do demonstracji, cisza | — |
| 10–15 s | Zbliżenie dłoni: naciśnięcie i otwarcie | — |
| 15–19 s | Pokrywka pozostaje otwarta, głos poza kadrem | „Naciskasz i gotowe”. |
| 19–20 s | Stabilny kadr bez mowy | — |
| 20–25 s | Powrót do bohaterki, kubek na blacie | „To kubek PORANEK”. |
| 25–29 s | Spojrzenie do obiektywu, dłoń przy produkcie | „Sprawdź szczegóły na stronie”. |
| 29–30 s | Zakończenie bez mowy | — |

## Mapa obrazów

W każdym klipie trzy planowane obrazy: `POSTAC` — wybrany portret, `PRODUKT` — prawdziwy kubek od przodu, `POKRYWKA` — rzeczywisty detal mechanizmu. To 3/7 miejsc w każdym wywołaniu. Przy trudnej ciągłości można dodać własną klatkę sceny, mieszcząc się w limicie. Nie potrzebujemy 12 klatek referencyjnej reklamy, żeby opisać jej rytm.

## Samodzielne prompty

### Klip 01 — 10 s

Pion 9:16, naturalna reklama produktowa z telefonu, miękkie światło dzienne z lewej. `POSTAC` określa twarz: kobieta około 30 lat, owalna twarz, brązowe oczy, ciemnobrązowe włosy do ramion z przedziałkiem po lewej. Oliwkowa koszula bez wzorów. `PRODUKT` określa matowy niebieski kubek PORANEK z białym nadrukiem; `POKRYWKA` określa prawdziwy mechanizm. Obrazy są wzorcami, nie automatycznym początkiem filmu. Kamera na wysokości oczu. Jasna kuchnia, drewniany blat, gładka kremowa ściana, bez innych produktów.

0–3 s: półzbliżenie. Bohaterka trzyma zamknięty kubek lewą dłonią, napis ku kamerze. Między 0,6 a 2,8 s mówi po polsku: „Spójrz na tę pokrywkę”. 3–7 s: unosi kubek bliżej kamery, prawy palec wskazuje przycisk bez naciskania. Między 3,5 a 6,2 s mówi: „Tu jest przycisk otwierania”. 7–10 s: bez mowy, zbliża prawy kciuk do przycisku; kubek pozostaje pionowo. Zakończ przed naciśnięciem.

Naturalny spokojny głos kobiecy o średniej wysokości, wyraźna polska wymowa, delikatny oddech i cichy dźwięk pomieszczenia. Bez muzyki. Dłonie i produkt zachowują geometrię, nadruk pozostaje jak na produkcie. Bez dodanych napisów ekranowych i logotypów w tle.

### Klip 02 — 10 s

Pion 9:16, zbliżenie dłoni i produktu, ta sama zaplanowana jasna kuchnia: drewniany blat, kremowa ściana, światło z lewej. `POSTAC` jest wzorcem kobiety około 30 lat, owalna twarz, brązowe oczy, ciemnobrązowe włosy do ramion, oliwkowa koszula bez wzorów. Twarz jest poza kadrem, widoczne mankiety. `PRODUKT` i `POKRYWKA` określają matowy niebieski kubek PORANEK z białym nadrukiem oraz rzeczywisty przycisk. Nie używaj portretu jako pierwszej klatki.

0–5 s: lewa dłoń stabilizuje pionowy zamknięty kubek, prawy kciuk spoczywa nad przyciskiem. W 2 s naciska; pokrywka otwiera się zgodnie z konstrukcją na wzorcu. Kamera pozostaje nieruchoma. Bez mowy, słychać krótkie kliknięcie. 5–9 s: kubek pozostaje otwarty, prawy kciuk odsuwa się. Między 5,5 a 7,7 s kobiecy głos poza kadrem mówi po polsku: „Naciskasz i gotowe”. 9–10 s: bez mowy, obie dłonie spokojne, produkt nadal pionowy.

Głos kobiecy o średniej wysokości, spokojny, wyraźna polska wymowa; ciche tło kuchni, bez muzyki. Kubek nie zmienia wielkości ani nadruku, pokrywka nie znika. Bez dodatkowych napisów. Ostatni kadr utrzymuje otwarty produkt do cięcia montażowego.

### Klip 03 — 10 s

Pion 9:16, naturalne półzbliżenie na wysokości oczu, jasna kuchnia z drewnianym blatem i kremową ścianą, miękkie światło z lewej. `POSTAC`: kobieta około 30 lat, owalna twarz, brązowe oczy, ciemnobrązowe włosy do ramion z przedziałkiem po lewej; oliwkowa koszula bez wzorów. Zachowaj twarz z tego wzorca. `PRODUKT` i `POKRYWKA`: matowy niebieski kubek PORANEK z białym nadrukiem i jego mechanizmem. Kubek stoi otwarty na blacie, napis zwrócony do kamery; lewa dłoń spoczywa obok, prawa jest opuszczona.

0–5 s: bohaterka patrzy na kubek, potem do kamery. Między 1 a 3,5 s mówi po polsku: „To kubek PORANEK”. 5–9 s: spokojny kontakt wzrokowy, produkt w pełni widoczny. Między 5,3 a 8,3 s mówi: „Sprawdź szczegóły na stronie”. 9–10 s: zamknięte usta, niewielki uśmiech i nieruchomy produkt. Bez dopisywania adresu strony, ceny ani rabatu.

Naturalny spokojny głos kobiecy o średniej wysokości, poprawna polska wymowa; nazwę PORANEK wypowiedz jak polskie słowo „poranek”. Cichy dźwięk kuchni, bez muzyki. Zachowaj twarz, nadruk, kolor i skalę produktu. Bez dodanych napisów ekranowych.

## Montaż i ograniczenia próby

Kolejność 01 → 02 → 03, twarde cięcia, po 10 s, bez nakładania. Lokalny czas w promptach zaczyna się zawsze od zera; globalne przesunięcia to 0, 10 i 20 s. Wypowiedzi nie przekraczają granic klipów. Faktyczny czas, głos na łączeniu i otwarta pokrywka wymagają oceny po generacji.

[Plan do walidatora](przyklad-plan.json) odzwierciedla tę oś. Jeśli rzeczywisty model obsługuje 30 s i potrzebne wejścia, można scalić opis w jeden prompt z globalnymi czasami. Jeśli limit wynosi 10 s, nie da się uzyskać nowego filmu 30 s jednym wywołaniem przez samo wpisanie takiej długości.

Następny krok rzeczywistej produkcji: dostarczenie i obejrzenie obrazu produktu oraz filmu referencyjnego, wygenerowanie i wybór postaci, sprawdzenie parametrów z załącznikami, a następnie generacja w ustalonym zakresie. W tym ćwiczeniu powstały wyłącznie prompty i plan.
