# Co przenieść z filmu

Analizuj zakres wskazany przez użytkownika. Zapisz źródło, czas początku/końca i faktycznie obejrzany zakres. Dla wycinka rozróżniaj czas źródłowy i czas od początku wycinka. Jeśli dostępne są tylko klatki, wnioskuj o kompozycji, ale nie udawaj odsłuchu ani znajomości pełnego ruchu.

## Pobieranie filmu z linku

Przy linku do reklamy, filmu lub strony z osadzonym wideo użyj w pierwszej kolejności `yt-dlp`. Pobierz konkretny materiał, zachowując obraz i dostępny dźwięk. Nie pobieraj całego profilu ani playlisty, jeśli użytkownik wskazał jeden film. Przy kilku filmach na stronie ustal, który jest referencją. Samo pobranie nie jest jeszcze obejrzeniem materiału.

Sprawdź dostępność `yt-dlp` i `ffmpeg`. Jeśli brakuje programu, skorzystaj z dostępnego środowiska lub zainstaluj go lokalnie w zakresie uprawnień środowiska. Nie wymagaj od użytkownika wykonywania poleceń, które możesz wykonać sam. Gdy instalacja jest niedostępna, użyj dostępnego bezpośredniego pliku wideo lub obsługiwanej metody przeglądarkowej; dopiero po rzeczywistym niepowodzeniu poproś o plik.

Przykład wywołania po ustawieniu zmiennych na link użytkownika i katalog wejściowy kampanii:

```bash
yt-dlp --ignore-config --no-playlist --no-overwrites --restrict-filenames \
  --retries 3 --fragment-retries 3 --socket-timeout 30 \
  -P "$KATALOG_REFERENCJI" -o '%(extractor_key)s-%(id)s.%(ext)s' \
  --print after_move:filepath -- "$URL_FILMU"
```

Przekazuj URL jako oddzielny argument, bez sklejania go z kodem powłoki. Domyślny dobór formatu zachowuje najlepszy dostępny obraz i dźwięk; łączenie osobnych strumieni wymaga `ffmpeg`. Bez niego wybierz dostępny format z połączonym obrazem i dźwiękiem, np. `-f b`, zamiast przypadkowo pobrać sam obraz. Nie wymuszaj rozszerzenia MP4 przez zmianę nazwy pliku; jeśli analiza wymaga innego kontenera lub kodeka, wykonaj osobną konwersję, zachowując pobrany oryginał. Opcje sprawdzaj w aktualnej [dokumentacji yt-dlp](https://github.com/yt-dlp/yt-dlp#usage-and-options).

Odczytaj końcową ścieżkę, sprawdź powodzenie pobierania, rozmiar i odtwarzalność pliku oraz metadane obrazu i audio. Nie uznawaj pliku `.part` za gotowy materiał. W `projekt.md` zapisz źródłowy link, datę, lokalną ścieżkę i zakres przeznaczony do analizy. Media pozostają w kampanii, poza paczką skilla. Nie zapisuj ciasteczek, tokenów ani podpisanych adresów pobierania w dokumentacji.

Przy błędzie ustal przyczynę: nieobsługiwana strona, nieaktualny ekstraktor, usunięty materiał lub wymagane logowanie. Nie powtarzaj bez końca tego samego wywołania. Nie eksportuj automatycznie sesji przeglądarki. Gdy potrzebne jest zalogowanie, skorzystaj z dostępu wyraźnie udostępnionego do tego zadania albo poproś o plik; nie obchodź DRM ani ograniczeń dostępu. Nieruchomą grafikę pobierz lub obejrzyj jako obraz — nie kieruj jej na siłę przez downloader wideo.

## Minimalna użyteczna analiza

Obejrzyj początek, demonstrację i zakończenie, następnie sprawdź wszystkie przejścia pomiędzy nimi. Zapisz:

| Czas źródła | Co widzimy i słyszymy | Funkcja | Co zachowujemy | Nasze wykonanie |
|---|---|---|---|---|
| Konkretny przedział | Kadr, działanie, ruch kamery, treść wypowiedzi | Zaciekawienie, dowód, wyjaśnienie lub decyzja | Ogólny mechanizm | Własna postać, produkt, zdanie i gest |

Wystarczy tyle wierszy, ile istotnych zmian. Zapisz pierwsze pojawienie się produktu, czy naprawdę demonstrowana jest zaleta i ile czasu pozostaje na zakończenie. „Ten film działa” jest hipotezą bez danych o wynikach; czas emisji, popularność i komentarze nie dowodzą rentowności.

Nie potrzebujesz pełnego zapisu cudzych słów do napisania nowego scenariusza. Streszczaj ich funkcję, odnotuj tempo i pauzy. Przy zleconej transkrypcji materiału użytkownika rozróżniaj odsłuchany cytat, streszczenie i słowo niepewne.

## Kiedy użyć klatek

Jeżeli dostępne są lokalne narzędzia, odczytaj metadane filmu. Rozpocznij od klatek na granicach ujęć i najważniejszych gestów; zagęść próbki wokół niejasnego ruchu. Pojedyncza klatka nie potwierdza kierunku ruchu. Detektor zmiany obrazu wskazuje kandydatów cięcia. Dokładność do klatki wymaga sprawdzenia sąsiednich klatek, a nie siatki co sekundę.

Zachowuj proporcje i oryginał pliku. Klatki oznaczaj czasem źródłowym. Powiększ etykietę lub ekran przed przepisaniem tekstu. Nie licz pustych pól siatki jako materiału. Arkusz kontaktowy pomaga agentowi w analizie nawet wtedy, gdy nie nadaje się jako wejście generatora.

## Dobór referencji do produkcji

Przy wyróżniającym się ruchu wybierz dodatkowe klatki jego kolejnych stanów i przygotuj je do dołączenia do generacji według [prowadzenia ruchu klatkami](ruch-i-klatki.md). Zapisz czasy źródłowe oraz docelowe. Sama analiza klatek bez ich wykorzystania jako wejść nie realizuje prośby o referencje ruchu.

Oddziel **dowody analizy** od **załączników generacyjnych**. Setka obejrzanych klatek nie oznacza setki wysłanych obrazów. Każdy załącznik ma jedną główną rolę: twarz, produkt, ubiór, przestrzeń, kompozycja lub ruch.

Źródłem wyglądu bohatera jest własny wybrany obraz. Źródłem geometrii produktu są materiały produktu. Referencja reklamy może wyznaczać rytm lub kamerę, ale nie może nadpisywać tych tożsamości. Przy sprzeczności usuń zbędny załącznik zamiast dopisywać kolejne zakazy.

Cały film dołączaj do generacji tylko wtedy, gdy jest potrzebny do wyraźnie zleconego transferu ruchu/edycji, użytkownik może go w tym celu wykorzystać i wybrany tryb go obsługuje. W pozostałych przypadkach twórz własne klatki sceny lub zapisuj ruch w promptach. Nie usuwaj oznaczeń pochodzenia z cudzego filmu, aby przedstawiać go jako własny.

Gdy link wymaga logowania lub nie udostępnia odtwarzalnego materiału, wskaż ten konkretny brak. Kontynuuj produkt i postać; adaptację opartą na referencji dokończ po uzyskaniu filmu. Własny koncept można przygotować od razu, jeśli użytkownik zgadza się na taki kierunek.
