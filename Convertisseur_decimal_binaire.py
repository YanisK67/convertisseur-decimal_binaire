#!/usr/bin/env python
# coding: utf-8

"""
Auteur : Yanis KHELIF
Projet : Convertisseur décimal ↔ IEEE 754 et exercices sur les nombres flottants
"""

import math
import struct
import decimal


# ======================================================
# Partie 1 : Convertisseur décimal ↔ IEEE 754
# ======================================================

def decimal_vers_ieee754(nombre):
    """Convertit un nombre décimal en sa représentation IEEE 754 (32 bits) sans struct."""
    if nombre == 0:
        return '0' * 32
    signe = '1' if nombre < 0 else '0'
    nombre = abs(nombre)
    if math.isinf(nombre):
        return signe + '11111111' + '0' * 23
    if math.isnan(nombre):
        return signe + '11111111' + '1' + '0' * 22

    exposant = math.floor(math.log2(nombre))
    mantisse = nombre / (2 ** exposant) - 1
    exposant_biased = exposant + 127
    exposant_bits = format(exposant_biased, '08b')

    mantisse_bits = ''
    for _ in range(23):
        mantisse *= 2
        if mantisse >= 1:
            mantisse_bits += '1'
            mantisse -= 1
        else:
            mantisse_bits += '0'

    return signe + exposant_bits + mantisse_bits


def ieee754_vers_decimal(bits):
    """Convertit une représentation IEEE 754 (32 bits) en nombre décimal sans struct."""
    if isinstance(bits, str):
        bits = int(bits, 2)
    signe = -1 if bits >> 31 else 1
    exposant = ((bits >> 23) & 0xFF) - 127
    mantisse = 1 + ((bits & 0x7FFFFF) / 0x800000)

    if exposant == 128:
        if mantisse == 1:
            return float('inf') if signe == 1 else float('-inf')
        return float('nan')

    if exposant == -127:
        if mantisse == 1:
            return 0.0 if signe == 1 else -0.0
        exposant = -126
        mantisse -= 1

    return signe * mantisse * (2 ** exposant)


# Version simplifiée avec struct
def decimal_vers_ieee754_struct(nombre):
    """Convertit un float en IEEE 754 32 bits (utilisation de struct)."""
    bits = struct.unpack('>I', struct.pack('>f', nombre))[0]
    return format(bits, '032b')


def ieee754_vers_decimal_struct(bits):
    """Convertit une représentation IEEE 754 (32 bits) en float (struct)."""
    if isinstance(bits, str):
        bits = int(bits, 2)
    return struct.unpack('>f', struct.pack('>I', bits))[0]


# ======================================================
# Partie 2 : Exercices sur les flottants
# ======================================================

def sont_egaux(a, b, precision=1e-10):
    """Vérifie si deux nombres flottants sont égaux à une précision donnée."""
    return abs(a - b) < precision


def analyse_nombre(n):
    """Détecte si un nombre est un cas spécial IEEE 754 (NaN, Infini, Normal)."""
    if math.isnan(n):
        return "NaN"
    elif math.isinf(n):
        return "Infini"
    return "Normal"


def perte_precision(operation):
    """
    Calcule le nombre de bits de précision perdus dans une opération en utilisant decimal.
    operation : fonction représentant l'opération à analyser.
    """
    resultat_float = operation()
    contexte_original = decimal.getcontext()
    nouveau_contexte = decimal.Context(prec=1000)
    decimal.setcontext(nouveau_contexte)

    # Ici exemple pour 0.1 + 0.2
    a = decimal.Decimal('0.1')
    b = decimal.Decimal('0.2')
    resultat_decimal = a + b

    decimal.setcontext(contexte_original)
    resultat_float_approx = float(resultat_decimal)
    difference = abs(resultat_float - resultat_float_approx)

    if difference == 0:
        return 0

    return int(-math.log2(difference))


# ======================================================
# Partie 3 : Tests et exemples
# ======================================================

def tests_convertisseur():
    print("=== Tests convertisseur IEEE 754 ===")
    nombres_test = [1.0, -2.5, 0.1, 0.3, float('inf'), float('nan')]
    for n in nombres_test:
        bits1 = decimal_vers_ieee754(n)
        result1 = ieee754_vers_decimal(bits1)
        bits2 = decimal_vers_ieee754_struct(n)
        result2 = ieee754_vers_decimal_struct(bits2)
        print(f"{n} -> {bits1} -> {result1} | struct: {bits2} -> {result2}")


def tests_fonctions_flottants():
    print("\n=== Tests fonctions flottants ===")
    print("\n1. Précision et arrondi")
    print(sont_egaux(0.1 + 0.2, 0.3))
    print(sont_egaux(0.1 + 0.2, 0.3, 1e-20))

    print("\n2. Détection des cas spéciaux")
    nombres_test = [1.0, float('inf'), float('nan')]
    for nombre in nombres_test:
        print(f"{nombre} est {analyse_nombre(nombre)}")

    print("\n3. Calcul de précision")
    perte = perte_precision(lambda: 0.1 + 0.2)
    print(f"Perte de précision : {perte} bits")


# ======================================================
# Exécution principale
# ======================================================

if __name__ == "__main__":
    tests_convertisseur()
    tests_fonctions_flottants()