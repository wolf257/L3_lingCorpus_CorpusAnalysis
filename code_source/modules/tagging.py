#!/usr/bin/env python3
#-*- coding : utf-8 -*-


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     PRESENTATION DU MODULE :
#          Ce modules rassemble les functions de
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

########################################################
# LIST FUNCTIONS IN MODULES
#	+ tagger_phrase_et_ajouter_au_dict_ref_to_word()
#	+
#	+
########################################################

import os, re, random

import treetaggerwrapper
import pprint , io

from collections import defaultdict

import modules.others as others
import modules.writing_in_files as writing_in_files

# Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_PROFESSEUR, CORPUS_LITTERATURE, MORPHALO_ROOT, RESULT_RAPPORT_ROOT, TREETAGGER_ROOT
###################################################################################

folder_treetagger = TREETAGGER_ROOT

# Construction et configuration du wrapper
tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr', TAGINENC='utf-8' , TAGOUTENC='utf-8' , TAGDIR=folder_treetagger)


##############################################################
# Fonction : tagger_phrase_et_ajouter_au_dict_ref_to_word()
##############################################################
def tagger_phrase_et_ajouter_au_dict_ref_to_word(dico_tag_corpus, phrase_to_tag,
                                                obj_file_distribution_corpus, obj_file_distribution_texte,
                                                 file_morphalou,
                                                 num_corpus='num_corpus_NR', num_texte='num_texte_NR',
                                                 num_phrase='num_phrase_NR') :

    #TAGGER LA PHRASE
    tags = tagger.TagText(phrase_to_tag)
    tags2 = treetaggerwrapper.make_tags(tags)

    #print('Le tagging donne : ')
    #pprint.pprint(tags2)

    # VAR
    compteur_mot = 0
    nb_mots_dans_phrase = len(tags2)
    mondico = defaultdict(lambda: defaultdict(dict))

    while compteur_mot < nb_mots_dans_phrase :
        #num_mot = tags2.index(line_word)
        num_mot = compteur_mot
        # Ref : Cx Tx Sx Wx
        reference_mot = 'c'+str(num_corpus)+'t'+str(num_texte)+'s'+str(num_phrase)+'w'+str(num_mot)

        #print(reference_mot)

        # RECUPERATION DES INFOS
        try :
            mot_forme = tags2[num_mot][0]
        except :
            mot_forme = 'forme_NR'
        try :
            mot_pos_treetagger = tags2[num_mot][1]
        except :
            mot_pos_treetagger = 'POS_NR'
        try :
            mot_lemme = tags2[num_mot][2]
        except :
            mot_lemme = 'lemme_NR'

        #RECHERCHE DES OCCURENCES
        try :
            mot_occurrence_texte = others.recherche_occurence_mot_in_file_distribution(obj_file_distribution_texte, mot_forme)
        except :
            mot_occurrence_texte = 'occurrence_texte_NR'

        try :
            mot_occurrence_corpus = others.recherche_occurence_mot_in_file_distribution(obj_file_distribution_corpus, mot_forme)
        except :
             mot_occurrence_corpus = 'occurence_corpus_NR'

        if isinstance(mot_occurrence_corpus, int) and (isinstance(mot_occurrence_corpus, int) and int(mot_occurrence_corpus != 0 )) :
            mot_frequence_corpus = int(mot_occurrence_texte) / int(mot_occurrence_corpus)
        else :
            mot_frequence_corpus = 'Freq non calculable'

        if isinstance(mot_occurrence_texte, int) and (isinstance(mot_occurrence_texte, int) and int(mot_occurrence_texte != 0 )) :
            mot_frequence_texte = int(mot_occurrence_texte) / int(mot_occurrence_texte)
        else :
            mot_frequence_texte = 'Freq non calculable'

        # TEST
        print('\nTEST : La ref \'{}\' pointe vers le mot \'{}\', lemme \'{}\', Pos \'{}\'.'.format(reference_mot, mot_forme, mot_lemme, mot_pos_treetagger))
        print('OT : {} et OC : {}'.format(mot_occurrence_texte, mot_occurrence_corpus))

        # RECHERCHE IN MORPHALO
        #VAR
        #mot_cherche = mot_forme
        mot_cherche = mot_lemme
        list_formSet = file_morphalou

        mot_POS_morphalou = []
        mot_genre_morphalou = []
        mot_nombre_morphalou = []

        for item in list_formSet :

            # mot_POS_morphalou = []
            # mot_genre_morphalou = []
            # mot_nombre_morphalou = []

            if item[0][0].text  == mot_cherche :
                #mot = item[0][0].text
                #print('Mot : {}'.format(mot))

                # POS_morphalou
                try :
                    POS_morphalou = item[0][1].text
                    #print('POS : {}'.format(POS))
                except :
                    pass
                    #mot_POS_morphalou.append('POS_NR_morphalou')
                else :
                    mot_POS_morphalou.append(str(POS_morphalou))

                #Genre Morphalou
                try :
                    genre_morphalou = item[0][2].text
                except :
                    pass
                    #mot_genre_morphalou.append('Genre_NR_morphalou')
                else :
                    mot_genre_morphalou.append(str(genre_morphalou))
                    #print('Genre : {}'.format(genre))

                #Nombre_morphalou
                try :
                    nombre_morphalou = item[1][1].text
                except :
                    pass
                    #mot_nombre_morphalou.append('Nombre_NR_morphalou')
                else :
                    mot_nombre_morphalou.append(str(nombre_morphalou))
                    #print('Nombre : {}\n\n'.format(nombre_morphalou))

        #print('Notre recherche morphalou donne : POS \'{}\', genre \'{}\' et nombre \'{}\'.'.format(mot_POS_morphalou, mot_genre_morphalou, mot_nombre_morphalou))

        #dico_tag_corpus[reference_mot]['reference']['corpus'] = corpus
        #dico_tag_corpus[reference_mot]['reference']['texte'] = nom_texte
        #dico_tag_corpus[reference_mot]['reference']['phrase'] = num_phrase
        #dico_tag_corpus[reference_mot]['reference']['mot'] = num_mot

        dico_tag_corpus[reference_mot]['morphology']['lemme'] = mot_lemme
        dico_tag_corpus[reference_mot]['morphology']['forme'] = mot_forme

        dico_tag_corpus[reference_mot]['morphology']['pos_treetagger'] = mot_pos_treetagger
        dico_tag_corpus[reference_mot]['morphology']['pos_morphalou'] = mot_POS_morphalou
        dico_tag_corpus[reference_mot]['morphology']['genre'] = mot_genre_morphalou
        dico_tag_corpus[reference_mot]['morphology']['nombre'] = mot_nombre_morphalou

        dico_tag_corpus[reference_mot]['statistics']['apparition_in_text'] = mot_occurrence_texte
        dico_tag_corpus[reference_mot]['statistics']['apparition_in_corpus'] = mot_occurrence_corpus

        #Calculer les nbres totaux
        #dico_tag_corpus[reference_mot]['statistics']['frequence_in_text'] = mot_frequence_texte
        #dico_tag_corpus[reference_mot]['statistics']['frequence_in_corpus'] = mot_frequence_corpus

        compteur_mot += 1

    return dico_tag_corpus

##############################################################
# Fonction : tagger_phrase_et_ajouter_au_texte_ref_to_word()
##############################################################
def tagger_phrase_et_ajouter_au_texte_ref_to_word(phrase_to_tag, path_to_file_xml,
                                                obj_file_distribution_corpus, obj_file_distribution_texte,
                                                 file_morphalou,
                                                 num_corpus='num_corpus_NR', num_texte='num_texte_NR',
                                                  num_phrase='num_phrase_NR',
                                                  nb_mots_file=0, nb_mots_corpus=0) :

    dico_tag_phrase = defaultdict(lambda: defaultdict(dict))
    fichier_xml = path_to_file_xml

    #TAGGER LA PHRASE
    tags = tagger.TagText(phrase_to_tag)
    tags2 = treetaggerwrapper.make_tags(tags)

    # VAR
    compteur_mot = 0
    nb_mots_dans_phrase = len(tags2)
    mondico = defaultdict(lambda: defaultdict(dict))

    while compteur_mot < nb_mots_dans_phrase :
        #num_mot = tags2.index(line_word)
        num_mot = compteur_mot
        # Ref : Cx Tx Sx Wx
        reference_mot = 'c'+str(num_corpus)+'t'+str(num_texte)+'s'+str(num_phrase)+'w'+str(num_mot)

        #print(reference_mot)

        # RECUPERATION DES INFOS
        try :
            mot_forme = tags2[num_mot][0]
        except :
            mot_forme = 'forme_NR'

        if mot_forme.endswith("'") :
            mot_forme = str(mot_forme[:-1])
        elif mot_forme == '&' :
            mot_forme = '&amp;'
        elif mot_forme == '<' :
            mot_forme = '&lt;'
        elif mot_forme == '>' :
            mot_forme = '&gt;'
        elif mot_forme == '"' :
            mot_forme = '&quot;'
        elif mot_forme == '\'' :
            mot_forme = '&apos;'

        try :
            mot_pos_treetagger = tags2[num_mot][1]
        except :
            mot_pos_treetagger = 'POS_NR'
        try :
            mot_lemme = tags2[num_mot][2]
        except :
            mot_lemme = 'lemme_NR'

        #RECHERCHE DES OCCURENCES
        try :
            mot_occurrence_texte = others.recherche_occurence_mot_in_file_distribution(obj_file_distribution_texte, mot_forme)
        except :
            mot_occurrence_texte = 'occurrence_texte_NR'

        try :
            mot_occurrence_corpus = others.recherche_occurence_mot_in_file_distribution(obj_file_distribution_corpus, mot_forme)
        except :
             mot_occurrence_corpus = 'occurence_corpus_NR'

        if isinstance(mot_occurrence_texte, int) and (isinstance(nb_mots_file, int)) and int((nb_mots_file != 0 )) :
            mot_frequence_texte = int(mot_occurrence_texte) / int(nb_mots_file)
        else :
            mot_frequence_texte = 'Frequence non calculable'


        if isinstance(mot_occurrence_corpus, int) and (isinstance(nb_mots_corpus, int)) and int((nb_mots_corpus != 0 )) :
            mot_frequence_corpus = int(mot_occurrence_corpus) / int(nb_mots_corpus)
        else :
            mot_frequence_corpus = 'Frequence non calculable'


        # TEST
        #print('\nTEST : La ref \'{}\' pointe vers le mot \'{}\', lemme \'{}\', Pos \'{}\'.'.format(reference_mot, mot_forme, mot_lemme, mot_pos_treetagger))
        #print('OT : {} et OC : {}'.format(mot_occurrence_texte, mot_occurrence_corpus))

        # RECHERCHE IN MORPHALO
        #VAR
        #mot_cherche = mot_forme
        mot_cherche = mot_lemme
        list_formSet = file_morphalou

        mot_POS_morphalou = []
        mot_genre_morphalou = []
        mot_nombre_morphalou = []

        for item in list_formSet :
            if item[0][0].text  == mot_cherche :
                #mot = item[0][0].text
                #print('Mot : {}'.format(mot))

                # POS_morphalou
                try :
                    POS_morphalou = item[0][1].text
                    #print('POS : {}'.format(POS))
                except :
                    pass
                    #mot_POS_morphalou.append('POS_NR_morphalou')
                else :
                    mot_POS_morphalou.append(str(POS_morphalou))

                #Genre Morphalou
                try :
                    genre_morphalou = item[0][2].text
                except :
                    pass
                    #mot_genre_morphalou.append('Genre_NR_morphalou')
                else :
                    mot_genre_morphalou.append(str(genre_morphalou))
                    #print('Genre : {}'.format(genre))

                #Nombre_morphalou
                try :
                    nombre_morphalou = item[1][1].text
                except :
                    pass
                    #mot_nombre_morphalou.append('Nombre_NR_morphalou')
                else :
                    mot_nombre_morphalou.append(str(nombre_morphalou))
                    #print('Nombre : {}\n\n'.format(nombre_morphalou))

        #print('Notre recherche morphalou donne : POS \'{}\', genre \'{}\' et nombre \'{}\'.'.format(mot_POS_morphalou, mot_genre_morphalou, mot_nombre_morphalou))

        try :
            #NIVEAU 4
            writing_in_files.ecrire_xml_balise_ouvrante(fichier_xml, 'word', 4, 'word_id', reference_mot, 'word_form', mot_forme)

            #NIVEAU 5
            writing_in_files.ecrire_xml_balise_ouvrante(fichier_xml, 'morphology', 5)

            #NIVEAU 6
            writing_in_files.ecrire_xml_balise_ouvrante(fichier_xml, 'lemme', 6)
            writing_in_files.ecrire_xml_contenu(fichier_xml, mot_lemme, 7)
            writing_in_files.ecrire_xml_balise_fermante(fichier_xml, 'lemme', 6)

            writing_in_files.ecrire_xml_balise_ouvrante(fichier_xml, 'POS_treetagger', 6)
            writing_in_files.ecrire_xml_contenu(fichier_xml , mot_pos_treetagger, 7)
            writing_in_files.ecrire_xml_balise_fermante(fichier_xml, 'POS_treetagger', 6)

            if len(mot_POS_morphalou) :
                writing_in_files.ecrire_xml_balise_ouvrante(fichier_xml, 'POS_morphalou', 6)
                writing_in_files.ecrire_xml_contenu(fichier_xml , mot_POS_morphalou, 7)
                writing_in_files.ecrire_xml_balise_fermante(fichier_xml, 'POS_morphalou', 6)

            if len(mot_genre_morphalou) :
                writing_in_files.ecrire_xml_balise_ouvrante(fichier_xml, 'genre', 6)
                writing_in_files.ecrire_xml_contenu(fichier_xml , mot_genre_morphalou, 7)
                writing_in_files.ecrire_xml_balise_fermante(fichier_xml, 'genre', 6)

            if len(mot_nombre_morphalou) :
                writing_in_files.ecrire_xml_balise_ouvrante(fichier_xml, 'nombre', 6)
                writing_in_files.ecrire_xml_contenu(fichier_xml , mot_nombre_morphalou, 7)
                writing_in_files.ecrire_xml_balise_fermante(fichier_xml, 'nombre', 6)

            writing_in_files.ecrire_xml_balise_fermante(fichier_xml, 'morphology', 5)

            #NIVEAU 5
            writing_in_files.ecrire_xml_balise_ouvrante(fichier_xml, 'statistics', 5)

            #NIVEAU 6
            writing_in_files.ecrire_xml_balise_ouvrante(fichier_xml, 'nb_apparition_text', 6)
            writing_in_files.ecrire_xml_contenu(fichier_xml , mot_occurrence_texte, 7)
            writing_in_files.ecrire_xml_balise_fermante(fichier_xml, 'nb_apparition_text', 6)

            writing_in_files.ecrire_xml_balise_ouvrante(fichier_xml, 'nb_apparition_corpus', 6)
            writing_in_files.ecrire_xml_contenu(fichier_xml , mot_occurrence_corpus, 7)
            writing_in_files.ecrire_xml_balise_fermante(fichier_xml, 'nb_apparition_corpus', 6)

            writing_in_files.ecrire_xml_balise_ouvrante(fichier_xml, 'frequence_in_text', 6)
            writing_in_files.ecrire_xml_contenu(fichier_xml ,mot_frequence_texte, 7)
            writing_in_files.ecrire_xml_balise_fermante(fichier_xml, 'frequence_in_text', 6)


            writing_in_files.ecrire_xml_balise_ouvrante(fichier_xml, 'frequence_in_corpus', 6)
            writing_in_files.ecrire_xml_contenu(fichier_xml ,mot_frequence_corpus, 7)
            writing_in_files.ecrire_xml_balise_fermante(fichier_xml, 'frequence_in_corpus', 6)


            writing_in_files.ecrire_xml_balise_fermante(fichier_xml, 'statistics', 5)

            writing_in_files.ecrire_xml_balise_fermante(fichier_xml, 'word', 4)
        except :
            print('\n\tL\'ajout du mot {} a rencontré un problème.'.format(reference_mot))
        else :
            print('\n\tLe mot {} a été ajouté au fichier xml.'.format(reference_mot))

        compteur_mot += 1
