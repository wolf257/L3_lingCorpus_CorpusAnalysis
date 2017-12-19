#!/usr/bin/env python3
#-*- coding : utf8 -*-

from collections import OrderedDict

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     PRESENTATION DU MODULE :
#          Ce modules rassemble toutes les fonctions
#          permettant de réaliser les distributions (lettres ou mots)
#          et les calculs statistiques.
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

########################################################
# LIST FUNCTIONS IN MODULES
#
#	+ lettersDistribution_dict_from_list + test
#	+ wordsDistribution_dict_from_list + test
#	+ wordsDistributionUpdate_dict_from_list()
#	+ nb_average_words_by_sentence
#	+ average_words_by_sentence_nb_from_
########################################################

##############################################################
# Fonction : lettersDistribution_dict_from_list()
# 	Parcourt la liste, parcourt chaque mot,
#	creer le vecteur distribution des lettres
#	en classant par lettre
# Input : list
# Return : dict
##############################################################
#TEST written
def lettersDistribution_dict_from_list(list_word):
    ''' Return dict lettersDistribution from a list '''

    lettersDistribution = {}

    for word in list_word :
        for letter in word :
            if letter not in lettersDistribution:
                lettersDistribution[letter] = 1
            else :
                lettersDistribution[letter] +=1

    #Retourne le dict sans ordre
    #return lettersDistribution
    return OrderedDict(sorted(lettersDistribution.items(), key=lambda t:t[0]))

    #Retourne un dict classé selon la colonne 0 c-a-d keys
    #lettersDistributionOrder = OrderedDict()
    #lettersDistributionOrder = OrderedDict(sorted(lettersDistribution.items(), key=lambda t:t[0]))
    #return lettersDistributionOrder

##############################################################
# Fonction : wordsDistribution_dict_from_list
# 	Parcourt la liste,
#	creer le vecteur distribution des mots
# Input : list
# Return : dict
##############################################################
#TEST written
def wordsDistribution_dict_from_list(list_words_without_point):
    ''' Return dict wordsDistribution from a list
        Classer par ordre alphabétique '''

    wordsDistribution = {}

    for word in list_words_without_point :
        if word not in wordsDistribution:
            wordsDistribution[word] = 1
        else :
            wordsDistribution[word] +=1

    wordsDistributionOrder = OrderedDict()
    wordsDistributionOrder = OrderedDict(sorted(wordsDistribution.items(), key=lambda t:t[0]))

    return wordsDistributionOrder

##############################################################
# Fonction : wordsDistributionUpdate_dict_from_list
# 	Parcourt la liste,
#	creer le vecteur distribution des mots
# Input : list
# Return : dict
##############################################################
#TEST written
def wordsDistributionUpdate_dict_from_list(dictionnaire, list_words):
    ''' Update dict from a list '''

    dico = dictionnaire

    for word in list_words :
        if word not in dictionnaire:
            dico[word] = 1
        else :
            dico[word] +=1

    DistributionOrder = OrderedDict()
    DistributionOrder = OrderedDict(sorted(dico.items(), key=lambda t:t[0]))

    return DistributionOrder

##############################################################
# Fonction : nb_average_words_by_sentence
# 	- calcule le nombre de mots et le nombre de point
#	le quotient de leur division donne le nombre de phrase
# Input : list
# Return : number
##############################################################
# prend comme marqueur le '.'
# calcul nombre de mot, nombre de '.' et divise
def nb_sentences_from_list_words_with_point(list_words_with_point):

    sentences = 0

    for word in list_words_with_point :
        if word == '.' or word == '?' or word == '!':
            sentences += 1

    return sentences

##############################################################
# Fonction : average_words_by_sentence_nb_from_
# 	- calcule le nombre de mots et le nombre de point
#	le quotient de leur division donne le nombre de phrase
# Input : list
# Return : number
##############################################################
# prend comme marqueur le '.'
# calcul nombre de mot, nombre de '.' et divise
def average_words_by_sentence_nb_from_(list_words_with_point):

    words, average_words_by_sentence, sentences = 0, 0, 0

    list_words_with_point = ponctuation_texte.punctuation_sep_word_list_from_list

    for word in list_words_with_point :
        if word == '.' or word == '?' or word == '!' :
            sentences += 1
        else :
            words += 1

    try:
        average_words_by_sentence = words / sentences
    except ZeroDivisionError as error :
        average_words_by_sentence = words

    return average_words_by_sentence

if __name__ == '__main__':
    pass
