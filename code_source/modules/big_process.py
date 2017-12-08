#!/usr/bin/env python3
#-*- coding : utf-8 -*-

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     PRESENTATION DU MODULES :
#          Ce modules rassemble les functions de fonctions
#          Dans le souci de ne pas surcharger le fichier main.py
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import os
import re
import random
import codecs

from collections import defaultdict

#import treetaggerwrapper
import pprint , io

import modules.others as others
import modules.ponctuation_texte as ponctuation_texte
#import modules.stats_1_base as stats_1_base
#import modules.tagging as tagging

# Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_PROFESSEUR, CORPUS_LITTERATURE, MORPHALO_ROOT, RESULT_RAPPORT_ROOT, TREETAGGER_ROOT
###################################################################################

dossier_corpus = CORPUS_LITTERATURE
liste_fichiers = others.list_text_in_folder_as_list(dossier_corpus)

def tour_du_corpus(path_to_corpus):
    nom_corpus = os.path.basename(os.path.normpath(path_to_corpus))
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n++ Nous travaillons sur le corpus : ' , nom_corpus)

    # E0 : CREATION DOSSIER STATISTIQUES a la RACINE DU CORPUS
    print('\n+++ Création du dossier : statistiques')
    try :
        if not os.path.exists(path_to_corpus+'statistiques/') :
            os.makedirs(path_to_corpus+'statistiques/')
    except :
        print('\tPROBLEME LORS DE LA CREATION DU DOSSIER.')
    else :
        print('\tCréation du dossier réussi.')
    path_to_corpus_stat = path_to_corpus+'statistiques/'

    # LISTE FICHIERS DU CORPUS
    files_in_corpus = None
    files_in_corpus = others.list_text_in_folder_as_list(path_to_corpus)
    nb_fichiers_corpus = len(files_in_corpus)

    ########################################
    # FICHIER PRINCIPAL CORPUS
    ########################################
    # CREATION FICHIER STATISTIQUES_CORPUS DANS DOSSIER STATISTIQUES
        # Ajout titre corpus et contenu
    nom_fichier_stats_corpus = path_to_corpus_stat+'0_stats_de_'+nom_corpus+'.txt'
    print('\n++++ Création du fichier : 0_stats_du_corpus.txt')
    try :
        with codecs.open(nom_fichier_stats_corpus, mode='a', encoding='utf8') as file_stat_corpus :
            file_stat_corpus.write('\n\n{}\n{} FICHIER CONTENANT STATISTIQUES DE CORPUS {}\n{}'.format('='*60 , '='*10 , '='*10 , '='*60))

            file_stat_corpus.write('\n\n{}\n{} PRESENTATION {}\n{}'.format('='*30 , '='*7 , '='*7 , '='*30))

            file_stat_corpus.write('\n\nLe corpus {} contient {} fichiers txt : '.format(nom_corpus , nb_fichiers_corpus))

            for file in files_in_corpus :
                file_stat_corpus.write('\n - {}'.format(file))
    except :
        print('\tPROBLEME LORS DE LA CREATION DU FICHIER.')
    else :
        print('\tCréation du fichier réussi.\n')


    ########################################
    # FICHIERs INDIVIDUELs TEXTES
    ########################################
    # CREATION FICHIER STATISTIQUES_TEXTE DANS DOSSIER STATISTIQUES
        # Ajout titre texte
    for file in files_in_corpus :
        print('++++ Création du fichier : ' , '1_stats_de_'+file)
        try :
            path_file = os.path.join(path_to_corpus, file)
            nom_fichier_stats_texte = path_to_corpus_stat+'1_stats_de_'+file

        # E.. : Ecriture 'nom texte' 'longueur initiale'
            with codecs.open(nom_fichier_stats_texte, mode='a', encoding='utf8') as file_stat_file :

                file_stat_file.write('\n\n{}\n{} FICHIER CONTENANT STATISTIQUES DU TEXTE : \n\t\t {} {}\n{}'.format('='*80 , '='*10 , file , '='*10 , '='*80))

                file_stat_file.write('\n\n{}\n{} PRESENTATION {}\n{}'.format('='*30 , '='*7 , '='*7 , '='*30))

                #file_stat_file.write('\n\nLe texte {} contient {} lignes.'.format(file, 'xxx'))
        except :
            print('\tPROBLEME LORS DE LA CREATION DU FICHIER.')
        else :
            print('\tCréation du fichier réussi.')
    print('\n')

    ########################################
    # DISTRIBUTION FICHIERs INDIVIDUELs TEXTES
    ########################################
    for file in files_in_corpus :
        path_file = os.path.join(path_to_corpus, file)
        #IMPORTER LE TEXTE EN UNE STR
        file_as_string = others.import_text_as_one_string(path_file)
        # ENLEVER LES 3 POINTS : STR
        string_2 = ponctuation_texte.all_three_points_become_one_string_from_string(file_as_string)
        # CONVERTIR EN LISTE : LIST
        liste_1 = string_2.split()
        # SEPARER LA PONCTUATION DES MOTS LIST
        liste_2 = ponctuation_texte.punctuation_sep_word_list_from_list(liste_1)

    #creer un fichier stats_corpus
    # mettre dedans :
       # nombre text DONE
       # nom des text DONE

    # dans chacun des textes :
        # creer fichiers text_stats_base

        # importer le texte en une string
        # out but point, ! et ?
        # distribution des lettre
            #pause : avez vous verifie ?
                 #option skip it
        # nombre de phrase
        #distribution des mots
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')
