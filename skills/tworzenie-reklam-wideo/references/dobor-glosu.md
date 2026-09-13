# Dobór silnika głosu

Najpierw ustal język filmu według głównego skilla. Dostawca głosu i model obrazu są osobnymi decyzjami. Jawne zamówienie użytkownika ma pierwszeństwo przed poniższym doborem.

| Potrzeba | Wykonanie |
|---|---|
| Angielski, bez specjalnych wymagań głosowych | Wbudowany głos Higgsfield: natywna mowa wideo dla mowy do kamery albo wbudowana synteza mowy dla osobnego lektora |
| Polski | ElevenLabs, niezależnie od generatora obrazu |
| Bardziej charakterystyczny lub specjalnie dobrany głos, także po angielsku | ElevenLabs; dobierz barwę, akcent i ekspresję do briefu |
| Inny język | Sprawdź obsługę wybranego języka; przy specjalnych wymaganiach głosowych użyj ElevenLabs |

W Higgsfield jawnie wybierz język, jeżeli aktualny tryb ma taki parametr lub selektor. Jeśli go nie udostępnia, użyj tekstu w docelowym języku, właściwego głosu i obsługiwanych instrukcji; nie wymyślaj pola `language`. W natywnym audio wideo określ dokładny dialog i język mowy. W polu tekstu TTS umieszczaj tylko wypowiadane słowa, bez poleceń, które mogłyby zostać odczytane.

## ElevenLabs przez dostępne połączenie

Użyj silnika ElevenLabs przez Higgsfield, jeśli jest dostępny; osobne połączenie ElevenLabs nie jest wtedy wymagane. W schemacie sprawdzonym 13.09.2026 `generate_audio` przyjmuje wewnątrz `params`: `model: "text2speech_v2"`, `variant: "elevenlabs"`, `prompt` oraz prawdziwe `voice_id` i `voice_type`. Przed produkcją ponownie sprawdź schemat i zgodność wybranego głosu z silnikiem. Nie pozostawiaj domyślnego `seed_audio` przy polskim lub zamówionym charakterystycznym głosie i nie opisuj go jako ElevenLabs.

Wbudowana synteza Higgsfield może korzystać z aktualnego domyślnego modelu mowy; obecnie narzędzie wskazuje `seed_audio`. Identyfikator głosu pobierz z właściwego katalogu. Przy wymaganym selektorze zastosuj aktualną procedurę narzędzia i zapamiętaj wybór. Nie zakładaj, że głos z jednego silnika będzie zgodny z innym.

Jeśli wariant ElevenLabs jest niedostępny, użyj dostępnego i autoryzowanego połączenia ElevenLabs. Gdy żadnego nie ma, przygotuj tekst i obraz, zgłoś brak potrzebnego połączenia; nie przełączaj po cichu na inny silnik. Nie zapisuj kluczy API w plikach skilla. Charakterystyczny głos oznacza dobór brzmienia, nie automatyczne klonowanie osoby z referencji.

## Zachowaj sposób mówienia

Wybór ElevenLabs nie zmienia automatycznie wypowiedzi do kamery w lektora. Dla mowy w kadrze wygeneruj docelowe audio, a następnie użyj obsługiwanej generacji sterowanej audio lub synchronizacji ust i sprawdź wynik. Samo podłożenie nowego głosu pod inne ruchy ust nie kończy zadania. Jeśli brak odpowiedniego narzędzia, wyjaśnij ograniczenie i ustal zmianę formatu zamiast jej zakładać.

Dla narracji spoza kadru osoba tylko wykonuje czynności; zmierz i dołącz gotowy głos w montażu. Szczegółowy przykład polskiego lektora: [polska narracja](polska-narracja.md). Przy charakterystycznym głosie w innym języku stosuj ten sam pomiar i montaż, zachowując wybrany język. Sprawdź wymowę, emocję, tempo, zgodność głosu między klipami oraz obecność właściwego audio w finalnym pliku. Żaden wybór silnika sam nie potwierdza jakości nagrania.
