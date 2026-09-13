#!/usr/bin/env python3
"""Sprawdza czas, referencje i okna mowy. Nie wywołuje generatorów."""

import argparse
import json
import math
import re
from pathlib import Path


def liczba(wartosc):
    return isinstance(wartosc, (int, float)) and not isinstance(wartosc, bool) and math.isfinite(wartosc)


def sprawdz(plan):
    bledy, uwagi = [], []

    def wymagaj(warunek, opis):
        if not warunek:
            bledy.append(opis)
        return warunek

    if not wymagaj(isinstance(plan, dict), 'Plan musi być obiektem JSON.'):
        return bledy, uwagi
    profil = plan.get('profil', {})
    klipy = plan.get('klipy', [])
    cel = plan.get('czas_docelowy_s')
    if not wymagaj(isinstance(profil, dict), 'Brak poprawnego profilu.'):
        return bledy, uwagi
    if not wymagaj(isinstance(klipy, list) and bool(klipy), 'Plan wymaga przynajmniej jednego klipu.'):
        return bledy, uwagi
    if not wymagaj(liczba(cel) and cel > 0, 'Czas docelowy musi być dodatni.'):
        return bledy, uwagi
    minimum, maksimum = profil.get('min_s'), profil.get('max_s')
    limit = profil.get('max_obrazow')
    if not wymagaj(liczba(minimum) and liczba(maksimum) and 0 < minimum <= maksimum,
                  'Profil wymaga dodatnich min_s i max_s.'):
        return bledy, uwagi
    if not wymagaj(type(limit) is int and limit >= 0, 'max_obrazow musi być nieujemną liczbą całkowitą.'):
        return bledy, uwagi
    czasy = profil.get('dozwolone_s')
    if czasy is not None and not wymagaj(isinstance(czasy, list) and bool(czasy)
                                       and all(liczba(x) and minimum <= x <= maksimum for x in czasy),
                                       'dozwolone_s musi zawierać czasy w granicach profilu.'):
        return bledy, uwagi
    tempo = profil.get('slowa_na_s', 2)
    if not wymagaj(liczba(tempo) and tempo > 0, 'slowa_na_s musi być dodatnie.'):
        return bledy, uwagi
    suma, poprzedni_czas = 0.0, 0.0
    identyfikatory = set()
    for numer, klip in enumerate(klipy, 1):
        etykieta = f'Klip {numer}'
        if not wymagaj(isinstance(klip, dict), f'{etykieta}: wymagany obiekt.'):
            continue
        ident = klip.get('id')
        if wymagaj(isinstance(ident, str) and bool(ident.strip()), f'{etykieta}: brak id.'):
            wymagaj(ident not in identyfikatory, f'{etykieta}: powtórzone id {ident}.')
            identyfikatory.add(ident)
        czas = klip.get('czas_s')
        if not wymagaj(liczba(czas) and czas > 0, f'{etykieta}: niepoprawny czas_s.'):
            continue
        wymagaj(minimum <= czas <= maksimum, f'{etykieta}: czas {czas} poza zakresem {minimum}–{maksimum} s.')
        if czasy is not None:
            wymagaj(czas in czasy, f'{etykieta}: czas {czas} nie należy do dozwolone_s.')
        poczatek, koniec = klip.get('uzyj_od_s', 0), klip.get('uzyj_do_s', czas)
        if not wymagaj(liczba(poczatek) and liczba(koniec) and 0 <= poczatek < koniec <= czas,
                      f'{etykieta}: niepoprawny zakres montażu.'):
            continue
        dlugosc = koniec - poczatek
        nakladka = klip.get('nakladanie_s', 0)
        if not wymagaj(liczba(nakladka) and 0 <= nakladka < dlugosc
                      and (nakladka == 0 if numer == 1 else nakladka < poprzedni_czas),
                      f'{etykieta}: niepoprawne nakładanie z poprzednim klipem.'):
            nakladka = 0
        suma += dlugosc - nakladka
        poprzedni_czas = dlugosc
        obrazy = klip.get('obrazy', [])
        if wymagaj(isinstance(obrazy, list) and all(isinstance(x, str) and x.strip() for x in obrazy),
                   f'{etykieta}: obrazy muszą być listą identyfikatorów.'):
            wymagaj(len(obrazy) <= limit, f'{etykieta}: {len(obrazy)} obrazów przekracza limit {limit}.')
            if len(set(obrazy)) != len(obrazy):
                uwagi.append(f'{etykieta}: powtórzone obrazy też zajmują pozycje wejściowe; sprawdź role.')
        sceny = klip.get('sceny', [])
        if not wymagaj(isinstance(sceny, list) and bool(sceny), f'{etykieta}: brak osi scen.'):
            continue
        granica = 0
        for indeks, scena in enumerate(sceny, 1):
            opis = f'{etykieta}, scena {indeks}'
            if not wymagaj(isinstance(scena, dict), f'{opis}: wymagany obiekt.'):
                continue
            od, do = scena.get('od_s'), scena.get('do_s')
            if not wymagaj(liczba(od) and liczba(do) and 0 <= od < do <= czas,
                          f'{opis}: niepoprawny przedział.'):
                continue
            wymagaj(abs(od - granica) < 0.001, f'{opis}: luka lub nakładanie na osi scen.')
            granica = do
            wymagaj(isinstance(scena.get('akcja'), str) and bool(scena['akcja'].strip()),
                    f'{opis}: brak działania.')
            tekst = scena.get('tekst', '')
            if not wymagaj(isinstance(tekst, str), f'{opis}: tekst musi być napisem.'):
                continue
            if tekst.strip():
                mowa_od, mowa_do = scena.get('mowa_od_s'), scena.get('mowa_do_s')
                if wymagaj(liczba(mowa_od) and liczba(mowa_do) and od <= mowa_od < mowa_do <= do,
                           f'{opis}: dialog wymaga okna mowy wewnątrz sceny.'):
                    wymagaj(poczatek <= mowa_od and mowa_do <= koniec,
                            f'{opis}: montaż ucina wypowiedź.')
                    slowa = len(re.findall(r"\w+(?:[-’']\w+)*", tekst, re.UNICODE))
                    if slowa / (mowa_do - mowa_od) > tempo:
                        uwagi.append(f'{opis}: {slowa} słów w {mowa_do - mowa_od:g} s; skróć tekst lub sprawdź odsłuchem.')
        wymagaj(abs(granica - czas) < 0.001, f'{etykieta}: oś scen nie obejmuje całego klipu.')
    wymagaj(abs(suma - cel) <= 0.05, f'Montaż daje {suma:g} s zamiast {cel:g} s.')
    return bledy, uwagi


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('plan', type=Path, help='Plik planu JSON')
    args = parser.parse_args()
    try:
        plan = json.loads(args.plan.read_text(encoding='utf-8'))
        bledy, uwagi = sprawdz(plan)
    except (OSError, ValueError) as exc:
        print(f'Nie można odczytać planu: {exc}')
        return 2
    for blad in bledy:
        print(f'BŁĄD: {blad}')
    for uwaga in uwagi:
        print(f'UWAGA: {uwaga}')
    if not bledy:
        print('Plan spójny technicznie. Jakość obrazu, wymowa i obsługa wejść wymagają osobnej kontroli.')
    return 1 if bledy else 0


if __name__ == '__main__':
    raise SystemExit(main())
