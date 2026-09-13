# Polski lektor nad obrazem

Uruchom ten tryb, gdy użytkownik wybrał język polski oraz prosi o narrację, lektora, voiceover lub „narration voice”, albo gdy przy wybranym polskim analizowana referencja opowiada w ten sposób. Samo zamówienie narracji nie oznacza polskiego: przy brakującym języku najpierw zapytaj o niego zgodnie z głównym skillem. Dla innego języka stosuj ogólne zasady narracji z [promptowania](promptowanie.md); nie tłumacz jej automatycznie na polski. Postać wykonuje czynności i prezentuje produkt; głos słyszymy spoza kadru. Nie wymagaj synchronizacji ust osoby, która nie mówi. Przy wyraźnym zamówieniu mowy do kamery zachowaj ten format.

## 1. Adaptacja referencji

Pobierz film przez `yt-dlp` i obejrzyj go zgodnie z instrukcją analizy. Zachowaj możliwie blisko długość, kolejność zdarzeń, kadrowanie, ruch kamery, moment demonstracji i rytm cięć. Wprowadź własnego wybranego aktora, nowy produkt i własny polski tekst dopasowany do tego produktu. Nie przenoś cudzych obietnic, głosu ani tożsamości. Nie dopowiadaj niewidocznych działań i nie obiecuj identyczności każdej klatki.

Seedance 2.5 jest preferowanym modelem obrazu w tym trybie. Użyj własnych wzorców postaci i produktu oraz opisu czasowego. Wybrane klatki kompozycji lub film mogą sterować wykonaniem tylko wtedy, gdy ich użycie jest dozwolone i potrzebne; jasno przypisz im rytm/ruch, a własnym obrazom tożsamość. Nie nadpisuj aktora twarzą z referencyjnego filmu. Jeśli użytkownik zamawia bezpośrednią edycję lub dokładny transfer ruchu, sprawdź aktualne zasady routingu narzędzia; nie uruchamiaj po cichu innego modelu.

## 2. Wybór polskiego głosu ElevenLabs

Zastosuj [dobór silnika głosu](dobor-glosu.md). Polski lektor korzysta z ElevenLabs; Higgsfield może być połączeniem do tego silnika.

Sam dobierz jeden naturalny, wyraźny głos z dostępnego katalogu głosów zgodnych z ElevenLabs: kobiecy do bohaterki, męski do bohatera, chyba że użytkownik wskazuje inaczej. Dopasuj do postaci przybliżony wiek brzmienia, energię i sposób mówienia. W reklamie codziennej wybierz swobodny, ciepły ton bez przesadnego radiowego patosu. Nie klonuj głosu osoby z referencji.

Sprawdź aktualne narzędzia mowy i próbkę głosu, jeśli jest dostępna. Zapisz prawdziwe `voice_id` i `voice_type` z katalogu lub wcześniejszego wyboru; nie wymyślaj nazw ani identyfikatorów. Sama etykieta płci głosu nie potwierdza dobrej polskiej wymowy. Sprawdź polskie słowa, nazwę marki, liczby i końcówki w odsłuchu wygenerowanego materiału.

Gdy interfejs pozwala agentowi wybrać pozycję z katalogu, wybierz ją sam bez ankiety. Jeśli aktualny interfejs Higgsfield wymaga wyboru użytkownika w selektorze, zastosuj ten mechanizm: poleć pasujące brzmienie, pokaż selektor i po otrzymaniu pary głosu kontynuuj. Nie obiecuj automatycznego wyboru, którego narzędzie nie udostępnia. W obecnym połączeniu brak pary głosu kieruje do `list_voices` jako jedynego wywołania w tej turze; wybór wraca w następnej wiadomości. Raz wybraną parę wykorzystuj dalej w kampanii.

## 3. Wygeneruj i zmierz narrację

Przygotuj osobno tekst lektora i instrukcje obrazu. Do pola tekstu syntezy mowy przekazuj wyłącznie słowa do wypowiedzenia. Nie dodawaj tam znaczników czasu, opisów ujęć ani poleceń typu „kobiecym głosem”, które mogłyby zostać przeczytane. Styl ustaw przez udostępnione parametry lub odpowiednio wybrany głos.

Wywołaj generowanie mowy silnikiem ElevenLabs z rzeczywistym zgodnym głosem, przez dostępny wariant Higgsfield lub połączenie ElevenLabs zgodnie z instrukcją doboru. Nie używaj domyślnego silnika Higgsfield zamiast ElevenLabs. Sprawdź obsługę polskiego i wymowę; język generatora obrazu nie ogranicza języka osobnej ścieżki audio.

Generuj jedną spójną ścieżkę dla krótkiej reklamy, aby utrzymać barwę głosu przez cięcia. Zaplanuj naturalne przerwy przy demonstracji. Gdy konieczne jest dopasowanie do sztywnych okien, można wykonać osobne pełne zdania tą samą parą głosu. Zachowaj limity kosztów i ponownych prób z głównego skilla. W trybie „tylko prompty” przygotuj tekst i dobór głosu bez uruchamiania generacji.

Zapisz zadanie i wynik, odsłuchaj, zmierz długość oraz wyznacz rzeczywiste czasy zdań. Na tej podstawie dopasuj ujęcia. Jeżeli lektor nie mieści się w docelowej długości referencji, skróć tekst i popraw nagranie; nie urywaj końcówki ani nie przyspieszaj sztucznie głosu. Przy trudnej wymowie użyj zapisu fonetycznego w tekście do syntezy, zachowując poprawną nazwę w dokumentacji i napisach. Gotowy głos jest źródłem czasu narracji, nie orientacyjny licznik słów.

## 4. Obraz bez mówiących ust

Sprawdź katalog Seedance 2.5, tryb przyjmujący potrzebne referencje i faktyczne limity. Dla nowej sceny z własnymi wzorcami używaj trybu referencyjnego, nie edycji źródła z założenia. W bieżącym katalogu Higgsfield identyfikator to `seedance_2_5`, tryb `omni_reference`, generacja 4–30 s. Przed wykonaniem odczytaj te wartości ponownie.

Ustaw `generate_audio: false`, gdy obsługiwane, i napisz w promptach: „Postać nie mówi, nie wykonuje ruchów ust imitujących mowę. Wykonuje tylko opisane czynności. Polski lektor zostanie dodany osobno podczas montażu”. Nie wklejaj tekstu lektora jako kwestii aktora do promptu wideo.

Wygenerowaną narrację można opcjonalnie przekazać jako referencję rytmu, jeśli dany tryb to obsługuje. Nie oznacza to, że model zachowa oryginalny plik głosu. W finalnym montażu zawsze użyj wybranej gotowej ścieżki narracji. Nie każ generatorowi tworzyć jej ponownie. Jedna generacja 30 s może wystarczyć; dłuższe materiały dziel na ujęcia przy zachowaniu jednej osi narracji.

## 5. Dodaj głos do gotowego filmu

Po sprawdzeniu obrazu zmontuj klipy i dołącz gotowy plik lektora jako ścieżkę audio, używając dostępnego montażu lub `ffmpeg`. To obowiązkowy krok zamówienia gotowego filmu; samo oddanie osobno MP4 i WAV nie jest ukończoną reklamą z narracją. Narzędzie zamiany istniejącego głosu nie służy do dodania lektora do niemego filmu.

Zachowaj obraz, gdy nie wymaga ponownego kodowania. Usuń przypadkową mowę z wygenerowanego wideo. Dźwięki produktu i muzykę pozostaw tylko, jeśli są dostępne, pasują do sceny i nie dublują narracji; ścisz je pod głosem. Nie przenoś automatycznie muzyki ani głosu z cudzej reklamy. Synteza mowy nie zastępuje generatora muzyki lub efektów.

Uwzględnij zaplanowane opóźnienie początku lektora i pauzy. Uzupełnij ciszą krótszą ścieżkę do długości montażu. Nie używaj bez sprawdzenia opcji skracającej wynik do krótszego strumienia: może usunąć końcowy kadr albo ostatnie słowo. Po połączeniu odsłuchaj cały film, sprawdź zgodność słów z pokazywanym działaniem, długość i brak ruchów ust sugerujących mowę. Zwróć odtwarzalny film z już dołączoną polską narracją oraz zachowaj osobny plik lektora do korekt.

## Przykład: ten sam pomysł, osobny lektor

Fikcyjny kubek PORANEK, bohaterka, 20 s. To przykład promptów, nie wykonana generacja. Potwierdzoną funkcją briefu jest przycisk otwierania.

**Tekst syntezy:** „Spójrz na kubek Poranek. Przycisk na pokrywce pozwala go otworzyć jednym naciśnięciem. Zobacz, jak działa. Sprawdź szczegóły na stronie”.

**Dobór:** naturalny kobiecy głos zgodny z ElevenLabs, spokojna polska wymowa. Dla męskiego aktora ten sam tekst z wybranym głosem męskim. Dokładne identyfikatory pobierz przy realizacji.

**Plan obrazu:** 0–4 s bohaterka unosi kubek; 4–9 s zbliżenie na przycisk; 9–15 s naciśnięcie i otwarcie, z miejscem na przerwę w narracji; 15–20 s produkt na blacie i spokojne zakończenie. To czasy robocze do dopasowania po odsłuchu.

**Prompt obrazu:** „20 s, 9:16. Własna bohaterka z referencji postaci, oliwkowa koszula, jasna kuchnia. Kubek i pokrywka dokładnie według wzorców produktu. Zachowaj powyższą oś czynności, realistyczny chwyt i działanie przycisku. Bohaterka nie mówi i nie imituje mowy ustami. Bez generowanej ścieżki audio i napisów; osobny polski lektor zostanie dodany w montażu”.

Walidator planu klipów sprawdza obraz i mowę przypisaną do pojedynczych scen. Narrację przechodzącą przez cięcia zapisuj osobno na globalnej osi; jej rzeczywiste dopasowanie potwierdź odsłuchem montażu, nie wynikiem walidatora.
