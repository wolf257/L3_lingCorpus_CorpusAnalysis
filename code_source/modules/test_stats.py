#!/usr/bin/env python3
#-*- coding : utf8 -*-

import unittest

from stats import *

class TestStats(unittest.TestCase):

    def test_dict_lettersDistribution_from_list(self):
        a = 'abcdee'.split()
        b = '1234'.split()

        #result_expected
        aa = OrderedDict([('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 2)])
        bb = OrderedDict([('1', 1), ('2', 1), ('3', 1), ('4', 1)])

        self.assertEqual(dict_lettersDistribution_from_list(a), aa)
        self.assertEqual(dict_lettersDistribution_from_list(b), bb)

    def test_dict_wordsDistribution_from_list(self):
        a = 'je vais jouer au basket'.split()

        #result_expected
        aa = OrderedDict([('je', 1), ('vais', 1), ('jouer', 1), ('au', 1), ('basket', 1)])

        self.assertEqual(dict_wordsDistribution_from_list(a), aa)
        #self.assertEqual(dict_lettersDistribution_from_list(b), bb)


if __name__ == '__main__':
    unittest.main()