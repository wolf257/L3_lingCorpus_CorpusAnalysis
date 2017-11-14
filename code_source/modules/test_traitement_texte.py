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
        a = 'je suis... ou je vais, au basket.'.split()
        b = "j'ai joué... au basket.".split()

        #result_expected
        aa = ['je' , 'suis' , '.' , '.' , '.' , 'ou' , 'je' , 'vais' , ',' , 'au' , 'basket' , '.']
        bb = ["j'ai" , 'joué' , '.' , '.' , '.' , 'au' , 'basket' , '.']

        self.assertEqual(list_punctuation_sep_from_list(a), aa)
        self.assertEqual(list_punctuation_sep_from_list(b), bb)

    def test_list_all_punctuation_out_from_list(self):
        a = "j'ai joué... au basket.".split()
        b = "j'y ai travaillé pendant 2 heures 30.".split()

        #result_expected
        aa = ["j'ai" , 'joué' , 'au' , 'basket' ]
        bb = ["j'y" , 'ai' , 'travaillé' , 'pendant' , '2' , 'heures' , '30' ]

        self.assertEqual(list_all_punctuation_out_from_list(a), aa)
        self.assertEqual(list_all_punctuation_out_from_list(b), bb)

    def test_list_all_but_point_and_word_from_list(self):
        a = "j'ai joué au basket.".split()
        b = "j'ai vu, entendu, et lu.".split()

        #result_expected
        aa = ["j'ai" , 'joué' , 'au' , 'basket' , '.' ]
        bb = ["j'ai" , 'vu' , 'entendu' , 'et' , 'lu' , '.' ]

        self.assertEqual(list_all_but_point_and_word_from_list(a), aa)
        self.assertEqual(list_all_but_point_and_word_from_list(b), bb)

if __name__ == '__main__':
    unittest.main()
