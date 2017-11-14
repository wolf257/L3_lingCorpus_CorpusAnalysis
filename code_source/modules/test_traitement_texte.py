#!/usr/bin/env python3
# -*- coding : utf8 -*-

import unittest

from traitement_texte import *

class TestStats(unittest.TestCase):

    def test_list_maj_to_min_from_list(self):
        a = ['Je' , 'suIS', 'LÀ']

        #result_expected
        aa = ['je' , 'suis', 'là']

        self.assertEqual(list_maj_to_min_from_list(a), aa)

    def test_list_punctuation_sep_from_list(self):
        a = 'je suis, ou je vais, au basket.'.split()

        #result_expected
        aa = ['je' , 'suis' , ',' , 'ou' , 'je' , 'vais' , ',' , 'au' , 'basket' , '.']

        self.assertEqual(list_punctuation_sep_from_list(a), aa)



if __name__ == '__main__':
    unittest.main()
