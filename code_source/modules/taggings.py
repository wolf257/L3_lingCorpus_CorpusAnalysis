#!/usr/bin/env python3
#-*- coding : utf-8 -*-

import os
import re
import random

import treetaggerwrapper
import pprint , io

import modules.others as others
import modules.ponctuation_texte as ponctuation_texte
import modules.stats_1_base as stats_1_base

## Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_TEST_ROOT, MORPHALO_ROOT, RESULT_RAPPORT_ROOT, TREETAGGER_ROOT
###################################################################################

folder_treetagger = TREETAGGER_ROOT

# Construction et configuration du wrapper
tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr', TAGINENC='utf-8' , TAGOUTENC='utf-8' , TAGDIR=folder_treetagger)

def tagger_phrase(phrase):
    tags = tagger.TagText(phrase)
    tags2 = treetaggerwrapper.make_tags(tags)

def tagger_et_afficher(phrase):
    tags = tagger.TagText(phrase)
    tags2 = treetaggerwrapper.make_tags(tags)
    pprint.pprint(tags2)

def tagger_et_recuperer_as_list(arg):
    tags = tagger.TagText(phrase)
    tags2 = treetaggerwrapper.make_tags(tags)

    i = 0
    compteur_max = len(tags2)
    dico = {}

    while i < compteur_max :
        # dico[tags2[i]] 
        print("forme : " , tags2[i][0])
        i+=1

    # for mot in tags2 :
    #     mot_forme = tags2[mot][0]
    #     mot_pos = tags2[mot][1]
    #     mot_lemme = tags2[mot][2]

def tagger_et_recuperer_as_dict(arg):
    tags = tagger.TagText(phrase)
    tags2 = treetaggerwrapper.make_tags(tags)

    for mot in tags2 :
        mot_forme = tags2[mot][0]
        mot_pos = tags2[mot][1]
        mot_lemme = tags2[mot][2]

def tagger_et_ajout_to_dict(phrase):
