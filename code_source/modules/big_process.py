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
import modules.stats_0_distributions as stats_0_distributions

#import modules.stats_1_base as stats_1_base
#import modules.tagging as tagging

# Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_PROFESSEUR, CORPUS_LITTERATURE, MORPHALO_ROOT, RESULT_RAPPORT_ROOT, TREETAGGER_ROOT
###################################################################################

#dossier_corpus = CORPUS_LITTERATURE
#liste_fichiers = others.list_text_in_folder_as_list(dossier_corpus)

def creation_folder(path_to_parent, name_folder):
    print('\n+++ Création du dossier : ' , name_folder)
    try :
        if not os.path.exists(path_to_parent + name_folder + '/') :
            os.makedirs(path_to_parent + name_folder + '/')
    except :
        print('\tPROBLEME LORS DE LA CREATION DU DOSSIER.')
    else :
        print('\tCréation du dossier réussi.')

def remplissage_info_base_corpus(nom_fichier_stats_corpus, nom_corpus, files_in_corpus):
    print('\n++++ Création du fichier : 0_stats_du_corpus.txt')
    try :
        #OPEN FILE
        file_stat_corpus = codecs.open(nom_fichier_stats_corpus, mode='a', encoding='utf8')
    except :
        print('\tPROBLEME LORS DE LA CREATION DU FICHIER.')
    else :
        print('\tCréation du fichier réussi.')

        try :
            # REMPLISSAGE FILE
            file_stat_corpus.write('\n\n{}\n{} FICHIER CONTENANT STATISTIQUES DE CORPUS {}\n{}'.format('='*60 , '='*10 , '='*10 , '='*60))

            file_stat_corpus.write('\n\n{}\n{} PRESENTATION {}\n{}'.format('='*30 , '='*7 , '='*7 , '='*30))

            file_stat_corpus.write('\n\nLe corpus {} contient {} fichiers txt : '.format(nom_corpus , len(files_in_corpus)))

            for file in files_in_corpus :
                file_stat_corpus.write('\n - {}'.format(file))
        except :
            print('\t\tProblème lors du remplissage')
        else :
            print('\tRemplissage du fichier réussi.')
            #CLOSE FILE
            file_stat_corpus.close()
            print('\tFichier fermé\n')


def du_texte_a_sa_premiere_distribution(path_file):
        #IMPORTER LE TEXTE EN UNE STR
        file_as_string = others.import_text_as_one_string(path_file)
        # ENLEVER LES 3 POINTS : STR
        string_2 = ponctuation_texte.all_three_points_become_one_string_from_string(file_as_string)
        # CONVERTIR EN LISTE : LIST
        liste_1 = string_2.split()
        # SEPARER LA PONCTUATION DES MOTS LIST : LIST
        liste_2 = ponctuation_texte.punctuation_sep_word_list_from_list(liste_1)
        # DISTRIBUTION MOTS IN TEXT : DICT
        distribution_mots_txt = stats_0_distributions.wordsDistribution_dict_from_list(liste_2)

        return distribution_mots_txt

def ecrire_distribution_mot_texte_dans_2_distri(file, path_to_corpus, path_to_corpus_stat_folder, dico_distribution):
        print('+++++ Création du fichier : ' , file[:-4] + '_2_distributions.txt')
        path_file = os.path.join(path_to_corpus, file)
        nom_fichier_distri_texte = path_to_corpus_stat_folder + file[:-4] + '_2_distributions.txt'
        try :
            file_distro_file = codecs.open(nom_fichier_distri_texte, mode='a', encoding='utf8')
        except :
           print('\tPROBLEME LORS DE LA CREATION DU FICHIER.')
        else :
            print('\tCréation du fichier réussi.')
            print('\tFichier ouvert en mode ecriture.')

            try :
                file_distro_file.write('\n\n{}\n{} FICHIER CONTENANT LA DISTRIBUTION DES MOTS DU TEXTE : \n\t\t {} {}\n{}'.format('='*80 , '='*10 , file , '='*10 , '='*80))

                file_distro_file.write('\n\n{}\n{} PRESENTATION {}\n{}\n\n'.format('='*30 , '='*7 , '='*7 , '='*30))

                for word, number in dico_distribution.items():
                    file_distro_file.write('{} : {}\n'.format(word, number))

                #file_stat_file.write('\n\nLe texte {} contient {} lignes.'.format(file, 'xxx'))
            except :
                print('\tPROBLEME LORS DU REMPLISSAGE DU FICHIER.')
            else :
                print('\tRemplissage du fichier réussi.')
                file_distro_file.close()
                print('\tFichier fermé')

def tour_du_corpus(path_to_corpus):
    #VAR
    nom_corpus = os.path.basename(os.path.normpath(path_to_corpus))

    print('++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n++ Nous travaillons sur le corpus : ' , nom_corpus)

    # E0 : CREATION DOSSIER STATISTIQUES a la RACINE DU CORPUS
    creation_folder(path_to_corpus, 'statistiques')

    ########################################
    # FICHIER PRINCIPAL CORPUS
    ########################################

    #VAR
    path_to_corpus_stat_folder = path_to_corpus+'statistiques/'

    # LISTE FICHIERS DU CORPUS
    files_in_corpus = None
    files_in_corpus = others.list_text_in_folder_as_list(path_to_corpus)
    #nb_fichiers_corpus = len(files_in_corpus)


    # CREATION FICHIER STATISTIQUES_CORPUS DANS DOSSIER STATISTIQUES
        # Ajout titre corpus et contenu

    #VAR
    nom_fichier_stats_corpus = path_to_corpus_stat_folder+'0_stats_de_'+nom_corpus+'.txt'

    remplissage_info_base_corpus(nom_fichier_stats_corpus, nom_corpus, files_in_corpus)

    ########################################
    # FICHIERs INDIVIDUELs TEXTES
    ########################################
    # CREATION FICHIER STATISTIQUES_TEXTE DANS DOSSIER STATISTIQUES
        # Ajout titre texte
    for file in files_in_corpus :
        # A METTRE SOUS FORME DE FONCTION
        print('++++ Création du fichier : ' , file[:-4]+'_1_stats.txt')
        try :
            path_file = os.path.join(path_to_corpus, file)
            nom_fichier_stats_texte = path_to_corpus_stat_folder+file[:-4]+'_1_stats.txt'

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

    #dico_distribution_mots_corpus = {}

    ########################################
    # DISTRIBUTION FICHIERs INDIVIDUELs TEXTES
    ########################################
    for file in files_in_corpus :
        path_file = os.path.join(path_to_corpus, file)
        distribution_mots_txt = du_texte_a_sa_premiere_distribution(path_file)

        ecrire_distribution_mot_texte_dans_2_distri(file, path_to_corpus, path_to_corpus_stat_folder, distribution_mots_txt)

        # ECRIRE LA DISTRIBUTION DU TEXTE
        # ...............................
        # print('+++++ Création du fichier : ' , file[:-4] + '_2_distributions.txt')
        # try :
        #     path_file = os.path.join(path_to_corpus, file)
        #     nom_fichier_distri_texte = path_to_corpus_stat_folder+file[:-4]+'_2_distributions.txt'
        #     with codecs.open(nom_fichier_distri_texte, mode='a', encoding='utf8') as file_distro_file :

        #         file_distro_file.write('\n\n{}\n{} FICHIER CONTENANT LA DISTRIBUTION DES MOTS DU TEXTE : \n\t\t {} {}\n{}'.format('='*80 , '='*10 , file , '='*10 , '='*80))

        #         file_distro_file.write('\n\n{}\n{} PRESENTATION {}\n{}\n\n'.format('='*30 , '='*7 , '='*7 , '='*30))

        #         for word, number in distribution_mots_txt.items():
        #             file_distro_file.write('{} : {}\n'.format(word, number))

        #         #file_stat_file.write('\n\nLe texte {} contient {} lignes.'.format(file, 'xxx'))
        # except :
        #     print('\tPROBLEME LORS DE LA CREATION DU FICHIER.')
        # else :
        #     print('\tCréation du fichier réussi.')

        #UPDATE DICO CORPUS
        #dico_distribution_mots_corpus = stats_0_distributions.wordsDistributionUpdate_dict_from_list(liste_2)

    # ECRIRE LA DISTRIBUTION DU CORPUS
    # ...............................

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
