#!/usr/bin/env python3
#-*- coding : utf8 -*-

import unittest

from stats_1_base import *

class TestStats(unittest.TestCase):

    def test_count_sentences_nb_from_string_or_list(self):
        a = "j'y vais . je suis là . je pars ."
        b = "j'y vais. je suis là . je pars ."
        c = "j'y vais. je suis là. je pars."
        #d = "j'y vais... je suis là. je pars." #TODO : find solution

        #result_expected
        count_sentences_a = 3
        count_sentences_b = 3
        count_sentences_c = 3
        #count_sentences_d = 2

        self.assertEqual(count_sentences_nb_from_string_or_list(a), count_sentences_a)
        self.assertEqual(count_sentences_nb_from_string_or_list(b), count_sentences_b)
        self.assertEqual(count_sentences_nb_from_string_or_list(c), count_sentences_c)
        #self.assertEqual(count_sentences_nb_from_string_or_list(d), count_sentences_d)

    # def test_average_words_by_sentence_nb_from_list(self):
    #     a = "j'y vais . je suis là ."
    #
    #     #result_expected
    #     aa = 2.5
    #
    #     self.assertEqual(average_words_by_sentence_nb_from_list(a), aa)

if __name__ == '__main__':
    unittest.main()
