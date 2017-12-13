#!/usr/bin/env python3
#-*- coding : utf-8 -*-

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     PRESENTATION DU MODULE :
#          Ce modules rassemble les functions de fonctions
#          Dans le souci de ne pas surcharger le fichier main.py
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

########################################################
# LIST FUNCTIONS IN MODULES
#     + tour_du_corpus()
#     + tour_des_fichiers()
#     + generation_dico_corpus_pr_xml()
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
import modules.tagging as tagging

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

    nom_fichier_stats_corpus = path_to_corpus_stat_folder + '0_stats_de_' + nom_corpus + '.txt'
    nom_fichier_distribution_corpus = path_to_corpus_stat_folder + '1_distribution_de_' + nom_corpus + '.txt'

    files_in_corpus = None
    files_in_corpus = others.list_text_in_folder_as_list(path_to_corpus)

    dico_distribution_mots_corpus = {}
    ts_text_in_one_string = []

    for file in files_in_corpus :
        #VAR
        path_file = os.path.join(path_to_corpus, file)

        ###################################
        #CREATION LISTE À EXPLOITER
        liste_exploitable_txt = ponctuation_texte.du_texte_a_sa_liste_exploitable_par_word_distribution(path_file)
        ###################################

        ts_text_in_one_string += liste_exploitable_txt

    distribution_mots_corpus = stats_0_distributions.wordsDistributionUpdate_dict_from_list(dico_distribution_mots_corpus, ts_text_in_one_string)

    writing_in_files.remplissage_stat_corpus(nom_fichier_stats_corpus, nom_corpus, files_in_corpus)

    writing_in_files.ecrire_distribution_mot_corpus(nom_fichier_distribution_corpus, path_to_corpus, distribution_mots_corpus)

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

##############################################################
# Fonction : 
# Input :
##############################################################

def generation_dico_corpus_pr_xml(path_to_corpus):
    #VAR
    dico_tag_corpus = defaultdict(lambda: defaultdict(dict))

    nom_corpus = os.path.basename(os.path.normpath(path_to_corpus))
    if nom_corpus == 'corpus_litterature' :
        num_corpus = 1
    else :
        num_corpus = 2
    reference_corpus = 'c'+str(num_corpus)

    print('++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n++ Nous allons tagger et recupérer les mots du corpus {}. \n Souhaitez-nous bonne chance'.format(nom_corpus))

    #CREATION DOSSIER TAG a la RACINE DU CORPUS
    others.creation_folder(path_to_corpus, 'tag')

    #VAR
    path_to_corpus_stat_folder = path_to_corpus+'statistiques/'
    path_to_corpus_donnee_tag_folder = path_to_corpus+'tag/'

    files_in_corpus = None
    files_in_corpus = others.list_text_in_folder_as_list(path_to_corpus)

    #nom_fichier_donner_tag_corpus = path_to_corpus_stat_folder + '0_stats_de_' + nom_corpus + '.txt'
    nom_fichier_distribution_corpus ='1_distribution_de_' + nom_corpus + '.txt'
    path_fichier_distribution_corpus = os.path.join(path_to_corpus_stat_folder, nom_fichier_distribution_corpus )
    liste_fichier_distribution_corpus = others.import_distribution_as_list(path_fichier_distribution_corpus)
    # try :
    #     obj_file_distribution_corpus = codecs.open(path_fichier_distribution_corpus, mode='r', encoding='utf8')
    # except :
    #     print('\nProblème lors de l\'ouverture de : {}'.format(nom_fichier_distribution_corpus))
    # else :
    #     print('\nOuverture du fichier \'{}\' réussie'.format(nom_fichier_distribution_corpus))

    #     try :
    #         list_distribution_corpus = []
    #         for line in obj_file_distribution_corpus :
    #             list_distribution_corpus += line
    #     except :
    #         print('\nProblème lors de la création de la liste \'list_distribution_corpus\'')
    #     else :
    #         print('\nListe \'list_distribution_corpus\' créée')
    #dico_distribution_mots_corpus = {}
    #ts_text_in_one_string = []

    #######
    # Niveau des textes
    ######
    #index_du_texte = 1
    #nb_fichiers_dans_corpus = len(files_in_corpus)

    text_for_tagg = []

    #reference_texte = 'c'+num_corpus+'t'+num_phrase+'s'+num_texte+'w'+index_du_mot

    for file in files_in_corpus:
        path_file = os.path.join(path_to_corpus, file)

        nom_fichier_distribution_texte = file[:-4] + '_2_distributions.txt'
        path_fichier_distribution_texte = os.path.join(path_to_corpus_stat_folder, nom_fichier_distribution_texte)
        liste_fichier_distribution_texte = others.import_distribution_as_list(path_fichier_distribution_texte)

        # try :
        #     obj_file_distribution_texte = codecs.open(path_fichier_distribution_texte, mode='r', encoding='utf8')
        # except :
        #     print('\nProblème lors de l\'ouverture de : {}'.format(nom_fichier_distribution_texte))
        # else :
        #     print('\nOuverture du fichier \'{}\' réussie'.format(nom_fichier_distribution_texte))
        #     print(obj_file_distribution_texte)
        #     try :
        #         list_distribution_texte = []
        #         for line in obj_file_distribution_texte :
        #             list_distribution_texte += line
        #     except :
        #         print('\nProblème lors de la création de la liste \'list_distribution_texte\'')
        #     else :
        #         print('\nListe \'list_distribution_texte\' créée')
        #         #print(list_distribution_texte)

        num_texte = int(files_in_corpus.index(file)) + 1
        reference_texte = 'c'+str(num_corpus)+'t'+str(num_texte)

        ###################################
        #CREATION LISTE À EXPLOITER
        text_for_tagg = ponctuation_texte.du_texte_a_sa_liste_exploitable_par_tagging(path_file)
        ###################################

        #print(text_for_tagg)

        compteur_ligne = 0
        nb_lignes_in_texte = len(text_for_tagg)
        #print('Le text {} a {} lignes à traiter'.format(reference_texte, nb_lignes_in_texte))

        while compteur_ligne < nb_lignes_in_texte :
            #num_line = int(text_for_tagg.index(compteur_ligne)) + 1

            num_line = compteur_ligne
            line = text_for_tagg[compteur_ligne]

            reference_line = 'c'+str(num_corpus)+'t'+str(num_texte)+'s'+str(num_line)

            print('\n\n{}'.format('='*35))
            print('***Ref ligne : {}'.format(reference_line))
            print('***Contenu : {}'.format(line))

            tagging.tagger_phrase_et_ajouter_au_dict_ref_to_word(dico_tag_corpus, line, liste_fichier_distribution_corpus, liste_fichier_distribution_texte, num_corpus, num_texte, num_line)

            compteur_ligne +=1

    #     if obj_file_distribution_texte :
    #         obj_file_distribution_texte.close()
    # if obj_file_distribution_corpus :
    #     obj_file_distribution_corpus.close()

    return dico_tag_corpus
