#!/usr/bin/env python3
#-*- coding : utf-8 -*-

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     PRESENTATION DU MODULES :
#          Ce modules rassemble les functions de fonctions
#          Dans le souci de ne pas surcharger le fichier main.py
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

########################################################
# LIST FUNCTIONS IN MODULES
#     + tour_du_corpus
#     + tour_des_fichiers
########################################################

import os
import re
import random
import codecs

from collections import defaultdict

#import treetaggerwrapper
import pprint , io

import modules.others as others
import modules.ponctuation_texte as ponctuation_texte
import modules.stats_0_distributions as stats_0_distributions
import modules.writing_in_files as writing_in_files

# Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_PROFESSEUR, CORPUS_LITTERATURE, MORPHALO_ROOT, RESULT_RAPPORT_ROOT, TREETAGGER_ROOT
###################################################################################

##############################################################
# Fonction : 
# Input :
##############################################################
def tour_du_corpus(path_to_corpus):
    ''' Creer et remplit le fichier 0_stats_du_corpus et 1_distribution_mot_du_corpus '''

    # VAR
    nom_corpus = os.path.basename(os.path.normpath(path_to_corpus))
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n++ Nous travaillons sur le corpus : {}'.format(nom_corpus))

    #CREATION DOSSIER STATISTIQUES a la RACINE DU CORPUS
    others.creation_folder(path_to_corpus, 'statistiques')
    #VAR
    path_to_corpus_stat_folder = path_to_corpus+'statistiques/'

    #VAR
    files_in_corpus = None
    files_in_corpus = others.list_text_in_folder_as_list(path_to_corpus)
    dico_distribution_mots_corpus = {}
    ts_text_in_one_string = []

    ########################################
    # DISTRIBUTION FICHIERs INDIVIDUELs TEXTES
    ########################################
    for file in files_in_corpus :
        #VAR
        path_file = os.path.join(path_to_corpus, file)

        ###################################
        #CREATION LISTE À EXPLOITER
        liste_exploitable_txt = ponctuation_texte.du_texte_a_sa_liste_exploitable_par_word_distribution(path_file)
        ###################################

        ts_text_in_one_string += liste_exploitable_txt

    distribution_mots_corpus = stats_0_distributions.wordsDistributionUpdate_dict_from_list(dico_distribution_mots_corpus, ts_text_in_one_string)

    nom_fichier_stats_corpus = path_to_corpus_stat_folder + '0_stats_de_' + nom_corpus + '.txt'

    writing_in_files.remplissage_stat_corpus(nom_fichier_stats_corpus, nom_corpus, files_in_corpus)

    nom_fichier_distribution_corpus = path_to_corpus_stat_folder + '1_distribution_de_' + nom_corpus + '.txt'

    writing_in_files.ecrire_distribution_mot_corpus(nom_fichier_distribution_corpus, path_to_corpus, distribution_mots_corpus)

    #print('\n++++++++++++++++++++++++++++++++++++++++++++++++++')

##############################################################
# Fonction :
# Input :
##############################################################
def tour_des_fichiers(path_to_corpus):
    ''' Creer et remplit le fichier 0_stats et 1_distribution_mot pour chaque fichier du corpus '''

    #VAR
    files_in_corpus = None
    files_in_corpus = others.list_text_in_folder_as_list(path_to_corpus)
    path_to_corpus_stat_folder = path_to_corpus+'statistiques/'

    for file in files_in_corpus :
        #VAR
        path_file = os.path.join(path_to_corpus, file)

        ###################################
        #CREATION LISTE À EXPLOITER
        liste_exploitable_txt = ponctuation_texte.du_texte_a_sa_liste_exploitable_par_word_distribution(path_file)
        ###################################

        distribution_mots_txt = stats_0_distributions.wordsDistribution_dict_from_list(liste_exploitable_txt)

        writing_in_files.remplissage_stat_texte(file, path_to_corpus, path_to_corpus_stat_folder)

        writing_in_files.ecrire_distribution_mot_texte(file, path_to_corpus, path_to_corpus_stat_folder, distribution_mots_txt)

    print('\n++++++++++++++++++++++++++++++++++++++++++++++++++')
