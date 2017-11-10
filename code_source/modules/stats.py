#!usr/bin/python3
#-*- coding : utf8 -*-


##############################################################
# Fonction : lettersDistribution
# 	Parcourt la liste, parcourt chaque mot,
#	creer le vecteur distribution des lettres
# Input : list
# Return : dict
##############################################################
def lettersDistribution(list_word):
    ''' Parcourt un texte, fais un vecteur distribution des mots
    Retour : dictionnaire
    Critere de segmentation : espace '''

    lettersDistribution = {}

    for word in list_word :
        for letter in word :
            if letter not in lettersDistribution:
                lettersDistribution[letter] = 1
            else :
                lettersDistribution[letter] +=1

    return lettersDistribution

##############################################################
# Fonction : wordsDistribution
# 	Parcourt la liste, creer le vecteur distribution des mots
# Input : list
# Return : dict
##############################################################
def wordsDistribution(list_word):
    ''' Parcourt un texte, fais un vecteur distribution des mots
    Retour : dictionnaire
    Critere de segmentation : espace '''

    wordsDistribution = {}

    for word in list_word :
        if word not in wordsDistribution:
            wordDistribution[word] = 1
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


################################################
#vecteur distribution des caracteres
#creer dico qui prend toutes les lettres
#verifier celle qui ne font pas partie de l'alphabet, et des nombres

# Cmt classer alphabetiquement ?
# Un dico qui tranverse le fichier
# Puis trier le dico par valeur
# Et print val : dico
