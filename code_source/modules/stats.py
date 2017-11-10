#!usr/bin/python3
#-*- coding : utf8 -*-

from collections import OrderedDict

##############################################################
# Fonction : lettersDistribution
# 	Parcourt la liste, parcourt chaque mot,
#	creer le vecteur distribution des lettres
#	en classant par lettre
# Input : list
# Return : dict
##############################################################
def dict_lettersDistribution_from_list(list_word):
    ''' Return dict lettersDistribution from a list '''

    lettersDistribution = {}

    for word in list_word :
        for letter in word :
            if letter not in lettersDistribution:
                lettersDistribution[letter] = 1
            else :
                lettersDistribution[letter] +=1

    #Retourne le dict sans ordre
    # return lettersDistribution

    #Retourne un dict classé selon la colonne 0 c-a-d keys
    return OrderedDict(sorted(lettersDistribution.items(), key=lambda t:t[0]))


##############################################################
# Fonction : wordsDistribution
# 	Parcourt la liste,
#	creer le vecteur distribution des mots
# Input : list
# Return : dict
##############################################################
def dict_wordsDistribution_from_list(list_words_without_point):
    ''' Return dict wordsDistribution from a list '''

    wordsDistribution = {}

    for word in list_words_without_point :
        if word not in wordsDistribution:
            wordsDistribution[word] = 1
        else :
            wordsDistribution[word] +=1

    return wordsDistribution


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

##############################################################
# Fonction : word_by_sentence
# 	- calcul le nombre de mots vs le nombre de formes differentes
# Input :
# Return :
##############################################################
# prend comme marqueur le '.'
# calcul nombre de mot, nombre de '.' et divise
def nb_average_words_by_sentence(list_words_with_point):

    words, average_words_by_sentence, sentences = 0, 0, 0

    for word in list_words_with_point :
        if word == '.':
            sentences += 1
        else :
            words += 1

    try:
        average_words_by_sentence = words / sentences
    except ZeroDivisionError as error :
        average_words_by_sentence = words

    return average_words_by_sentence


################################################
#vecteur distribution des caracteres
#creer dico qui prend toutes les lettres
#verifier celle qui ne font pas partie de l'alphabet, et des nombres

# Un dico qui tranverse le fichier
# Puis trier le dico par valeur
# Et print val : dico
