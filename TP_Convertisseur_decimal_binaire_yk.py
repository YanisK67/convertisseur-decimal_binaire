#!/usr/bin/env python
# coding: utf-8

# Fait par Yanis KHELIF
# **<h2>4. Projet : Notre premier convertisseur décimal-binaire </h2>**

# In[12]:


import math

def decimal_vers_ieee754(nombre):
    """Convertit un nombre décimal en sa représentation IEEE 754 (32 bits)"""
    
    # Cas particulier : si le nombre est 0, retourner une chaîne de 32 zéros
    if nombre == 0:
        return '0' * 32
    
    # Déterminer le bit de signe : 1 pour un nombre négatif, 0 pour un nombre positif
    signe = '1' if nombre < 0 else '0'
    nombre = abs(nombre)  # Travailler avec la valeur absolue
    
    # Cas particulier : si le nombre est l'infini, retourner la représentation IEEE correspondante
    if math.isinf(nombre):
        return signe + '11111111' + '0' * 23
    
    # Cas particulier : si le nombre est NaN (Not a Number), retourner la représentation IEEE correspondante
    if math.isnan(nombre):
        return signe + '11111111' + '1' + '0' * 22
    
    # Calculer l'exposant en base 2 du nombre
    exposant = math.floor(math.log2(nombre))
    # Calculer la mantisse normalisée (en supprimant le bit implicite)
    mantisse = nombre / (2 ** exposant) - 1
    
    # Ajouter le biais IEEE 754 (127) à l'exposant
    exposant_biased = exposant + 127
    # Convertir l'exposant en binaire sur 8 bits
    exposant_bits = format(exposant_biased, '08b')
    
    # Construire la mantisse en binaire sur 23 bits
    mantisse_bits = ''
    for _ in range(23):
        mantisse *= 2
        if mantisse >= 1:
            mantisse_bits += '1'
            mantisse -= 1
        else:
            mantisse_bits += '0'
    
    # Retourner la représentation IEEE 754 sous forme de chaîne binaire
    return signe + exposant_bits + mantisse_bits

def ieee754_vers_decimal(bits):
    """Convertit une représentation IEEE 754 (32 bits) en nombre décimal"""
    
    # Si l'entrée est une chaîne binaire, la convertir en entier
    if isinstance(bits, str):
        bits = int(bits, 2)    
    
    # Extraire le bit de signe : 1 -> négatif, 0 -> positif
    signe = -1 if bits >> 31 else 1
    
    # Extraire l'exposant (bits 30 à 23) et retirer le biais IEEE 754 (127)
    exposant = ((bits >> 23) & 0xFF) - 127
    
    # Extraire la mantisse (bits 22 à 0) et ajouter le bit implicite (1)
    mantisse = 1 + ((bits & 0x7FFFFF) / 0x800000)
    
    # Cas particulier : si l'exposant est 255 (11111111), le nombre est Infini ou NaN
    if exposant == 128:
        if mantisse == 1:
            return float('inf') if signe == 1 else float('-inf')
        else:
            return float('nan')
    
    # Cas particulier : si l'exposant est 0
    if exposant == -127:
        if mantisse == 1:
            return 0.0 if signe == 1 else -0.0
        exposant = -126  # Exposant corrigé 
        mantisse -= 1     # Ajustement de la mantisse
    
    # Retourner le nombre décimal correspondant
    return signe * mantisse * (2 ** exposant)

# Tests du convertisseur
print("Convertisseur version 1 : ")
nombres_test = [1.0, -2.5, 0.1, 0.3, float('inf'), float('nan')] # Liste de nombres à tester

for n in nombres_test:
    bits = decimal_vers_ieee754(n)  # Conversion en IEEE 754
    result = ieee754_vers_decimal(bits)  # Conversion inverse en décimal
    print(f"{n} -> {bits} -> {result}")


################# version suplémentaire (faite avec aide) mais plus compliquée avec struct

# In[14]:


import struct

def decimal_vers_ieee754(nombre):
    """Convertit un nombre décimal en sa représentation IEEE 754 (32 bits)"""
    # Utilisation de la librairie struct pour convertir un float en octets puis en entier
    bits = struct.unpack('>I', struct.pack('>f', nombre))[0]  # Conversion float -> octets -> int
    return format(bits, '032b')  # Format binaire sur 32 bits

def ieee754_vers_decimal(bits):
    """Convertit une représentation IEEE 754 (32 bits) en nombre décimal"""
    # Vérifier si l'entrée est une chaîne binaire et la convertir en entier
    if isinstance(bits, str):
        bits = int(bits, 2)  # Convertir la chaîne binaire en entier
    # Utilisation de struct pour convertir l'entier en float
    return struct.unpack('>f', struct.pack('>I', bits))[0]  # Conversion inverse

# Tests du convertisseur
print("\nConvertisseur version 2 : ")
nombres_test = [1.0, -2.5, 0.1, 0.3, float('inf'), float('nan')]  # Liste de nombres à tester

for n in nombres_test:
    bits = decimal_vers_ieee754(n)  # Conversion en IEEE 754
    result = ieee754_vers_decimal(bits)  # Conversion inverse en décimal
    print(f"{n} -> {bits} -> {result}")


# **<h3>4.1 Exercices - Manipulation des nombres flottants</h3>**

# **1. Précision et arrondi**
# 
#   Écrivez une fonction qui compare deux nombres flottants avec une précision donnée :

# In[15]:

def sont_egaux(a, b, precision=1e-10):
    """
    Vérifie si deux nombres flottants sont égaux à une précision donnée.
    :param a: Premier nombre
    :param b: Deuxième nombre
    :param precision: Tolérance d'erreur pour la comparaison
    :return: True si les nombres sont considérés comme égaux, False sinon
    """

    if abs(a - b) < precision :
        return(True)
    else :
        return(False)

# Tests de la fonction sont_egaux
print("\n1. Précision et arrondi ")
print(sont_egaux(0.1 + 0.2, 0.3))  # Devrait afficher True car la tolérance acceptable
print(sont_egaux(0.1 + 0.2, 0.3, 1e-20))  # Devrait afficher False car la tolérance est très stricte


# **2. Détection des cas spéciaux**
# 
#   Créez une fonction qui détecte si un nombre est un cas spécial IEEE 754 :

# In[16]:


import math


def analyse_nombre(n):
    """
    Détecte si un nombre est un cas spécial IEEE 754 (NaN, Infini, ou Normal).
    :param n: Nombre à analyser
    :return: Chaîne de caractère décrivant le type du nombre
    """
    if math.isnan(n):
        return "NaN"  # Nombre Not-a-Number (indéfini)
    elif math.isinf(n):
        return "Infini"  # Nombre Infini (positif ou négatif)
    else:
        return "Normal"  # Nombre standard

# Test de la fonction analyse_nombre
print("\n2. Détection des cas spéciaux ")
nombres_test = [1.0, float('inf'), float('nan')]
for nombre in nombres_test:
    print(f"{nombre} est {analyse_nombre(nombre)}")


# **3. Calcul de précision**
# 
#   Développez une fonction qui détermine combien de bits de précision sont perdus dans une opération :

# In[17]:


import decimal
import math

def perte_precision(operation):
    """
    Calcule le nombre de bits de précision perdus dans une opération en comparant
    le résultat en virgule flottante avec une version haute précision.
    J'utilise decimal
    :param operation: Fonction représentant l'opération à analyser
    :return: Nombre de bits de précision perdus
    """
    # Exécute l'opération en précision standard
    resultat_float = operation()

    # Sauvegarde du contexte de précision actuel
    contexte_original = decimal.getcontext()
    
    # Création d'un nouveau contexte avec une précision très élevée
    nouveau_contexte = decimal.Context(prec=1000)  # 1000 bits de précision
    decimal.setcontext(nouveau_contexte)
    
    # Recalcul de l'opération avec une plus précision 
    a = decimal.Decimal('0.1')
    b = decimal.Decimal('0.2')
    resultat_decimal = a + b  # Exemple d'opération : 0.1 + 0.2
    
    # Restauration du contexte d'origine
    decimal.setcontext(contexte_original)
    
    # Conversion du résultat haute précision en float standard
    resultat_float_approx = float(resultat_decimal)
    
    # Calcul de la différence entre les deux résultats
    difference = abs(resultat_float - resultat_float_approx)
    
    # Si aucune différence, aucune perte de précision
    if difference == 0:
        return 0
    
    # Calcul du nombre de bits de précision perdus
    nombre_bits_perdus = int(-math.log2(difference))
    
    return nombre_bits_perdus

# Test de la fonction perte_precision
print("\n3. Calcul de précision")
perte = perte_precision(lambda: 0.1 + 0.2)
print(f"Perte de précision : {perte} bits")