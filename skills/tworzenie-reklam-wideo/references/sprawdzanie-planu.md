# Pomocnicza kontrola planu

Agent może uruchomić `python3 scripts/sprawdz_plan.py /sciezka/do/planu.json` z katalogu skilla. Skrypt korzysta wyłącznie z biblioteki standardowej Pythona. Nie łączy się z internetem, nie przesyła plików, nie generuje mediów i nie zużywa kredytów.

Używaj go dla planów wieloklipowych lub ograniczeń wejść. Użytkownik nie musi wypełniać JSON ani uruchamiać polecenia. [Przykładowy plan](przyklad-plan.json) jest kompletnym plikiem do uruchomienia.

Pola:

- `czas_docelowy_s`: czas całego montażu.
- `profil`: `min_s`, `max_s`, `max_obrazow`; opcjonalnie `dozwolone_s` dla modelu ze stałymi długościami oraz `slowa_na_s` do ostrzeżeń o tempie.
- `klipy`: lista z unikalnym `id`, czasem generacji `czas_s`, listą wszystkich obrazów `obrazy` i osią `sceny`. Uwzględnij także obrazy początku/końca. Role i identyfikatory przesyłania sprawdzaj osobno.
- Opcjonalne `uzyj_od_s` i `uzyj_do_s`: zakres montażu w czasie lokalnym klipu. Domyślnie cały klip.
- Opcjonalne `nakladanie_s`: ile bieżący klip nakłada się na poprzedni. Dla twardego cięcia zero.
- `sceny`: `od_s`, `do_s`, `akcja`, opcjonalny `tekst`. Dla mowy wymagane `mowa_od_s` i `mowa_do_s` w czasie lokalnym klipu.

Skrypt sprawdza sumę montażu z przycięciami i nakładaniem, dozwolone długości, limit obrazów w każdym klipie, pełne pokrycie osi czasu, okna wypowiedzi i ich ucięcie przez montaż. Przekroczenie orientacyjnego tempa daje uwagę, nie automatyczne odrzucenie mowy. Kod wyjścia: 0 — plan technicznie spójny, 1 — błędy planu, 2 — problem odczytu.

Limit jest danymi wejściowymi, nie wbudowaną wiedzą o modelu. Wpisz go dopiero po sprawdzeniu katalogu albo oznacz jako założenie. Walidator nie potwierdza istnienia plików, zgodności z API, prawdziwości twierdzeń, sensu gestów, jakości polszczyzny ani wyglądu produktu. Poprawny JSON nie jest zgodą na wydatki ani dowodem jakości filmu.
