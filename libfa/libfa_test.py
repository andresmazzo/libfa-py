#!/usr/bin/python3

import unittest
import libfa


class TestLibfa(unittest.TestCase):

    def test_author(self):
        self.assertEqual(libfa.author, 'Andres Mazzo')

    def test_version(self):
        self.assertEqual(libfa.version, '0.0.1')

    def test_web_accesor(self):
        libfa.web
        libfa.web.v1.locales()
        libfa.web.v1.base_uri()
    
    def test_exporter_accesor(self):
        libfa.exporter
        libfa.exporter.csv_v1
        # filepath = sys.argv[1]
        # db = libfa.exporter.csv_v1.ratings(data, filepath)

    def test_importer_accesor(self):
        libfa.importer
        libfa.importer.exportdata
        # zipFilepath = sys.argv[1]
        # libfa.importer.exportdata.run(zipFilepath)


if __name__ == '__main__':
    unittest.main()
