# Sprawdzenie pakietu

Data: 13.09.2026.

## Wykonane próby

- Walidator struktury skilla: wynik poprawny. Sprawdzono nazwę, metadane i brak pozostałości szablonu.
- 19 testów pomocniczego walidatora planu: wszystkie zakończone powodzeniem. Polecenie: `python3 -m unittest discover -s tests -v` z katalogu pakietu.
- Przykład polskiej reklamy 30 s: trzy samodzielne prompty, trzy obrazy na klip, lokalne osie czasu i globalna kolejność montażu. Plan przechodzi walidację bez uwag o tempie mowy.
- Odczyt aktualnego katalogu i szczegółów Gemini Omni Flash 1.1 przez połączenie Higgsfield.
- Dwie rzeczywiste wyceny bez wysyłania generacji: dla 10 s i dla 30 s. Nie przesyłano mediów ani nie uruchamiano płatnych zadań.
- Po dodaniu pobierania referencji przez `yt-dlp` sprawdzono dostępność programu, użytych opcji i etapu `after_move` w lokalnym `--help`; walidacja struktury skilla ponownie przeszła. Nie wykonywano pobierania z serwisu, ponieważ ta aktualizacja dotyczyła instrukcji i nie zawierała konkretnego linku do filmu.

## Istotny wynik wyceny

Dla modelu `gemini_omni_flash_1_1`, trybu `text-to-video`, pionu 9:16 i 720p wycena 10 s wyniosła 30 kredytów. Przy żądaniu 30 s narzędzie także zwróciło wycenę 30 kredytów, ale z korektą `duration: requested=30, used=10`. Była to wycena klipu 10 s, nie reklamy 30 s. Informacja o korekcie została uwzględniona w instrukcjach wykonania.

To obserwacja z powyższej daty i tego połączenia, nie stały cennik. Wyceniano parametry bez obrazów; nie sprawdzono rzeczywistego przesłania siedmiu referencji. Katalog nie podał liczbowego limitu obrazów. Budżet siedmiu pozostaje jawnym ustawieniem workflow do sprawdzenia przy produkcji. Możliwości modelu opisuje także [Higgsfield](https://higgsfield.ai/gemini-omni-flash).

## Co obejmują testy kodu

Poprawny plan 3 × 10 s; siedem obrazów osobno dla każdego klipu; odrzucenie ósmego obrazu; odrzucenie 30 s w profilu do 10 s; dopuszczenie jednej generacji 30 s w odpowiednim profilu; podział 12 s na 6 + 6; minimum długości; zamknięta lista dozwolonych czasów; luki i nakładanie scen; mowa poza sceną; ucięcie mowy przez montaż; ostrzeżenie o przeładowaniu dialogu; uwzględnienie przenikań w sumie czasu; nieprawidłowe nakładanie pierwszego klipu; duplikat identyfikatora; błędne typy i wartości liczbowe; poprawne uruchomienie z pliku i błąd odczytu JSON.

## Próba workflow

[Przykład](skills/reklama-z-referencji/references/przyklad.md) przechodzi przez etapowy brief: najpierw produkt i kobieta, potem opis referencji oraz 30-sekundowy plan. Pokazuje rozdzielenie informacji z briefu od obserwacji, casting bez czekania na film, własną treść reklamy i dopasowanie do krótkich generacji. To przygotowany przez autora skilla przykład i przegląd decyzji, nie niezależny test skuteczności agenta.

## Granica sprawdzenia

Nie wykonano pełnej kampanii na prawdziwym produkcie i dostarczonym filmie. Nie wygenerowano portretu, klipów ani dźwięku. Nie potwierdzono jakości polskiej wymowy, synchronizacji ust, wierności etykiety ani ciągłości twarzy. Testy techniczne i wycena nie potwierdzają tych właściwości.

Do pełnej próby potrzebne są: obraz lub dostępny link produktu, wybór bohatera i film referencyjny. Następnie trzeba obejrzeć wygenerowaną postać, pierwszy reprezentatywny klip i gotowy montaż zgodnie z kontrolą jakości skilla.
