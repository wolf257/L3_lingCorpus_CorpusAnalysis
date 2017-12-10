#!/usr/bin/env python3
#-*- coding : utf-8 -*-


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     PRESENTATION DU MODULE :
#          Ce modules rassemble les functions de
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import os, re, random

import treetaggerwrapper
import pprint , io

from collections import defaultdict

# Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_PROFESSEUR, CORPUS_LITTERATURE, MORPHALO_ROOT, RESULT_RAPPORT_ROOT, TREETAGGER_ROOT
###################################################################################

########################################################
# LIST FUNCTIONS IN MODULES
#	+ tagger_et_recuperer_as_dict + test
#	+
#	+
#	+
#	+
########################################################

folder_treetagger = TREETAGGER_ROOT

# Construction et configuration du wrapper
tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr', TAGINENC='utf-8' , TAGOUTENC='utf-8' , TAGDIR=folder_treetagger)

# def tagger_phrase(phrase):
#     tags = tagger.TagText(phrase)
#     tags2 = treetaggerwrapper.make_tags(tags)

# def tagger_et_afficher(phrase):
#     tags = tagger.TagText(phrase)
#     tags2 = treetaggerwrapper.make_tags(tags)
#     pprint.pprint(tags2)

def tagger_et_recuperer_as_dict_word_to_ref(phrase_to_tag, corpus='professeur',  nom_texte="titre-texte-inconnu", num_phrase='nb-phrase-inconnue', num_mot='nb-mot-inconnu'):

    tags = tagger.TagText(phrase_to_tag)
    tags2 = treetaggerwrapper.make_tags(tags)

    print('Le tagging donne : ')
    pprint.pprint(tags2)

    i = 0
    compteur_max = len(tags2)
    mondico = defaultdict(lambda: defaultdict(dict))

    while i < compteur_max :
        mot = tags2[i][0]
        mot_forme = tags2[i][0]
        mot_pos = tags2[i][1]
        mot_lemme = tags2[i][2]

        mondico[mot]['ref']['corpus'] = corpus
        mondico[mot]['ref']['texte'] = nom_texte
        mondico[mot]['ref']['phrase'] = num_phrase
        mondico[mot]['ref']['mot'] = num_mot

        mondico[mot]['morpho']['form'] = mot_forme
        mondico[mot]['morpho']['pos'] = mot_pos
        mondico[mot]['morpho']['lemme'] = mot_lemme

        mondico[mot]['stat']['apparition_text'] = 0
        mondico[mot]['stat']['apparition_corpus'] = 0
        mondico[mot]['stat']['frequence_in_text'] = 0
        mondico[mot]['stat']['frequence_in_corpus'] = 0

        i+=1

    print('Mis sous forme de dictionnaire, cela nous donne : ')
    pprint.pprint(mondico)

    return mondico
