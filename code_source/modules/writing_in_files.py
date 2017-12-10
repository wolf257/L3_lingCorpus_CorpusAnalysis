#!/usr/bin/env python3
#-*- coding : utf8 -*-

import os
import codecs

##############################################################
# Fonction : remplissage_info_base_corpus
# - Crée le fichier  0_stats_du_corpus.tx
# - Inscrit le nombre de fichier
# - Ecrit une liste des fichiers
##############################################################
def remplissage_stat_corpus(nom_fichier_stats_corpus, nom_corpus, files_in_corpus):
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
def remplissage_stat_texte(file, path_to_corpus, path_to_corpus_stat_folder):
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
                file_stat_file.write('\n{} : {} : {} : {} '.format(2,3,4,5))

                file_stat_file.write('\n\n\n NOTICE (le numéro est celui du champ en cas de split(\':\') : ')
                file_stat_file.write('\n[0] {} : [1] {} : [2] {} : [3] {} : [4] {}'.format( 'a' , 'b' , 'c' , 'd' , 'e'))

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


if __name__ == '__main__':
    pass
