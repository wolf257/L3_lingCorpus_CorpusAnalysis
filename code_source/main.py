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

dossier_base_projet = PROJECT_ROOT
dossier_corpus_litterature = CORPUS_LITTERATURE
dossier_corpus_professeur = CORPUS_PROFESSEUR

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

            start = time.time()

            ##########################
            # EXECUTION
            ##########################

            liste_corpus = []
            liste_corpus.append(dossier_corpus_professeur)
            liste_corpus.append(dossier_corpus_litterature)

            others.conversion_pdf_to_text(dossier_corpus_professeur)

            for corpus in liste_corpus :
               big_process.tour_du_corpus(corpus)
               big_process.tour_des_fichiers(corpus)

            if a.strip() == '1' :
                for corpus in liste_corpus:
                    big_process.generation_corpus_xml(corpus, 'light')
            elif a.strip() == '2' :
                for corpus in liste_corpus:
                    big_process.generation_corpus_xml(corpus, 'complet')

            big_process.creer_et_remplir_fichier_synthese_xml(dossier_base_projet, liste_corpus)
            big_process.creer_et_remplir_fichier_dtd(dossier_base_projet)
            big_process.generation_et_execution_script_bash_validation_dtd(dossier_base_projet)

            ###########################
            # CALCUL TPS EXECUTION
            ##########################
            end = time.time()

            tps_ecoule_sec = end - start
            tps_ecoule_min = 0
            tps_ecoule_h = 0

            if tps_ecoule_sec > 60 :
                tps_ecoule_min = int(tps_ecoule_sec / 60)
                tps_ecoule_sec = int(tps_ecoule_sec % 60)
                if tps_ecoule_min > 60 :
                    tps_ecoule_h = int(tps_ecoule_min /60)
                    tps_ecoule_min = int(tps_ecoule_min % 60)

            print('\n\n===Toute l\'éxecution a pris : {} h {} min {} sec\n\n'.format(tps_ecoule_h, tps_ecoule_min, tps_ecoule_sec))
            ##########################

            break

        #==================================
        elif a.strip() == '' :
            print("\n-----------------------------------")
            print("Vous nous quittez déjà ! Au revoir.")
            print("-----------------------------------\n")

            break

        #==================================
        else :
            print("\n---------------------------------------------------------------------")
            print("Désolé, je n'ai pas compris votre instruction. (Retournons au début.)")
            print("-----------------------------------------------------------------------")


if __name__ == '__main__':
    main()
