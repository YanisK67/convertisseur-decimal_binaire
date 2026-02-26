# TP Python — IEEE 754 & Précision des flottants

Projet réalisé par **Yanis KHELIF**.

Ce dépôt contient **deux scripts Python** autour des nombres flottants :
1. Un **convertisseur décimal ↔ IEEE 754 (32 bits)** + exercices liés (comparaison, cas spéciaux, perte de précision).
2. Un **TP d’analyse de précision** (différence absolue/relative, bits perdus, analyse complète, extensions).

---

## Contenu du dépôt

- `TP_Convertisseur_decimal_binaire_yk.py`  
  Convertisseur **IEEE 754 simple précision (32 bits)** + exercices :
  - conversion décimal → binaire IEEE754 (manuelle)
  - conversion binaire IEEE754 → décimal
  - version  avec `struct`
  - comparaison de flottants à tolérance
  - détection des NaN / Infini / Normal
  - estimation de **bits perdus** sur une opération

- `TP_Precision.py`  
  TP sur la **précision des calculs flottants** :
  - différence absolue
  - différence relative
  - conversion différence relative → **bits perdus**
  - fonction d’analyse complète (affichages)
  - bonus : évaluation de la qualité (“Très précis”, …), tests avancés, optimisation simple d’expressions

---

## Bibliothèques utilisées : 
- uniquement la bibliothèque standard (`math`, `struct`, `decimal`)

---

## Exécution

Depuis un terminal à la racine du dépôt :

python nomFich.py

## Auteur
---
Yanis Khelif (Lycée Notre Dame Providence- Enghien les bains)
