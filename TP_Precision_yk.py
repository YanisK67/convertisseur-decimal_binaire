#!/usr/bin/env python
# coding: utf-8

# Projet Jupyter notebook par Yanis KHELIF 
# 
# **<h2> Exercice 1 : Calcul de la différence </h2>**

# In[21]:


import math

def calcule_difference(nombre1, nombre2):
    """
    Cette fonction calcule la différence absolue entre deux nombres
    
    Paramètres de la fonction :
        nombre1 : premier nombre
        nombre2 : deuxième nombre
    
    valeur de retour :
        La valeur absolue de la différence entre les deux nombres
    """
    # je calcule la valeur absolue de la difference et je la retourne
    resultat = abs(nombre1-nombre2)
    return (resultat)

# appel de la fonction pour tester avec les valeurs de l'ennoncé
print("exo 1")
print("Resultat de mon Test 1:", calcule_difference(0.1 + 0.2, 0.3))  
print("Resultat de mon Test 2:", calcule_difference(1, 1))            


# **<h2> Exercice 2 : Différence relative </h2>**

# In[20]:


def calcule_difference_relative(nombre1, nombre2):
    """
    Cette fonction calcule la différence relative entre deux nombres
    
     Paramètres de la fonction :
        nombre1 : nombre calculé
        nombre2 : nombre théorique (référence)
    
      valeur de retour :
        La différence relative ou None si b est 0
    """
    # Attention je rajoute un if pour eviter la division par 0
    if nombre2 == 0:
        return None
    # on appelle la fonction precedente
    resultat = calcule_difference(nombre1, nombre2)/abs(nombre2)
    return resultat

# appel de la fonction pour tester avec les valeurs de l'ennoncé
print("\nexo 2")
print("Resultat de mon Test 1:", calcule_difference_relative(0.1 + 0.2, 0.3))
print("Resultat de mon Test 2:", calcule_difference_relative(1000000.1, 1000000))
print("Resultat de mon Test 3:", calcule_difference_relative(1, 0)) 


# 
# **<h3> Exercice 3 : À la découverte des bits de précision </h3>**
#  
# ############ Partie A# ############ 

# In[23]:


#exemple de calcule de la différence relative sur plusieurs cas
print("\nexo 3 Partie : A")

print(calcule_difference_relative(1.5, 1))  

print(calcule_difference_relative(1.25, 1)) 

print(calcule_difference_relative(1.125, 1))  


# # ############ Partie B # ############ 

# In[19]:


from math import log2

def calcule_bits_perdus(dif_re):
    """
    Cette fonction convertit une différence relative en un nombre de bits de précision perdus
    
    Paramètres d'entrée de la fonction :
        
        dif_re : la différence relative 
    
    retour :
        Le nombre de bits perdus ou None si la différence est 0 ou None
    """
    # verification du None ou 0
    
    if dif_re is None or dif_re == 0:
        return None
    else :       # resultat le nombre de bits perdus grace au log2
        resultat= -log2(dif_re)
        return (resultat)

# je fais des tests pour verifier la fonction avec les valeurs de l'ennoncé

print("\nexo 3 Partie : B")
difference = calcule_difference_relative(0.1 + 0.2, 0.3)
bits_perdus = calcule_bits_perdus(difference)
print(f"Bits de précision perdus (0.1 + 0.2, 0.3) : {bits_perdus}")

difference = calcule_difference_relative(1/3 + 1/3 + 1/3, 1)
bits_perdus = calcule_bits_perdus(difference)
print(f"Bits de précision perdus (1/3 + 1/3 + 1/3, 1): {bits_perdus}")


difference = calcule_difference_relative(2 + 2, 4)
bits_perdus = calcule_bits_perdus(difference)
print(f"Bits de précision perdus (2 + 2, 4): {bits_perdus}")

#

# **<h3> Exercice 4 : Assemblage des fonctions </h3>**

# In[15]:


def analyse_precision(calcule, theorique):
    """
    fonction qui analyse la précision d'un calcul
    
    parametres :
        calcule : le résultat du calcul à analyser
        theorique : la valeur théorique attendue
    retour :
        c'est une fonction qui affiche
    """
    print("*" * 50)
    print(f"Analyse la precision de {calcule} ≈ {theorique}")
    print("*" * 50)
    print("\n")
    
    # je cherche à calculer  la différence absolue
    diff1 = calcule_difference(calcule, theorique)
    print(f"Différence absolue : {diff1}")
    
    # je cherche à calculer la différence relative
    diff2 = calcule_difference_relative(calcule, theorique)
    
    # attention il faut tester le none
    if diff2 is not None:
        print(f"Différence relative : {diff2}")
        
        # Calcul des bits perdus
        bits = calcule_bits_perdus(diff2)
        print(f"Les bits de précision perdus : {bits}")
    else:
        print("Impossible : je suis dans le cas de la division par zéro)")
    print("\n")
# Tests de la fonction avec les valeurs de l'ennoncé
tests = [
    (0.1 + 0.2, 0.3),
    (1/3 + 1/3 + 1/3, 1),
    (2 + 2, 4),
    (0.1 + 0.1 + 0.1, 0.3) 
]
print("\nexo 4")
for test in tests:
    calcule, theorique = test
    analyse_precision(calcule, theorique)

# **<h3> Pour aller plus loins </h3>**
##############################1
def precision_evaluation(bits_perdus):
    """
    Évalue la précision d'un calcul en fonction du nombre de bits perdus.

    Arguments:
        bits_perdus

    Retours:
        Une chaîne de caractères décrivant la précision ("Très précis", "Précision moyenne", "Peu précis")
             ou None si on ne peut pas mesuer
    """
    # Vérifie si la valeur de bits_perdus existe
    if bits_perdus is not None: 
        # Si la perte de bits est inférieure à 5, la précision est considérée comme très bonne
        if bits_perdus < 5:
            return "Très précis"
        # Si la perte de bits est entre 5 et 20 la précision est considérée comme moyenne
        elif 5 <= bits_perdus <= 20:
            return "Précision moyenne"
        #si la perte de bits est supérieure à 20, la précision est considérée comme faible
        else:
            return "Peu précis"
    # ici a perte de précision n'a pas été mesurée
    else:
        return None

print("\n*****************Pour aller plus loins******************")
print("\n*****************Niveau de précision******************")

# Exemple d'utilisation
difference = calcule_difference_relative(0.1 + 0.2, 0.3)
bits_perdus = calcule_bits_perdus(difference)
print("Niveau de précision :", precision_evaluation(bits_perdus))

difference = calcule_difference_relative(1/3 + 1/3 + 1/3, 1)
bits_perdus = calcule_bits_perdus(difference)
print("Niveau de précision :", precision_evaluation(bits_perdus))


difference = calcule_difference_relative(2 + 2, 4)
bits_perdus = calcule_bits_perdus(difference)
print("Niveau de précision :", precision_evaluation(bits_perdus))

##############################2
#import math
print("\n***********Testez différents types de calculs pour comprendre quand les erreurs apparaissent****************")
analyse_precision(0.1 + 0.2, 0.3)
analyse_precision(1e308 * 1e308, float('inf'))  # Infini en IEEE-754
analyse_precision(1e-308 / 1e308, 0)  # Résultat proche de zéro
analyse_precision(math.pi * 2, 6.283185307179586)

##############################3
def optimiser_calcul(expression):
    """fonction qui propose une meilleure façon de faire le calcul quand cest possible"""
    # Divise l'expression en termes séparés par le signe '+'
    termes = expression.split('+')
    
    # Supprime les espaces au début et à la fin de chaque terme
    termes = [terme.strip() for terme in termes]
    
    # Vérifie si tous les termes sont identiques et s'il y a plus d'un terme
    if len(set(termes)) == 1 and len(termes) > 1:
        # Convertit le premier terme en nombre flottant
        nombre = float(termes[0])
        
        # Compte le nombre de termes
        count = len(termes)
        # Retourne l'expression optimisée sous forme de multiplication
        return f"{count} * {nombre}"
     # Si l'optimisation n'est pas possible, retourne l'expression originale
    return expression


print("\n*******fonction qui propose une meilleure façon de faire le calcul quand cest possible*********")

# Exemple d'utilisation
expression1 = "0.1 + 0.1 + 0.1"
optimisee1 = optimiser_calcul(expression1)
print(f"Original : {expression1}")
print(f"Optimisée : {optimisee1}")

# Nouveau cas : déjà sous forme de multiplication
expression2 = "3 * 0.1"
optimisee2 = optimiser_calcul(expression2)
print(f"\nOriginal : {expression2}")
print(f"Optimisée : {optimisee2}")


print("\n*******fin***** voir dans le code en commentaire question 4*********")


######################### question 4 ####################
#En Python, un nombre de type float utilise 64 bits en mémoire, qui sont répartis en trois parties : le signe (1 bit), l'exposant (11 bits) et la mantisse (52 bits). 
# Le signe montre si le nombre est positif ou négatif, l'exposant détermine où se trouve la virgule flottante, et la mantisse contient les chiffres significatifs du nombre.
# La mantisse est constituée de 52 bits explicites, plus 1 bit caché, ce qui donne un total de 53 bits pour la précision du nombre.
# Cela permet de garder environ 15 à 17 chiffres significatifs. La précision est limitée à ces 52 bits utiles. 
# Si l'erreur dépasse cette limite, la mantisse devient inutile, et le nombre est arrondi à zéro ou à un multiple de 2 (on est en binaire) le plus proche.
# Une erreur plus grande signifie que l'on a atteint la limite de ce que peut représenter un nombre en double précision.
#