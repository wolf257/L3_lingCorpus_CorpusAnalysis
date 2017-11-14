#!usr/bin/env python3
# -*- coding : utf8 -*-

import unittest

from traitement_texte import *

class TestStats(unittest.TestCase):

    def test_list_maj_to_min(self):
        a = ['Je' , 'suIS', 'LÀ']

        #result_expected
        aa = ['je' , 'suis', 'là']

        self.assertEqual(list_maj_to_min(a), aa)


if __name__ == '__main__':
    unittest.main()
