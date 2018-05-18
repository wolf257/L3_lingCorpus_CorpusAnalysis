#!/usr/bin/env python3
#-*- coding : utf8 -*-

## NOTE : Ne surtout pas déplacer ce fichier !! Sinon tous les paths changeront !!

import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__ + "/../../"))
CURRENT_ROOT = os.path.abspath(os.path.dirname(__file__))
CORPUS_PROFESSEUR = os.path.join(PROJECT_ROOT, 'corpus_professeur/')
CORPUS_LITTERATURE = os.path.join(PROJECT_ROOT, 'corpus_litterature/')
MORPHALOU_ROOT = os.path.join(PROJECT_ROOT, 'morphalou/')
RESULT_RAPPORT_ROOT = os.path.join(PROJECT_ROOT, 'resultats_et_rapport/')
TREETAGGER_ROOT = os.path.join(PROJECT_ROOT, 'from_outside_treetagger/')

def main():
    print(PROJECT_ROOT) #nous donne la base du dossier
    print(CURRENT_ROOT)
    print(CORPUS_PROFESSEUR)
    print(CORPUS_LITTERATURE)
    print(MORPHALOU_ROOT)
    print(RESULT_RAPPORT_ROOT)

if __name__ == '__main__':
    main()
