import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(650)

    def test_luodun_kassapaatteen_rahamaara_ja_myytyjen_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_seka_edullisten_etta_maukkauden_lounaiden_osalta(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(600), 200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_toimii_seka_edullisten_etta_maukkauden_lounaiden_osalta(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_ja_kassassa_oleva_rahamaara_kasvaa_ladatulla_summalla (self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 11.5)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 11.5)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005)