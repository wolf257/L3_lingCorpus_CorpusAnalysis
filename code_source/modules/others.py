#!/usr/bin/env python3
#-*- coding : utf8 -*-


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     PRESENTATION DU MODULE :
#          Ce modules contient toutes les autres fonctions,
#          celle d'importation, les recherches, les créations de dossier,
#          ainsi que l'exécution de scripts bash.
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

########################################################
# LIST FUNCTIONS IN MODULES
#
#       + conversion_pdf_to_text()
#       + creation_folder()
#       + load_morphalou()
#
#	+ list_text_in_folder_as_list() + test
#
#	+ import_text_as_one_string() + test
#	+ import_text_as_list_of_strings() + test (obsolete)
#	+ import_text_as_list_of_words() + test (obsolete)
#
#	+ import_distribution_as_list()
#
#	+ recherche_occurence_mot_in_file_distribution()
#	+ recherche_stats_base_texte()
#
########################################################

import os
import re
import sys
import io
import codecs
import subprocess
import time
import codecs

from lxml import etree

# Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_PROFESSEUR, CORPUS_LITTERATURE, MORPHALOU_ROOT, RESULT_RAPPORT_ROOT, TREETAGGER_ROOT
###################################################################################

#dossier_morphalou = MORPHALOU_ROOT

##############################################################
# Fonction : conversion_pdf_to_text
##############################################################
def conversion_pdf_to_text(path_to_file, name_script_bash='convert.sh'):
    print('LANCEMENT DU SCRIPT : ' , name_script_bash , ' .' )
    subprocess.call(path_to_file+name_script_bash, shell=True, cwd=path_to_file)
    print('FIN DU SCRIPT')

##############################################################
# Fonction : creation_folder
##############################################################
def creation_folder(path_to_parent, name_folder):
    print('\n+++ Création du dossier : ' , name_folder)
    try :
        if not os.path.exists(path_to_parent + name_folder + '/') :
            os.makedirs(path_to_parent + name_folder + '/')
    except :
        print('\tPROBLEME LORS DE LA CREATION DU DOSSIER.')
    else :
        print('\tCréation du dossier réussi.')

##############################################################
# Fonction : load_morphalou()
##############################################################
def load_morphalou(dossier_morphalou):
    print('++ Je suis en train d\'ouvrir morphalou. Cela peut me prendre quelques secondes.')
    start = time.time()
    path_to_morphalou = os.path.join(dossier_morphalou, 'morphalou-2.0.xml')

    try :
        doc = etree.parse(path_to_morphalou)
    except:
        print('\tJe n\'ai pas pu ouvrir morphalou. Veuillez voir ma definition dans : \n\t\tmodules/others ouvrir_morphalou()')
        end = time.time()
    else :
        print('\tOuverture et chargement réussis.')
        end = time.time()

    tps_ecoule = end - start
    tps_ecoule = str(tps_ecoule)

    print('\tCela a pris {} secondes'.format(tps_ecoule[:4]))

    liste_formSet = doc.xpath('lexicalEntry/formSet')

    return liste_formSet

##############################################################
# Fonction : list_text_in_folder_as_list
# Input : text
# Return : list
##############################################################
def list_text_in_folder_as_list(path_to_folder):
    ''' Import the content of a folder as one list '''

    liste_finale = []

    for fichier in os.listdir(path_to_folder) :
        if fichier.endswith('.txt') :
            liste_finale.append(fichier)

    return liste_finale

##############################################################
# Fonction : import_text_as_one_string
# Input : path_to_text
# Return : string
##############################################################
def import_text_as_one_string(path_to_text):
    ''' Import a text as one string '''

    liste_brute = []
    liste_finale = []
    string_from_text = ''

    #list of all lines (not sentences) (from beg to EOL)
    # [l1 , l2 , l3 , ...]
    with codecs.open(path_to_text, mode = 'r', encoding='utf8') as file :
        liste_brute = file.readlines()

    #enlevons les \n \r ...
    for string in liste_brute :
            liste_finale.append(string.strip())


    string_from_text = ' '.join(liste_finale)
    # " l1 ' ' l2 ' ' l3 ' ' ... "

    return string_from_text

##############################################################
# Fonction : import_text_as_list_of_words
# Input : text
# Return : list
##############################################################
def import_text_as_list_of_strings(path_to_text):
    ''' Import a text as one list of strings '''

    liste_brute = []
    liste_finale = []

    with open(path_to_text, 'rt', encoding='utf8') as file :
        liste_brute = file.readlines()
        #list of all lines (from beg to EOL)

    for string in liste_brute :
            liste_finale.append(string.strip())

    return liste_finale

##############################################################
# Fonction : import_text_as_list_of_words
# Input : text
# Return : list
##############################################################
def import_text_as_list_of_words(path_to_text):
    ''' Import a text as one list of words '''

    liste_brute = []
    liste_finale = []

    with open(path_to_text, 'r', encoding='utf8') as file :
        liste_brute = file.readlines()
        #list of all lines (from beg to EOL)

    #MOT PAR MOT
    for elt in liste_brute :
        word = re.findall(r"[\w']+|[.,!?;]" , elt)

        liste_finale.append(word) #will give a nested list

    #to make the list flat
    liste_finale = [item for items in liste_finale for item in items]

    return liste_finale

##############################################################
# Fonction : import_distribution_as_list
# Input :
# Return :
##############################################################
def import_distribution_as_list(path_to_file) :
    try :
        f = codecs.open(path_to_file, mode='r', encoding='utf8')
    except :
        print('\nProblème lors de l\'ouverture du fichier.')
    else :
        #print('\nFichier distribution ouvert.')
        pass

        try :
            g = f.readlines()
        except :
            print('\nProblème lors de l\'importation du fichier.')
        else :
            #print('\nFichier distribution importé')
            f.close()
            return g


##############################################################
# Fonction : recherche_occurence_mot_in_file_distribution
# Input :
# Return :
##############################################################

def recherche_occurence_mot_in_file_distribution(file_or_list, mot_a_chercher) :
    #
    nb = 0
    #
    i = re.compile(r'^'+mot_a_chercher+' : (\d+)')
    for line in file_or_list :
        a_matcher = re.match(i , line)
        if a_matcher is None :
            pass
        else :
            nb += int(a_matcher.group(1))

    return nb

###############################################################
# Fonction : recherche_stats_base_texte()
# Input :
# Return :
##############################################################

def recherche_stats_base_texte(path_file) :
    try :
        file = codecs.open(path_file, mode='r', encoding='utf8')
    except :
        print('\tProblème ouverture.')
    else :
        #
        nb_mots_file, nb_phrases_file, nb_moyen_mots_par_phrase = 0, 0, 0
        resultats = []
        #

        i = re.compile(r'^(\d+) : (\d+) : (\d+\.\d+)')

        for line in file :
            a_matcher = re.match(i , line)
            if a_matcher is None :
                pass
            else :
                #print(a_matcher.group(0)) #le tout
                #print(a_matcher.group(1)) #le nb
                nb_mots_file += int(a_matcher.group(1))
                resultats.append(nb_mots_file)

                nb_phrases_file += int(a_matcher.group(2))
                resultats.append(nb_phrases_file)

                nb_moyen_mots_par_phrase += float(a_matcher.group(3))
                resultats.append(nb_moyen_mots_par_phrase)
                break

        file.close()

        return resultats

if __name__ == '__main__':
    pass
