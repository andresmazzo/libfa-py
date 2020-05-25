"""Test module."""

import unittest
import libfa.importer.exportdata as importer


class TestImporterExportdata(unittest.TestCase):
    """test exportdata importer."""

    def test_support_returns_pages(self):
        """Test support()."""
        self.assertEqual(len(importer.support()), 5)


if __name__ == '__main__':
    unittest.main()
