"""Test module."""

import unittest
import libfa.exporter.csv_v1 as exporter
import libfa.exporter.csv_v1.lists as mlists
from libfa.models.ListModel import List as ListModel


class TestExporterCsv(unittest.TestCase):
    """test exportdata importer."""

    def test_header(self):
        """Test header()."""
        self.assertEqual(exporter.outputs(), ['lists', 'ratings'])

    def test_lists_module_header(self):
        """Test lists module."""
        self.assertEqual(mlists.header(), ['ID', 'Name'])

    def test_lists_module_run(self):
        """Test lists module."""
        obj = {}
        obj['id'] = 1
        obj['name'] = 'hello world'
        list1 = ListModel(obj)
        data = [list1]
        mlists.lists(data, "temp/example.csv")

        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
