#!/usr/bin/env python3
#-*- coding : utf8 -*-

from collections import OrderedDict

########################################################
# LIST FUNCTIONS IN MODULES
#	+ lettersDistribution_dict_from_list
#	+ wordsDistribution_dict_from_list
#	+
#	+
#	+
########################################################

#########
#TODO : creer moyen d'acces, surtout aux dicos
#########

##############################################################
# Fonction : lettersDistribution
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
# Fonction : wordsDistribution
# 	Parcourt la liste,
#	creer le vecteur distribution des mots
# Input : list
# Return : dict
##############################################################
#TEST written
def wordsDistribution_dict_from_list(list_words_without_point):
    ''' Return dict wordsDistribution from a list '''

    wordsDistribution = {}

    for word in list_words_without_point :
        if word not in wordsDistribution:
            wordsDistribution[word] = 1
        else :
            wordsDistribution[word] +=1

    return wordsDistribution

##############################################################
# Fonction : nb_average_words_by_sentence
# 	- calcule le nombre de mots et le nombre de point
#	le quotient de leur division donne le nombre de phrase
# Input : list
# Return : number
##############################################################
# prend comme marqueur le '.'
# calcul nombre de mot, nombre de '.' et divise
def average_words_by_sentence_nb_from_(list_words_with_point):

    words, average_words_by_sentence, sentences = 0, 0, 0

    for word in list_words_with_point :
        if word == '.':
            sentences += 1
        #TODO : creer fonction pour separer les points des mots from string
        # PUIS creer la liste
        # NB : pour l'instant 'je.' n'augmentera pas le nb de phrase ET tombe dans le else.

        else :
            words += 1

    try:
        average_words_by_sentence = words / sentences
    except ZeroDivisionError as error :
        average_words_by_sentence = words

    return average_words_by_sentence

#TEST
# a = 'je vais jouer au basket. je reviens'
# b = a.split()
# c = 0
# c = nb_average_words_by_sentence(b)
# print("On a une moyenne de mots/phrase de : " , c)

##############################################################
# Fonction : wordbyValue
# 	-
# Input : dict
# Return : dict
##############################################################
# def wordbyValue(nom_dico) :
    # '''Reverse mot -> occurence pour occurence vers mots
    # Retour : dictionnaire
    # Classement : par frequence '''
    #
    # wordbyValue = {}
    # wordbyValue = dict([[value, key] for key, value in nom_dico.items()])
    #
    # return wordbyValue

    #PB : la key est uniq donc si plusieurs mots ont la même value, seul le dernier sera retenu.

##############################################################
# Fonction : nbres_vs_forme
# 	- calcul le nombre de mots vs le nombre de formes differentes
# Input :
# Return :
##############################################################





if __name__ == '__main__':
    pass
