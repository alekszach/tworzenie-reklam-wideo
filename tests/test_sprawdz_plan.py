"""Próby ograniczeń planowania. Bez sieci i bez generowania mediów."""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'tworzenie-reklam-wideo'
SCRIPT = SKILL / 'scripts' / 'sprawdz_plan.py'
spec = importlib.util.spec_from_file_location('sprawdz_plan', SCRIPT)
modul = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modul)
WZOR = json.loads((SKILL / 'references' / 'przyklad-plan.json').read_text())


class PlanTest(unittest.TestCase):
    def setUp(self):
        self.plan = copy.deepcopy(WZOR)

    def bledny(self):
        self.assertTrue(modul.sprawdz(self.plan)[0])

    def test_trzy_klipy_po_polsku(self):
        self.assertEqual(modul.sprawdz(self.plan), ([], []))

    def test_limit_liczony_osobno_dla_klipu(self):
        for k in self.plan['klipy']:
            k['obrazy'] = [f'obraz-{i}' for i in range(7)]
        self.assertEqual(modul.sprawdz(self.plan), ([], []))

    def test_osmy_obraz_odrzucony(self):
        self.plan['klipy'][0]['obrazy'] = [str(i) for i in range(8)]
        self.bledny()

    def test_30_sekund_nie_miesci_sie_w_10(self):
        self.plan['klipy'] = [{'id':'dlugi','czas_s':30,'obrazy':['postac','produkt'],
                               'sceny':[{'od_s':0,'do_s':30,'akcja':'Własna scena.'}]}]
        self.bledny()

    def test_dlugi_model_nie_wymusza_podzialu(self):
        self.plan['profil']['max_s'] = 30
        self.plan['klipy'] = [{'id':'dlugi','czas_s':30,'obrazy':['postac','produkt'],
                               'sceny':[{'od_s':0,'do_s':30,'akcja':'Własna scena.'}]}]
        self.assertEqual(modul.sprawdz(self.plan), ([], []))

    def test_12_sekund_jako_6_plus_6(self):
        self.plan['czas_docelowy_s'] = 12
        self.plan['klipy'] = [{'id':str(i),'czas_s':6,'obrazy':[],
                               'sceny':[{'od_s':0,'do_s':6,'akcja':'Prosta demonstracja.'}]} for i in range(2)]
        self.assertEqual(modul.sprawdz(self.plan), ([], []))

    def test_2_sekundy_ponizej_minimum(self):
        self.plan['klipy'][0]['czas_s'] = 2
        self.bledny()

    def test_czas_spoza_listy_stalych_dlugosci(self):
        self.plan['profil'].update(min_s=4,max_s=12,dozwolone_s=[4,8,12])
        self.bledny()

    def test_luka_w_osi(self):
        self.plan['klipy'][0]['sceny'][1]['od_s'] = 3.1
        self.bledny()

    def test_nakladajace_sie_sceny(self):
        self.plan['klipy'][0]['sceny'][1]['od_s'] = 2.9
        self.bledny()

    def test_mowa_poza_scena(self):
        self.plan['klipy'][0]['sceny'][0]['mowa_do_s'] = 3.5
        self.bledny()

    def test_montaz_ucina_slowo(self):
        self.plan['klipy'][0]['uzyj_od_s'] = 1
        self.plan['czas_docelowy_s'] = 29
        self.bledny()

    def test_przeladowany_dialog_daje_uwage(self):
        self.plan['klipy'][0]['sceny'][0]['tekst'] = 'Długie zdanie ' * 20
        bledy, uwagi = modul.sprawdz(self.plan)
        self.assertFalse(bledy)
        self.assertTrue(uwagi)

    def test_nakladanie_skraca_montaz(self):
        for k in self.plan['klipy'][1:]:
            k['nakladanie_s'] = 1
        self.bledny()
        self.plan['czas_docelowy_s'] = 28
        self.assertFalse(modul.sprawdz(self.plan)[0])

    def test_pierwszy_klip_nie_ma_nakladania(self):
        self.plan['klipy'][0]['nakladanie_s'] = 1
        self.bledny()

    def test_powtorzone_id(self):
        self.plan['klipy'][1]['id'] = self.plan['klipy'][0]['id']
        self.bledny()

    def test_nieprawidlowe_dane_bez_awarii(self):
        for p in [None, [], {}, {'profil':None}, {'profil':{},'klipy':[None],'czas_docelowy_s':30}]:
            with self.subTest(plan=p):
                self.assertTrue(modul.sprawdz(p)[0])
        for wartosc in [float('nan'), float('inf'), True, '30', -1]:
            self.plan['czas_docelowy_s'] = wartosc
            with self.subTest(wartosc=wartosc):
                self.bledny()

    def test_cli_poprawny_plan(self):
        result = subprocess.run([sys.executable,str(SCRIPT),str(SKILL/'references'/'przyklad-plan.json')],capture_output=True)
        self.assertEqual(result.returncode,0,result.stdout.decode())

    def test_cli_blad_odczytu(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/'plan.json'
            p.write_text('{')
            result = subprocess.run([sys.executable,str(SCRIPT),str(p)],capture_output=True)
            self.assertEqual(result.returncode,2)


if __name__ == '__main__':
    unittest.main()
