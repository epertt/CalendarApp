import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(self.maksukortti.saldo_euroina(), 12.0)

    def test_rahan_ottaminen_toimii(self):
        self.assertTrue(self.maksukortti.ota_rahaa(200))
        self.assertEqual(self.maksukortti.saldo_euroina(), 8.0)
        

    def test_rahan_ottaminen_toimii2(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1200))
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
