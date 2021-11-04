import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_varastolla_ei_ole_negatiivista_tilavuutta(self):
        uusi_varasto = Varasto(-10)
        self.assertAlmostEqual(uusi_varasto.tilavuus, 0)

    def test_uudella_varastolla_ei_ole_negatiivista_saldoa(self):
        uusi_varasto = Varasto(10, -10)
        self.assertAlmostEqual(uusi_varasto.saldo, 0)

    def test_uudella_varastolla_saldo_ei_suurempi_kuin_tilavuus(self):
        uusi_varasto = Varasto(10, 20)
        self.assertAlmostEqual(uusi_varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_ei_ylita_maksimi_tilavuutta(self):
        self.varasto.lisaa_varastoon(11)

        # vapaata tilaa pitäisi olla 0
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_lisays_ei_hyvaksy_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_ei_anna_enemman_kuin_varastossa_on(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu_maara, 5)

    def test_ottaminen_ei_hyvaksy_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-10)

        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_merkkijonoesitys_sisaltaa_oikean_saldon_ja_tilan(self):
        self.varasto.lisaa_varastoon(6)
        self.assertEqual(self.varasto.__str__(), "saldo = 6, vielä tilaa 4")
