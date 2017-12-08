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
    name = os.path.basename(os.path.normpath(path_to_corpus))
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n++Nous travaillons sur le corpus : ' , name)
    # E0 : lister les fichiers du corpus
    nom_corpus = str(os.path.relpath(path_to_corpus))


    print('\n+++ Création du dossier : statistiques')
    try :
        if not os.path.exists(path_to_corpus+'statistiques/') :
            os.makedirs(path_to_corpus+'statistiques/')
    except :
        print('\tPROBLEME LORS DE LA CREATION DU DOSSIER.')
    else :
        print('\tCréation du dossier réussi.')
    path_to_corpus_stat = path_to_corpus+'statistiques/'

    files_in_corpus = None
    files_in_corpus = others.list_text_in_folder_as_list(path_to_corpus)
    nb_fichiers_corpus = int(len(files_in_corpus))
    nom_corpus = str(os.path.relpath(path_to_corpus))
    #print('Le corpus ' , os.path.relpath(path_to_corpus) , ' est composé de : ' , len(files_in_corpus) , 'fichiers txt.')
    #pprint.pprint(files_in_corpus)

    # E... : creation du fichier contenant les statistiques du corpus
    nom_fichier_stats_corpus = path_to_corpus_stat+'0_stats_de_'+name+'.txt'
    # nom_fichier_stats_texte = path_to_corpus+files_in_corpus[i]

    # E.. : Ecriture 'nom corpus' 'longueur initiale' 'composition'
    print('\n+++ Création du fichier : 0_stats_du_corpus.txt')
    try :
        with codecs.open(nom_fichier_stats_corpus, mode='a', encoding='utf8') as file_stat_corpus :
            file_stat_corpus.write('====================================================')
            file_stat_corpus.write('\n=== FICHIER CONTENANT LES STATISTIQUES DU CORPUS ===')
            file_stat_corpus.write('\n====================================================')

            file_stat_corpus.write('\n\n==========================')
            file_stat_corpus.write('\n=== PRESENTATION ===')
            file_stat_corpus.write('\n========================')

            file_stat_corpus.write('\n\n Le corpus ')
            file_stat_corpus.write(nom_corpus)
            file_stat_corpus.write(' contient : ')
            file_stat_corpus.write(str(nb_fichiers_corpus))
            file_stat_corpus.write( ' fichiers txt.\n')

            for file in files_in_corpus :
                file_stat_corpus.write('\n'+file)
    except :
        print('\tPROBLEME LORS DE LA CREATION DU FICHIER.')
    else :
        print('\tCréation du fichier réussi.\n')

    # E... : creation dES fichiers contenant les statistiques de chaque texte

    with codecs.open(nom_fichier_stats_corpus, mode='a', encoding='utf8') as file_stat_corpus :
        for file in files_in_corpus :
            print('+++ Création du fichier : ' , '1_stats_de_'+file)
            try :
                path_file = os.path.join(path_to_corpus, file)
                nom_fichier_stats_texte = path_to_corpus_stat+'1_stats_de_'+file

            # E.. : Ecriture 'nom texte' 'longueur initiale'
                with codecs.open(nom_fichier_stats_texte, mode='a', encoding='utf8') as file_stat_file :

                    file_stat_file.write('====================================================')
                    file_stat_file.write('\n=== FICHIER CONTENANT LES STATISTIQUES DE TEXTE ===')
                    file_stat_file.write('\n====================================================')

                    file_stat_file.write('\n\n==========================')
                    file_stat_file.write('\n=== PRESENTATION ===')
                    file_stat_file.write('\n========================')

                    file_stat_file.write('\n\n Le Text ')
                    file_stat_file.write(file)
                    file_stat_file.write(' contient : ')
                    file_stat_file.write( ' xxx lignes.\n')
            except :
                print('\tPROBLEME LORS DE LA CREATION DU FICHIER.')
            else :
                print('\tCréation du fichier réussi.')
        print('\n')

    #creer un fichier stats_corpus
    # mettre dedans :
       # nombre text
       # nom des text

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
