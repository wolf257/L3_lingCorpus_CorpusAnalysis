#!/usr/bin/env python3
#-*- coding : utf8 -*-

import os
import codecs

##############################################################
# Fonction : remplissage_info_base_corpus
##############################################################
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


##############################################################
# Fonction : ecrire_distribution_mot_texte_dans_2_distri
##############################################################
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
