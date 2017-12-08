#!/usr/bin/env python3
#-*- coding : utf8 -*-

import os
import re
import random
import treetaggerwrapper
import pprint
import io
import codecs

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

def main():
    while 1 :
        a = input("\n===Level 0 : Bonjour, et bienvenue." + \
            "\n Que voulez-vous faire :" +\
            "\n 1 : Suivre la procédure 'normale' " + \
            "\n 2 : Choice 2" + \
            "\n (enter) - Exit" + \
            "\nYour choice : ")

        #==================================
        if a.strip() == '1' :
            print("Choix 1.")
            #E1 : conversion des cours en txt
            #others.conversion_pdf_to_text(dossier_corpus_professeur)

            big_process.tour_du_corpus(dossier_corpus_litterature)

            break
        #==================================
        elif a.strip() == '2' :
            print("Choix 2.")
            break #continue pour revenir

        #==================================
        elif a.strip() == '' :
            print("\n+++++++++++++++++++++++++++++")
            print("Thank you ! Bye.")
            print("+++++++++++++++++++++++++++++\n")

            break

        #==================================
        else :
            print("\n-----------------------------------")
            print("Désolé, je n'ai pas compris votre instruction. (Retournons au début.)")
            print("-----------------------------------")


if __name__ == '__main__':
    main()
