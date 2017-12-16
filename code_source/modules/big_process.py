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

dossier_morphalou = MORPHALO_ROOT

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
    nom_fichier_stats_corpus = path_to_corpus_stat_folder + '0_stats_de_' + nom_corpus + '.txt'
    nom_fichier_distribution_corpus = path_to_corpus_stat_folder + '1_distribution_de_' + nom_corpus + '.txt'

    files_in_corpus = None
    files_in_corpus = others.list_text_in_folder_as_list(path_to_corpus)

    dico_distribution_mots_corpus = {}
    ts_text_in_one_string = []

    nb_mots_corpus = 0
    nb_phrases = 0

    for file in files_in_corpus :
        #VAR
        path_file = os.path.join(path_to_corpus, file)

        ###################################
        #CREATION LISTE À EXPLOITER
        liste_exploitable_txt = ponctuation_texte.du_texte_a_sa_liste_exploitable_par_word_distribution(path_file)
        ###################################

        nb_mots_corpus += len(liste_exploitable_txt)

        for word in liste_exploitable_txt :
            if word == '.' or word == '?' or word == '!' :
                nb_phrases += 1

        ts_text_in_one_string += liste_exploitable_txt

    distribution_mots_corpus = stats_0_distributions.wordsDistributionUpdate_dict_from_list(dico_distribution_mots_corpus, ts_text_in_one_string)

    writing_in_files.remplissage_stat_corpus(nom_fichier_stats_corpus, nom_corpus, files_in_corpus, nb_mots_corpus, nb_phrases)

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

        nb_mots_texte = len(liste_exploitable_txt)
        nb_phrases = 0

        for word in liste_exploitable_txt :
            if word == '.' or word == '?' or word == '!' :
                nb_phrases += 1

        distribution_mots_txt = stats_0_distributions.wordsDistribution_dict_from_list(liste_exploitable_txt)

        writing_in_files.remplissage_stat_texte(file, path_to_corpus, path_to_corpus_stat_folder, nb_mots_texte, nb_phrases)

        writing_in_files.ecrire_distribution_mot_texte(file, path_to_corpus, path_to_corpus_stat_folder, distribution_mots_txt)

    print('\n++++++++++++++++++++++++++++++++++++++++++++++++++')

##############################################################
# Fonction : generation_corpus_xml
# Input :
##############################################################

def generation_corpus_xml(path_to_corpus, version='light'):
    #VAR
    dico_tag_corpus = defaultdict(lambda: defaultdict(dict))
    file_morphalou = others.load_morphalou(dossier_morphalou)

    nom_corpus = os.path.basename(os.path.normpath(path_to_corpus))

    if nom_corpus == 'corpus_litterature' :
        num_corpus = 1
    else :
        num_corpus = 2

    #VAR
    reference_corpus = 'c'+str(num_corpus)

    print('++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n++ Nous allons tagger et recupérer les mots du corpus {}. \n Souhaitez-nous bonne chance'.format(nom_corpus))

    #CREATION DOSSIER TAG a la RACINE DU CORPUS
    #others.creation_folder(path_to_corpus, 'tag')
    #CREATION DOSSIER XML a la RACINE DU CORPUS
    others.creation_folder(path_to_corpus, 'xml')

    #VAR
    path_to_corpus_stat_folder = path_to_corpus+'statistiques/'
    #path_to_corpus_donnee_tag_folder = path_to_corpus+'tag/'

    path_to_corpus_xml_folder = path_to_corpus+'xml/'
    nom_fichier_xml_corpus = path_to_corpus_xml_folder + 'rendu_de_' + nom_corpus + '.xml'

    #XML : balise <corpus type_corpus='valeur'>
    writing_in_files.ecrire_xml_balise_ouvrante(nom_fichier_xml_corpus, 'corpus', 1, 'type_corpus', nom_corpus)

    files_in_corpus = None
    files_in_corpus = others.list_text_in_folder_as_list(path_to_corpus)

    #nom_fichier_donner_tag_corpus = path_to_corpus_stat_folder + '0_stats_de_' + nom_corpus + '.txt'
    nom_fichier_distribution_corpus ='1_distribution_de_' + nom_corpus + '.txt'
    path_fichier_distribution_corpus = os.path.join(path_to_corpus_stat_folder, nom_fichier_distribution_corpus )
    liste_fichier_distribution_corpus = others.import_distribution_as_list(path_fichier_distribution_corpus)

    nom_fichier_stats_corpus = path_to_corpus_stat_folder + '0_stats_de_' + nom_corpus + '.txt'
    nb_mots_corpus, nb_phrases_corpus, nb_moyen_mots_par_phrase_corpus = others.recherche_stats_base_texte(nom_fichier_stats_corpus)

    #######
    # Niveau des textes
    ######

    text_for_tagg = []

    for file in files_in_corpus:
        path_file = os.path.join(path_to_corpus, file)

        nom_fichier_distribution_texte = file[:-4] + '_2_distributions.txt'
        path_fichier_distribution_texte = os.path.join(path_to_corpus_stat_folder, nom_fichier_distribution_texte)
        liste_fichier_distribution_texte = others.import_distribution_as_list(path_fichier_distribution_texte)

        nom_fichier_stats_texte = path_to_corpus_stat_folder+file[:-4]+'_1_stats.txt'
        nb_mots_texte, nb_phrases_texte, nb_moyen_mots_par_phrase_texte = others.recherche_stats_base_texte(nom_fichier_stats_texte)
        print('{}, {}, {}'.format(nb_mots_texte, nb_phrases_texte, nb_moyen_mots_par_phrase_texte))

        num_texte = int(files_in_corpus.index(file))
        reference_texte = 'c'+str(num_corpus)+'t'+str(num_texte)

        #XML : balise <text text_id=CxTx>
        writing_in_files.ecrire_xml_balise_ouvrante(nom_fichier_xml_corpus, 'text', 2, 'text_id', reference_texte)

        ###################################
        #CREATION LISTE À EXPLOITER
        text_for_tagg = ponctuation_texte.du_texte_a_sa_liste_exploitable_par_tagging(path_file)
        ###################################

        compteur_ligne = 0
        nb_lignes_in_texte = len(text_for_tagg)
        nb_lignes_a_traiter = 0

        if version == 'complet' :
            nb_lignes_a_traiter = nb_lignes_in_texte
        else :
            nb_lignes_a_traiter = 1

        while compteur_ligne < nb_lignes_a_traiter :
            num_line = compteur_ligne
            line = text_for_tagg[compteur_ligne]

            reference_line = 'c'+str(num_corpus)+'t'+str(num_texte)+'s'+str(num_line)

            #XML : balise <sentence sentence_id=CxTxSx>
            writing_in_files.ecrire_xml_balise_ouvrante(nom_fichier_xml_corpus, 'sentence', 3, 'sentence_id', reference_line)

            print('\n\n{}'.format('='*35))
            print('***Ref ligne : {}'.format(reference_line))
            print('***Contenu : {}'.format(line))

            #ON tagge ln/ln et on ajoute le resultat à notre dico
            # tagging.tagger_phrase_et_ajouter_au_dict_ref_to_word(dico_tag_corpus, line, liste_fichier_distribution_corpus, liste_fichier_distribution_texte, file_morphalou, num_corpus, num_texte, num_line)

            tagging.tagger_phrase_et_ajouter_au_texte_ref_to_word(line, nom_fichier_xml_corpus, liste_fichier_distribution_corpus, liste_fichier_distribution_texte, file_morphalou, num_corpus, num_texte, num_line, nb_mots_corpus, nb_mots_texte)

            writing_in_files.ecrire_xml_balise_fermante(nom_fichier_xml_corpus, 'sentence', 3)

            compteur_ligne +=1

        writing_in_files.ecrire_xml_balise_fermante(nom_fichier_xml_corpus, 'text', 2)

    writing_in_files.ecrire_xml_balise_fermante(nom_fichier_xml_corpus, 'corpus', 1)

def synthese_xml(path_to_corpus1, path_to_corpus2) :
    pass
