#!/usr/bin/env python3
#-*- coding : utf8 -*-

import os
import codecs

import modules.others as others

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     PRESENTATION DU MODULE :
#          Ce modules rassemble les functions de
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

########################################################
# LIST FUNCTIONS IN MODULES
#	+ remplissage_stat_corpus()
#	+ remplissage_stat_texte()
#	+ ecrire_distribution_mot_corpus()
#       + ecrire_distribution_mot_texte()
########################################################

##############################################################
# Fonction : remplissage_info_base_corpus
# - Crée le fichier  0_stats_du_corpus.tx
# - Inscrit le nombre de fichier
# - Ecrit une liste des fichiers
##############################################################
def remplissage_stat_corpus(nom_fichier_stats_corpus, nom_corpus, files_in_corpus, nb_mots_corpus, nb_phrases):
    print('\n++++ Création du fichier : 0_stats_du_corpus.txt')
    try :
        #OPEN FILE
        file_stat_corpus = codecs.open(nom_fichier_stats_corpus, mode='a', encoding='utf8')
    except :
        print('\tPROBLEME LORS DE LA CREATION DU FICHIER.')
    else :
        print('\tCréation du fichier réussi.')

        nb_mots_par_phrase = str(nb_mots_corpus / nb_phrases)[:5]

        try :
            # REMPLISSAGE FILE
            file_stat_corpus.write('\n\n{}\n{} FICHIER CONTENANT STATISTIQUES DE CORPUS {}\n{}'.format('='*60 , '='*10 , '='*10 , '='*60))

            file_stat_corpus.write('\n\n{}\n{} PRESENTATION {}\n{}'.format('='*30 , '='*7 , '='*7 , '='*30))

            file_stat_corpus.write('\n\nLe corpus {} contient {} fichiers txt  : '.format(nom_corpus , len(files_in_corpus)))

            for file in files_in_corpus :
                file_stat_corpus.write('\n - {}'.format(file))

            file_stat_corpus.write('\n\nNotre Corpus contient : ')
            file_stat_corpus.write('\n{} : {} : {}'.format(nb_mots_corpus, nb_phrases, nb_mots_par_phrase))

            file_stat_corpus.write('\n\n\n NOTICE (le numéro est celui du champ en cas de split(\':\') : ')
            file_stat_corpus.write('\n[0] {} : [1] {} : [2] {}'.format( 'Nombre de mots' , 'Nombre de phrases' , 'Nombre moyen de mots par phrase'))

        except :
            print('\t\tProblème lors du remplissage')
        else :
            print('\tRemplissage du fichier réussi.')
            #CLOSE FILE
            file_stat_corpus.close()
            print('\tFichier fermé\n')

##############################################################
# - ecrire_distribution_mot_corpus
##############################################################
def ecrire_distribution_mot_corpus(nom_fichier_distribution_corpus, path_to_corpus, distribution_mots_corpus):
    print('\n++++ Création du fichier : 1_distribution_mot_du_corpus.txt')
    try :
        #OPEN FILE
        file_distribution_corpus = codecs.open(nom_fichier_distribution_corpus, mode='a', encoding='utf8')
    except :
        print('\tPROBLEME LORS DE LA CREATION DU FICHIER.')
    else :
        print('\tCréation du fichier réussi.')

        try :
            # REMPLISSAGE FILE
            file_distribution_corpus.write('\n\n{}\n{} FICHIER CONTENANT LA DISTRIBUTION DES MOTS DE CORPUS {}\n{}\n\n'.format('='*60 , '='*10 , '='*10 , '='*60))

            #file_distribution_corpus.write('\n\n{}\n{} PRESENTATION {}\n{}'.format('='*30 , '='*7 , '='*7 , '='*30))

            #ECRITURE DES FREQUENCE
            for word, number in distribution_mots_corpus.items():
                file_distribution_corpus.write('{} : {}\n'.format(word, number))

        except :
            print('\t\tProblème lors du remplissage')
        else :
            print('\tRemplissage du fichier réussi.')
            #CLOSE FILE
            file_distribution_corpus.close()
            print('\tFichier fermé\n')

##############################################################
# Fonction : remplissage_info_base_text
##############################################################
def remplissage_stat_texte(file, path_to_corpus, path_to_corpus_stat_folder, nb_mots_texte, nb_phrases):


        nb_mots_texte = nb_mots_texte
        nb_phrases = nb_phrases
        nb_mots_par_phrase = str(nb_mots_texte / nb_phrases)[:5]

        print('\n++++ Création du fichier : ' , file[:-4]+'_1_stats.txt')
        try :
            path_file = os.path.join(path_to_corpus, file)
            nom_fichier_stats_texte = path_to_corpus_stat_folder+file[:-4]+'_1_stats.txt'

            file_stat_file = codecs.open(nom_fichier_stats_texte, mode='a', encoding='utf8')
        except :
            print('\tPROBLEME LORS DE LA CREATION DU FICHIER.')
        else :
            print('\tCréation du fichier réussi.')

            try :
                file_stat_file.write('\n\n{}\n{} FICHIER CONTENANT STATISTIQUES DU TEXTE : \n\t\t {} {}\n{}'.format('='*80 , '='*10 , file , '='*10 , '='*80))

                file_stat_file.write('\n\nNotre fichier contient : ')
                file_stat_file.write('\n{} : {} : {}'.format(nb_mots_texte, nb_phrases, nb_mots_par_phrase))

                file_stat_file.write('\n\n\n NOTICE (le numéro est celui du champ en cas de split(\':\') : ')
                file_stat_file.write('\n[0] {} : [1] {} : [2] {}'.format( 'Nombre de mots' , 'Nombre de phrases' , 'Nombre moyen de mots par phrase'))

            except :
                print('\tPROBLEME LORS DU REMPLISSAGE DU FICHIER.')
            else :
                print('\tRemplissage du fichier réussi.')
        print('\n')

##############################################################
# Fonction : ecrire_distribution_mot_texte
##############################################################
def ecrire_distribution_mot_texte(file, path_to_corpus, path_to_corpus_stat_folder, dico_distribution):
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
                file_distro_file.write('\n\n{}\n{} FICHIER CONTENANT LA DISTRIBUTION DES MOTS DU TEXTE : \n\t\t {} {}\n{}\n\n'.format('='*80 , '='*10 , file , '='*10 , '='*80))

                #file_distro_file.write('\n\n{}\n{} DISTRIBUTION {}\n{}\n\n'.format('='*30 , '='*7 , '='*7 , '='*30))

                #ECRITURE DES FREQUENCE
                for word, number in dico_distribution.items():
                    file_distro_file.write('{} : {}\n'.format(word, number))

            except :
                print('\tPROBLEME LORS DU REMPLISSAGE DU FICHIER.')
            else :
                print('\tRemplissage du fichier réussi.')
                file_distro_file.close()
                print('\tFichier fermé')

##############################################################
# Fonction : ecrire_xml_balise_ouvrante()
##############################################################
def ecrire_xml_balise_ouvrante(path_to_file_xml, tag, niveau=0, att1='', val1='', att2='', val2='', att3='', val3=''):
    with codecs.open(path_to_file_xml, mode='a', encoding='utf8') as file :
        if att1 != '' and att2 != '' and att3 != '':
            file.write('\n{}<{} {}=\'{}\' {}=\'{}\' {}=\'{}\'>'.format(' '*int(niveau)*3, tag, att1, val1, att2, val2, att3, val3))
        elif att1 != '' and att2 != '' and att3 == '':
            file.write('\n{}<{} {}=\'{}\' {}=\'{}\'>'.format(' '*int(niveau)*3, tag, att1, val1, att2, val2))
        elif att1 != '' and att2 == '' and att3 == '':
            file.write('\n{}<{} {}=\'{}\'>'.format(' '*int(niveau)*3, tag, att1, val1))
        elif att1 == '' and att2 == '' and att3 == '':
            file.write('\n{}<{}>'.format(' '*int(niveau)*3, tag))


##############################################################
# Fonction : ecrire_xml_balise_fermante()
##############################################################
def ecrire_xml_balise_fermante(path_to_file_xml, tag, niveau=0) :
    with codecs.open(path_to_file_xml, mode='a', encoding='utf8') as file :
        file.write('\n{}</{}>'.format(' '*int(niveau)*3, tag))

##############################################################
# Fonction : ecrire_xml_contenu_()
##############################################################
def ecrire_xml_contenu(path_to_file_xml, contenu, niveau=0) :
    with codecs.open(path_to_file_xml, mode='a', encoding='utf8') as file :
        file.write('\n{}<![CDATA[ {} ]]>'.format(' '*int(niveau)*3, contenu))

##############################################################
# Fonction : TEST
##############################################################
def print_xml_balise_fermante(tag, niveau) :
    print('{}</{}>'.format(' '*int(niveau)*4, tag))

def print_xml_balise_ouvrante(tag, niveau=0, att1='', val1='', att2='', val2='', att3='', val3=''):
    if att1 != '' and att2 != '' and att3 != '':
        print('{}<{} {}=\'{}\' {}=\'{}\' {}=\'{}\'>'.format(' '*int(niveau)*3, tag, att1, val1, att2, val2, att3, val3))
    elif att1 != '' and att2 != '' and att3 == '':
        print('{}<{} {}=\'{}\' {}=\'{}\'>'.format(' '*int(niveau)*3, tag, att1, val1, att2, val2))
    elif att1 != '' and att2 == '' and att3 == '':
        print('{}<{} {}=\'{}\'>'.format(' '*int(niveau)*3, tag, att1, val1))
    elif att1 == '' and att2 == '' and att3 == '':
        print('{}<{}>'.format(' '*int(niveau)*3, tag))

if __name__ == '__main__':
    pass
