import unittest
from dna_analysis.operations.restriction_sites import (
    find_restriction_sites,
    count_restriction_sites
)


class TestFindRestrictionSites(unittest.TestCase):

    def test_find_restriction_sites_valid_sequence(self):
        # Test para una secuencia de ADN válida
        sequence = "ATGCATGCAAAGCTAGCTGATCGATGCTAGCTAGCTAG"
        enzymes = ["EcoRI", "BamHI", "HindIII"]

        # Verificar que se encuentren los sitios de corte para cada enzima
        sites = find_restriction_sites(sequence, enzymes)

        # Verificar que se devuelva un diccionario con los sitios encontrados
        self.assertIsInstance(sites, dict)

        # Verificar que se encuentren los sitios de corte para cada enzima solicitada
        for enzyme in enzymes:
            self.assertIn(enzyme, sites)
            self.assertIsInstance(sites[enzyme], list)
            self.assertTrue(all(isinstance(site, int)
                            for site in sites[enzyme]))

    def test_count_restriction_sites_empty_sequence(self):
        # Test para una secuencia de ADN vacía
        sequence = ""
        enzymes = ["EcoRI", "BamHI", "HindIII"]

        # Verificar que lance un ValueError cuando la secuencia está vacía
        with self.assertRaises(ValueError):
            count_restriction_sites(sequence, enzymes)

    def test_count_restriction_sites_invalid_enzyme(self):
        # Test para una enzima de restricción no reconocida
        sequence = "ATGCATGCAAAGCTAGCTGATCGATGCTAGCTAGCTAG"
        enzymes = ["EcoRI", "XYZ"]

        # Verificar que lance un ValueError cuando se proporciona una enzima no reconocida
        with self.assertRaises(ValueError):
            count_restriction_sites(sequence, enzymes)

    def test_count_restriction_sites_no_sites_found(self):
        # Test para una secuencia sin sitios de corte para ninguna enzima
        sequence = "ATGCATGCAAAGCTAGCTGATCGATGCTAGCTAGCTAG"
        enzymes = ["NotI", "PstI"]

        # Verificar que se devuelva un diccionario vacío
        sites = count_restriction_sites(sequence, enzymes)
        self.assertEqual(sites, {"NotI": 0, "PstI": 0})


if __name__ == '__main__':
    unittest.main()
