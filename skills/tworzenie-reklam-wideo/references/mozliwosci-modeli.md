# Dopasowanie do możliwości

Workflow nie zależy od nazwy modelu ani od jednej platformy. Jeżeli użytkownik wskazuje Higgsfield, korzystaj z jego dostępnego połączenia. Bez narzędzi generacyjnych nadal można wykonać analizę, casting tekstowy i komplet promptów; obrazu ani filmu nie oznaczaj wtedy jako wygenerowanych.

## Profil przed produkcją

Ustal z bieżącego katalogu i schematu wywołania:

- dokładny identyfikator modelu i wybrany tryb;
- dozwolone czasy, proporcje i rozdzielczości;
- limit obrazów oraz osobne i łączne limity obrazów, wideo i dźwięku;
- czy klatki początku/końca wliczają się do limitu i czy można je łączyć z referencjami;
- dostępność mowy, utrzymania głosu, edycji i przedłużania;
- wycenę i ewentualne zmiany parametrów w odpowiedzi.

Nie przenoś limitu edycji istniejącego filmu na długość nowej generacji. Opis „multimodalny” nie potwierdza wszystkich kombinacji wejść. Brak pola limitu oznacza „nieustalony”, nie „bez limitu”. Użyj weryfikacji bez generacji albo oznacz założenie i dostosuj do odpowiedzi narzędzia.

W Higgsfield odpowiednie operacje to odkrycie modeli, odczyt szczegółów, oszacowanie kosztu, przesłanie mediów, generacja i odczyt wyniku. Odkrywaj aktualne narzędzia; prefiksy zależą od środowiska. Czytaj role z aktualnego schematu wywołania: nazwa pola katalogu nie zawsze jest literalną rolą załącznika. Nie dopisuj nieobsługiwanych parametrów na podstawie pamięci.

Estymacja może normalizować parametry. Odpowiedź dla 30 s może wyceniać tylko 10 s. Odczytaj faktycznie użyte wartości, popraw plan i oszacuj całą partię ponownie. Wycenę bez załączników nazywaj wyceną parametrów, nie pełną walidacją wejść. Nie używaj generacji jako testu limitu.

## Dwa sposoby prowadzenia sceny

**Dłuższy ciąg, więcej referencji.** Gdy model obsługuje długość reklamy, wyślij jeden spójny prompt z czasami. Każda wybrana klatka pokazuje ważny stan sceny, a tekst opisuje przejście między stanami. Obraz sam nie narzuca kolejności. Nie rozdzielaj na wiele generacji wyłącznie z przyzwyczajenia do starszych modeli. Złożona scena może jednak zyskać na kilku prostych klipach.

**Krótkie klipy, mało referencji.** Podziel wypowiedzi i działania na zamknięte części w dozwolonych czasach. Dla 30 s i limitu 10 s możliwy jest plan 3 × 10 s. Dla 12 s i minimum 3 s wybierz np. 6 + 6, nie 10 + 2. Uwzględnij przycięcia i nakładanie przejść w długości końcowej. Każdy klip ma własny komplet referencji, a nie wspólny limit całej kampanii, o ile narzędzie nie stanowi inaczej.

## Opcjonalny profil: Gemini Omni Flash 1.1

Stan sprawdzony 13.09.2026 w katalogu Higgsfield: identyfikator `gemini_omni_flash_1_1`, nowa generacja 3–10 s, tryby tekstowy, obrazowy, referencyjny i edycja; role obejmują obrazy referencyjne, początek/koniec i wideo. Dostępność połączeń ról trzeba sprawdzić dla konkretnego trybu. Katalog opisuje natywny dźwięk, ale nie stanowi testu jakości polskiej wymowy.

To opcja do krótkich reklam po polsku, jeśli odpowiada preferencji użytkownika. Nie przypisuj innym językom sztywnego generatora ani nie obiecuj przewagi jakościowej bez porównania własnych wyników. [Strona modelu w Higgsfield](https://higgsfield.ai/gemini-omni-flash) i [dokumentacja producenta](https://ai.google.dev/gemini-api/docs/omni) opisują także pracę z referencjami; możliwości interfejsu producenta nie muszą być identyczne z połączeniem w Higgsfield.

**Budżet 7 zdjęć** jest zachowanym ustawieniem tego workflow, podanym przez użytkownika. Odczyt katalogu z powyższej daty nie zwrócił liczbowego maksimum zdjęć, więc nie traktuj go jako niezależnie potwierdzonego, uniwersalnego limitu API. Przed wysłaniem sprawdź wybrane wejścia; przy niższym limicie zmniejsz pakiet.

Praktyczna kolejność wykorzystania maksymalnie siedmiu miejsc:

| Priorytet | Obraz | Po co |
|---|---|---|
| 1 | Wybrany portret | Tożsamość |
| 2 | Produkt od przodu | Kształt i oznaczenia |
| 3 | Produkt z innej strony, jeśli potrzebny | Detal demonstracji |
| 4 | Własny bohater w scenie, jeśli potrzebny | Ubiór, skala i światło |
| 5 | Własna klatka początkowa albo połączenie | Ciągłość |
| 6–7 | Wybrane kadry kompozycji lub ważny detal | Konkretne trudne zdarzenie |

Nie wypełniaj wolnych miejsc na siłę. Często portret, produkt i własna scena wystarczą. Konserwatywnie licz wszystkie wysyłane obrazy, w tym początek/koniec, do wspólnego budżetu siedmiu, dopóki aktualny schemat nie potwierdzi innej zasady. Klatki referencyjne są możliwe, lecz nie powinny wypierać postaci i produktu. Kolaż nie zastępuje precyzyjnych referencji i może zostać wyrenderowany jako podzielony ekran.

## Profil obrazu do polskiego lektora

Przy polskim lektorze preferuj [Seedance 2.5 dla obrazu i osobną syntezę mowy w Higgsfield](polska-narracja.md). Polski dźwięk nie wymaga wtedy polskiej mowy w generatorze wideo. Katalog Seedance 2.5 sprawdzony 13.09.2026 udostępnia generację 4–30 s, tryb `omni_reference` i przełącznik `generate_audio`; ustaw go na `false` i dodaj lektora w montażu. Ponownie sprawdzaj parametry przy wykonaniu. Gemini pozostaje opcją dla krótszych klipów, w tym mowy w kadrze; nie traktuj ograniczeń jednego modelu jako ogólnego zakazu polskiego języka.

## Elastyczność agenta

Współczesny agent może sam obejrzeć materiały, zestawić dowody, napisać plan, wywołać narzędzia i sprawdzić wynik. Nie wymagaj osobnego agenta do każdej roli ani przepisywania dokumentów między etapami. Równoległe odczyty są przydatne; generowanie postaci, przyjęcie jej wzorca i generowanie z nią filmu pozostają zależnymi krokami. Nie wymuszaj zmiany modelu asystenta na podstawie nazwy handlowej.
