#!/usr/bin/env python
# coding: utf-8

"""
Auteur : Yanis KHELIF
Projet : Analyse de précision des calculs flottants
"""

import math
from math import log2


# ======================================================
# Partie 1 : Différences et bits perdus
# ======================================================

def calcule_difference(nombre1, nombre2):
    """Calcule la différence absolue entre deux nombres."""
    return abs(nombre1 - nombre2)


def calcule_difference_relative(nombre1, nombre2):
    """Calcule la différence relative entre deux nombres."""
    if nombre2 == 0:
        return None
    return calcule_difference(nombre1, nombre2) / abs(nombre2)


def calcule_bits_perdus(dif_re):
    """Convertit une différence relative en nombre de bits de précision perdus."""
    if dif_re is None or dif_re == 0:
        return None
    return -log2(dif_re)


# ======================================================
# Partie 2 : Analyse de précision
# ======================================================

def analyse_precision(calcule, theorique):
    """Analyse la précision d'un calcul par rapport à la valeur théorique."""
    print("*" * 50)
    print(f"Analyse de la précision : {calcule} ≈ {theorique}")
    print("*" * 50)

    # Différence absolue
    diff_abs = calcule_difference(calcule, theorique)
    print(f"Différence absolue : {diff_abs}")

    # Différence relative
    diff_rel = calcule_difference_relative(calcule, theorique)
    if diff_rel is not None:
        print(f"Différence relative : {diff_rel}")
        bits = calcule_bits_perdus(diff_rel)
        print(f"Bits de précision perdus : {bits}")
    else:
        print("Impossible : division par zéro")
    print("\n")


def precision_evaluation(bits_perdus):
    """Évalue la précision selon le nombre de bits perdus."""
    if bits_perdus is None:
        return None
    if bits_perdus < 5:
        return "Très précis"
    elif 5 <= bits_perdus <= 20:
        return "Précision moyenne"
    else:
        return "Peu précis"


def optimiser_calcul(expression):
    """
    Propose une meilleure façon de faire un calcul si possible.
    Exemple : "0.1 + 0.1 + 0.1" -> "3 * 0.1"
    """
    termes = [t.strip() for t in expression.split('+')]
    if len(set(termes)) == 1 and len(termes) > 1:
        return f"{len(termes)} * {float(termes[0])}"
    return expression


# ======================================================
# Partie 3 : Tests et exemples
# ======================================================

def tests_exercice1_2_3():
    print("=== Exercice 1 : Différence absolue ===")
    print("Test 1:", calcule_difference(0.1 + 0.2, 0.3))
    print("Test 2:", calcule_difference(1, 1))

    print("\n=== Exercice 2 : Différence relative ===")
    print("Test 1:", calcule_difference_relative(0.1 + 0.2, 0.3))
    print("Test 2:", calcule_difference_relative(1000000.1, 1000000))
    print("Test 3:", calcule_difference_relative(1, 0))

    print("\n=== Exercice 3 : Bits perdus ===")
    examples = [(0.1 + 0.2, 0.3), (1 / 3 + 1 / 3 + 1 / 3, 1), (2 + 2, 4)]
    for calc, theorique in examples:
        diff_rel = calcule_difference_relative(calc, theorique)
        bits = calcule_bits_perdus(diff_rel)
        print(f"Bits perdus pour {calc} vs {theorique} : {bits}")


def tests_exercice4():
    print("\n=== Exercice 4 : Analyse de précision ===")
    tests = [
        (0.1 + 0.2, 0.3),
        (1 / 3 + 1 / 3 + 1 / 3, 1),
        (2 + 2, 4),
        (0.1 + 0.1 + 0.1, 0.3),
        (1e308 * 1e308, float('inf')),  # Infini
        (1e-308 / 1e308, 0),  # Résultat proche de zéro
        (math.pi * 2, 6.283185307179586)
    ]
    for calc, theorique in tests:
        analyse_precision(calc, theorique)


def tests_optimisation():
    print("\n=== Test optimisation de calcul ===")
    expressions = ["0.1 + 0.1 + 0.1", "3 * 0.1", "0.2 + 0.2 + 0.2"]
    for expr in expressions:
        optimisee = optimiser_calcul(expr)
        print(f"Original : {expr} -> Optimisée : {optimisee}")


def tests_precision_evaluation():
    print("\n=== Test évaluation du niveau de précision ===")
    exemples = [(0.1 + 0.2, 0.3), (1 / 3 + 1 / 3 + 1 / 3, 1), (2 + 2, 4)]
    for calc, theorique in exemples:
        diff_rel = calcule_difference_relative(calc, theorique)
        bits = calcule_bits_perdus(diff_rel)
        niveau = precision_evaluation(bits)
        print(f"{calc} vs {theorique} -> Niveau de précision : {niveau}")


# ======================================================
# Exécution principale
# ======================================================

if __name__ == "__main__":
    tests_exercice1_2_3()
    tests_exercice4()
    tests_optimisation()
    tests_precision_evaluation()