#!/usr/bin/python3

import unittest
import libfa.web.v1 as fa_web_v1

class TestWebV1(unittest.TestCase):

    def test_base_uri(self):
        self.assertEqual(fa_web_v1.base_uri(), 'https://www.filmaffinity.com')

    def test_locales(self):
        self.assertEqual(len(fa_web_v1.locales()), 16)

    def test_movie(self):
        fa_web_v1.movie('ar', '534365')


if __name__ == '__main__':
    unittest.main()
