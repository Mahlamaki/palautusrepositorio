import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            
        kauppa_mock = Mock()



        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        #oikealla asiakkaalla,tilinumeroilla ja summalla
        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla_kun_kaksi_tuotetta(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "juusto", 7)
            
            
        kauppa_mock = Mock()


        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote


        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("mikko", "23456")

        pankki_mock.tilisiirto.assert_called_with("mikko", 42, "23456", "33333-44455", 12)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla_kun_kaksi_samaa_tuotetta(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "juusto", 7)
            
            
        kauppa_mock = Mock()


        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote


        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("mikko", "23456")

        pankki_mock.tilisiirto.assert_called_with("mikko", 42, "23456", "33333-44455", 10)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla_kun_toinen_tuote_loppu(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "juusto", 7)
            
            
        kauppa_mock = Mock()



        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote



        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("mikko", "23456")

        pankki_mock.tilisiirto.assert_called_with("mikko", 42, "23456", "33333-44455", 5)

    def test_asioinnin_aloitus_nollaa_edellisen_tapahtuman(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "juusto", 7)
            
            
        kauppa_mock = Mock()


        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("mikko", "23456")
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("mikko", "23456")

        pankki_mock.tilisiirto.assert_called_with("mikko", 42, "23456", "33333-44455", 7)

    def test_kauppa_pyytää_uuden_viitenumeron_maksutapahtumille(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.side_effect = [12323, 111111]

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "juusto", 7)
            
        kauppa_mock = Mock()

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote


        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("mikko", "23456")
        pankki_mock.tilisiirto.assert_called_with(ANY, 12323, ANY, ANY, ANY)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("mikko", "23456")

        pankki_mock.tilisiirto.assert_called_with(ANY, 111111, ANY, ANY, ANY)

    def test_ostoskorista_poistaminen_toimii(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        ostoskori_mock = Mock()

        viitegeneraattori_mock.uusi.side_effect = [12323, 111111]

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "juusto", 7)


            
        kauppa_mock = Mock()

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.poista_korista(1)
        kauppa.tilimaksu("mikko", "23456")


        pankki_mock.tilisiirto.assert_called_with(ANY,ANY, ANY, ANY, 5)


