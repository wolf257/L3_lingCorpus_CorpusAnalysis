#!/usr/bin/env python3
#-*- coding : utf8 -*-

import unittest

from tagging import *

class TestStats(unittest.TestCase):

    def test_tagger_et_recuperer_as_dict(self):
        phrase = 'je vais à Vienne.'
        dico = None
        dico = tagger_et_recuperer_as_dict(phrase)

        self.assertIsInstance(d, dict)

if __name__ == '__main__':
    unittest.main()
