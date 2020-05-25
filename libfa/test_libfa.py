"""Test libfa module."""
import unittest
import libfa


class TestLibfa(unittest.TestCase):
    """Test libfa."""

    def test_author(self):
        """Test author."""
        self.assertEqual(libfa.AUTHOR, 'Andres Mazzo')

    def test_version(self):
        """Test author."""
        self.assertEqual(libfa.VERSION, '0.0.1')

    def test_web_accesor(self):
        """Test web accessor."""
        try:
            libfa.web
            libfa.web.v1.locales()
            libfa.web.v1.base_uri()
        except AttributeError:
            self.fail("libfa hasn't attributes")

    def test_exporter_accesor(self):
        """Test exporter accessor."""
        try:
            libfa.exporter
            libfa.exporter.csv_v1
        except AttributeError:
            self.fail("libfa hasn't attributes")
        # filepath = sys.argv[1]
        # db = libfa.exporter.csv_v1.ratings(data, filepath)

    def test_importer_accesor(self):
        """Test importer accessor."""
        try:
            libfa.importer
            libfa.importer.exportdata
        except AttributeError:
            self.fail("libfa hasn't attributes")
        # zipFilepath = sys.argv[1]
        # libfa.importer.exportdata.run(zipFilepath)


if __name__ == '__main__':
    unittest.main()
