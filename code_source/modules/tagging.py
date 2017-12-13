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

import modules.others as others

# Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_PROFESSEUR, CORPUS_LITTERATURE, MORPHALO_ROOT, RESULT_RAPPORT_ROOT, TREETAGGER_ROOT
###################################################################################

########################################################
# LIST FUNCTIONS IN MODULES
#	+ tagger_et_recuperer_as_dict_word_to_ref + test
#	+ tagger_et_recuperer_as_dict_ref_to_ref
#	+
#	+
#	+
########################################################

folder_treetagger = TREETAGGER_ROOT

# Construction et configuration du wrapper
tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr', TAGINENC='utf-8' , TAGOUTENC='utf-8' , TAGDIR=folder_treetagger)


def tagger_phrase_et_ajouter_au_dict_ref_to_word(dico_tag_corpus, phrase_to_tag,
                                                obj_file_distribution_corpus, obj_file_distribution_texte,
                                                 num_corpus='num_corpus_NR', num_texte='num_texte_NR',
                                                 num_phrase='num_phrase_NR') :

    #TAGGER LA PHRASE
    tags = tagger.TagText(phrase_to_tag)
    tags2 = treetaggerwrapper.make_tags(tags)

    #print('Le tagging donne : ')
    #pprint.pprint(tags2)

    # VAR
    compteur_mot = 0
    nb_mots_dans_phrase = len(tags2)
    mondico = defaultdict(lambda: defaultdict(dict))

    while compteur_mot < nb_mots_dans_phrase :
        #num_mot = tags2.index(line_word)
        num_mot = compteur_mot
        # Ref : Cx Tx Sx Wx
        reference_mot = 'c'+str(num_corpus)+'t'+str(num_texte)+'s'+str(num_phrase)+'w'+str(num_mot)

        #print(reference_mot)

        # RECUPERATION DES INFOS
        try :
            mot_forme = tags2[num_mot][0]
        except :
            mot_forme = 'forme_NR'
        try :
            mot_pos = tags2[num_mot][1]
        except :
            mot_pos = 'POS_NR'
        try :
            mot_lemme = tags2[num_mot][2]
        except :
            mot_lemme = 'lemme_NR'

        #RECHERCHE DES OCCURENCES
        try :
            mot_occurrence_texte = others.recherche_occurence_mot_in_file_distribution(obj_file_distribution_texte, mot_forme)
        except :
            mot_occurrence_texte = 'occurrence_texte_NR'

        try :
            mot_occurrence_corpus = others.recherche_occurence_mot_in_file_distribution(obj_file_distribution_corpus, mot_forme)
        except :
             mot_occurrence_corpus = 'occurence_corpus_NR'
        # TEST
        print('\nTEST : La ref \'{}\' pointe vers le mot \'{}\', lemme \'{}\', Pos \'{}\'.'.format(reference_mot, mot_forme, mot_lemme, mot_pos))
        print('OT : {} et OC : {}'.format(mot_occurrence_texte, mot_occurrence_corpus))

        # AUTRE RECHERCHE




        compteur_mot += 1

    #while index_du_mot < nb_mots_dans_phrase :
        # Ref : Cx Tx Sx Wx
        #reference_mot = 'c'+str(num_corpus)+'t'+str(num_texte)+'s'+str(num_phrase)+'w'+str(index_du_mot)

        #mot = tags2[index_du_mot][0]
        #mot_forme = tags2[index_du_mot][0]
        #mot_pos = tags2[index_du_mot][1]
        #mot_lemme = tags2[index_du_mot][2]

        #mondico[reference_mot]['reference']['corpus'] = corpus
        #mondico[reference_mot]['reference']['texte'] = nom_texte
        #mondico[reference_mot]['reference']['phrase'] = num_phrase
        #mondico[reference_mot]['reference']['mot'] = num_mot

        # dico_tag_corpus[reference_mot]['morphology']['form'] = mot_forme
        # dico_tag_corpus[reference_mot]['morphology']['pos'] = mot_pos
        # dico_tag_corpus[reference_mot]['morphology']['lemme'] = mot_lemme

        # dico_tag_corpus[reference_mot]['statistics']['apparition_in_text'] = 0
        # dico_tag_corpus[reference_mot]['statistics']['apparition_in_corpus'] = 0
        # dico_tag_corpus[reference_mot]['statistics']['frequence_in_text'] = 0
        # dico_tag_corpus[reference_mot]['statistics']['frequence_in_corpus'] = 0

        # index_du_mot += 1

    #print('Mis sous forme de dictionnaire, cela nous donne : ')
    #pprint.pprint(mondico)

    #return mondico
