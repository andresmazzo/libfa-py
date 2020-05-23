#!/usr/bin/python3

import unittest
import libfa.importer.exportdata as importer

class TestImporterExportdata(unittest.TestCase):

    def test_run(self):
        self.assertEqual(len(importer.support()), 5)



if __name__ == '__main__':
    unittest.main()
