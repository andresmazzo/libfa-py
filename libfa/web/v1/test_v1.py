"""Test module."""

import unittest
from unittest.mock import MagicMock
import libfa.web.v1 as fa_web_v1

import libfa.web.v1.pages as fa_web_pages

import stubs


class TestWebV1(unittest.TestCase):
    """Test module."""

    def test_base_uri(self):
        """test base uri."""
        self.assertEqual(fa_web_v1.base_uri(), 'https://www.filmaffinity.com')

    def test_locales(self):
        """test it returns locales."""
        self.assertEqual(len(fa_web_v1.locales()), 16)

    def test_get_a_movie(self):
        """test it get movie successfully."""
        fa_web_v1.get_html = MagicMock(return_value=stubs.get_html('movie_info'))

        movie = fa_web_v1.movie('ar', '534365')
        # mock.get_html.assert_called()
        self.assertEqual(movie['id'], '534365')

    def test_get_top_fa(self):
        """test it get top fa successfully."""
        fa_web_v1.get_html = MagicMock(return_value=stubs.get_html('top_fa'))

        data = fa_web_v1.top_fa('ar')
        self.assertEqual(data['movies'][0]['id'], '809297')


if __name__ == '__main__':
    unittest.main()
