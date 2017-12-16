#!/usr/bin/env python3
#-*- coding : utf8 -*-

import os
import re
import random
import treetaggerwrapper
import pprint
import io
import codecs
import time

from settings import PROJECT_ROOT
from collections import defaultdict

import modules.others as others
import modules.ponctuation_texte as ponctuation_texte
import modules.stats_1_base as stats_1_base
import modules.tagging as tagging
import modules.big_process as big_process

# Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_PROFESSEUR, CORPUS_LITTERATURE, MORPHALO_ROOT, RESULT_RAPPORT_ROOT, TREETAGGER_ROOT
###################################################################################

dossier_corpus_litterature = CORPUS_LITTERATURE
dossier_corpus_professeur = CORPUS_PROFESSEUR
#dossier_morphalou = MORPHALO_ROOT

def main():
    while 1 :
        a = input("\nBonjour, et bienvenue." + \
            "\n Que voulez-vous faire :" +\
            "\n 1 : Suivre la procédure 'light' " + \
            "\n 2 : Suivre la procédure 'compléte' " + \
            "\n (enter) - Exit" + \

            "\n\nNOTE EXPLICATIVE : " +\
            "\n\t- La version 'light' suit la procédure normale, sauf que le processus n'est appliqué qu'aux 10 premières phrases de chaque texte. Durée estimée : moins d'une heure." +\
            "\n\t- La version 'compléte' applique le processus à tout le corpus. Le temps d\'exécution risque de prendre plus de 24 heures." +\

            "\n\nQuel est votre choix : ")

        #==================================
        if a.strip() == '1' or a.strip() == '2' :
            if a.strip() == '1' :
                print("\n\nVous avez choisi la version 'light'. Bon choix.")
            elif a.strip() == '2' :
                print("\n\nVous avez choisi la version 'complete'. Bonne chance.")

            liste_corpus = []
            #liste_corpus.append(dossier_corpus_professeur)
            liste_corpus.append(dossier_corpus_litterature)

            #E1 : conversion des cours en txt
            #others.conversion_pdf_to_text(dossier_corpus_professeur)

            #start = time.time()
            #for corpus in liste_corpus :
            #    big_process.tour_du_corpus(corpus)
            #    big_process.tour_des_fichiers(corpus)

            if a.strip() == '1' :
                for corpus in liste_corpus:
                    big_process.generation_corpus_xml(corpus, 'light')
            elif a.strip() == '2' :
                for corpus in liste_corpus:
                    big_process.generation_corpus_xml(corpus, 'complet')

                #big_process.generation_corpus_xml(dossier_corpus_litterature, 'complet')

            #big_process.synthese_xml(dossier_corpus_professeur, dossier_corpus_litterature)

            #etape1 = time.time()
            #end1 = etape1 - start
            #end1 = str(end1)
            # try :
            #     print('\tCela a pris {} secondes'.format(end1[:4]))
            # except :
            #     print('Probleme de tps')

            #with open(CORPUS_LITTERATURE+'tag/resultat.txt', mode ='a') as file_tag :
            #    file_tag.write('\n\n\n{}'.format(dico1))

            # etape2 = time.time()

            # tps_ecoule = etape2 - start
            # tps_ecoule = str(tps_ecoule)

            # print('\tCela a pris en tout {} secondes'.format(tps_ecoule[:4]))
            #     #TODO

            #big_process.write_xml_dico_in_file(dico1 , file_xml)
            #d'abord texte_distri.xml (1)
            # puis le gros où l'on copie tous les petits


            #pprint.pprint(dico1)

            break

        #==================================
        elif a.strip() == '' :
            print("\n+++++++++++++++++++++++++++++")
            print("Vous nous quittez déjà ! Au revoir.")
            print("+++++++++++++++++++++++++++++\n")

            break

        #==================================
        else :
            print("\n---------------------------------------------------------------------")
            print("Désolé, je n'ai pas compris votre instruction. (Retournons au début.)")
            print("-----------------------------------------------------------------------")


if __name__ == '__main__':
    main()
