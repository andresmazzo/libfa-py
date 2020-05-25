"""Test module."""

import unittest
import libfa.web.v1 as fa_web_v1


class TestWebV1(unittest.TestCase):
    """Test module."""

    def test_base_uri(self):
        """test base uri."""
        self.assertEqual(fa_web_v1.base_uri(), 'https://www.filmaffinity.com')

    def test_locales(self):
        """test it returns locales."""
        self.assertEqual(len(fa_web_v1.locales()), 16)

    def test_movie(self):
        """test it get movie successfully."""
        try:
            fa_web_v1.movie('ar', '534365')
        except AttributeError:
            self.fail("failed to get movie")


if __name__ == '__main__':
    unittest.main()
