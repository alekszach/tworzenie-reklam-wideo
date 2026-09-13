# Tworzenie reklam wideo

Skill po polsku do tworzenia reklam z własnym produktem i bohaterem.

To **jeden skill z plikami pomocniczymi**. Wywołujesz tylko `tworzenie-reklam-wideo`; agent sam sięga po instrukcje promptowania, analizy i kontroli jakości, gdy są potrzebne. Pozostałe pliki nie są osobnymi skillami i nie wymagają osobnych komend.

**Produkt → postać → referencja → reklama.** Wysyłasz link lub zdjęcie produktu i wybierasz kobietę albo mężczyznę. Agent tworzy postać. Następnie wykorzystuje film referencyjny do napisania własnego scenariusza i zaplanowania ujęć. Po generacji sprawdza produkt, twarz, dłonie, mowę i montaż.

## Jak zacząć

### Instalacja z GitHub

Wklej do Codex:

> Zainstaluj skill z https://github.com/alekszach/tworzenie-reklam-wideo/tree/main/skills/tworzenie-reklam-wideo

Agent z obsługą instalacji skillów pobierze cały katalog wraz z plikami pomocniczymi. To jeden skill; nie instaluj każdego pliku osobno. Jeśli używasz innego środowiska, pobierz repozytorium i skopiuj folder `skills/tworzenie-reklam-wideo` do katalogu skillów tego środowiska.

### Pierwsza reklama

> Użyj $tworzenie-reklam-wideo. Produkt: [link lub załączone zdjęcie]. Bohaterka: kobieta około 30 lat. Reklama po polsku. Najpierw stwórz postać, potem prześlę film referencyjny.

Jeśli masz już komplet:

> Użyj $tworzenie-reklam-wideo. Oto produkt, wybrana postać i film referencyjny. Przygotuj reklamę 30 sekund w podobnym rytmie, z własnym tekstem. Na razie pokaż scenariusz i prompty.

Możesz podać mężczyznę, inny wiek dorosłej postaci, język filmu, własny wizerunek, długość lub format. Przyjęte wcześniej wybory pozostają w projekcie. Nie trzeba obsługiwać osobnych etapów technicznych.

Jeśli nie podasz języka reklamy, agent zapyta: „W jakim języku ma być reklama?”. Nie zakłada polskiego na podstawie rozmowy ani języka filmu referencyjnego. Wcześniejszy wybór w tej kampanii pozostaje ważny. Dotyczy to zarówno mowy do kamery, jak i osobnego lektora; możesz wybrać też inny język napisów. Film bez mowy i dodawanych tekstów nie wymaga wyboru języka.

Możesz również podać rozdzielczość filmu. Jeśli jej nie określisz, agent zapyta przed generacją i pokaże opcje dostępne dla wybranego modelu oraz dostępne różnice kosztu. Nie zakłada automatycznie 1080p. Możesz też polecić mu dobrać jakość do celu i budżetu.

Po otrzymaniu linku do filmu agent najpierw próbuje pobrać wskazany materiał przez `yt-dlp`, a następnie analizuje lokalny plik z dźwiękiem. Obsługuje także strony z osadzonym wideo. Linki do nieruchomych grafik traktuje jako obrazy. Przy niedostępnym materiale wyjaśnia konkretny problem i korzysta z dostępnej alternatywy lub prosi o plik.

Przy charakterystycznych ruchach agent wybiera dodatkowe klatki przed, w trakcie i po czynności oraz dołącza je jako referencje, szczególnie dla Seedance 2.5. Każda ma określoną rolę, kolejność i czas. W reklamach aplikacji sprawdza zarówno gest dłoni, jak i reakcję ekranu; w razie potrzeby wykorzystuje rzeczywiste nagranie aplikacji w montażu. Ujęcie wymagające działania nie przechodzi kontroli jako nieruchomy ekran z dłonią.

## Pakiet

Właściwy skill znajduje się w [skills/tworzenie-reklam-wideo](skills/tworzenie-reklam-wideo/SKILL.md). Skopiuj cały ten folder do swojego katalogu skillów, np. `~/.codex/skills/`, zachowując pliki `references`, `scripts` i `agents`. Uruchom nową rozmowę, aby środowisko mogło go wykryć. Możesz też wskazać agentowi bezpośrednio plik `SKILL.md`. Samo rozpakowanie archiwum nie podłącza narzędzi generacji.

Rdzeń nie wymaga konkretnego modelu wideo. Dla reklam z polską narracją preferuje Seedance 2.5 do obrazu i osobny polski głos z Higgsfield. Gemini Omni Flash 1.1 pozostaje opcją do krótkich klipów. Można przygotować prompty bez połączenia z generatorem. Faktyczne obrazy i filmy wymagają dostępnych narzędzi oraz odpowiednich środków. Limity są sprawdzane przy projekcie.

## Reklama z polskim lektorem

> Użyj $tworzenie-reklam-wideo. Oto produkt i film referencyjny. Nowa bohaterka ma tylko pokazywać produkt, bez mówienia. Użyj Seedance 2.5 do obrazu, wybierz naturalny kobiecy głos po polsku w Higgsfield, wygeneruj narrację i dodaj ją do gotowego filmu. Zachowaj możliwie blisko rytm i ujęcia referencji, z własnym tekstem.

Dla mężczyzny skill dobiera głos męski, chyba że wskażesz inaczej. Agent mierzy gotową narrację, dopasowuje obraz i oddaje film z już dołączonym lektorem. Narrator może mówić także podczas zbliżeń produktu i demonstracji, gdy aktor nie mówi. Gdy połączenie wymaga selektora głosu, wybierasz go raz, a agent kontynuuje z zapamiętaną parą. Szczegóły i przykład: [polska narracja](skills/tworzenie-reklam-wideo/references/polska-narracja.md).

Przy budżecie 7 obrazów skill wybiera najważniejsze wzorce postaci i produktu, a resztę ruchu opisuje sekundowo. Przy modelu obsługującym dłuższy film można użyć jednej generacji. Nie ma obowiązkowego rozbijania na krótkie klipy ani stałego przypisania języka do modelu.

W pakiecie znajduje się [przykład po polsku](skills/tworzenie-reklam-wideo/references/przyklad.md), kontrola techniczna planu oraz [raport przeprowadzonych prób](SPRAWDZENIE.md). Pliki kampanii, prywatne media i dane konta trzymaj poza tym pakietem.

## Zakres sprawdzenia

Pakiet obejmuje testy planowania i sprawdzenie parametrów dostępnego połączenia. Nie jest deklaracją, że przeprowadzono pełną płatną produkcję reklamy. Jakość wygenerowanego obrazu, polskiej wymowy i ciągłości wymaga kontroli na rzeczywistym produkcie oraz filmie referencyjnym.
