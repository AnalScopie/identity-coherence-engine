# 🔵 Identity Coherence Engine

Moteur de normalisation et d’audit des données d’identité côté utilisateur.

## 🎯 Objectif

Ce projet démontre une implémentation minimale d’un moteur de cohérence des données permettant :

- la normalisation des attributs d’identité
- des transformations déterministes
- une traçabilité complète (audit log)
- une exécution locale sans dépendance externe

## ⚙️ Fonctionnement

Entrée :
- fichier JSON contenant des données d’identité

Sortie :
- données normalisées (`output.json`)
- journal d’audit (`audit.log`)

## 🔐 Propriétés

- comportement déterministe
- aucune connectivité réseau
- transformations transparentes
- système entièrement inspectable

## 🧪 Exemple

Entrée :
```json
{
  "first_name": "  jean ",
  "email": "JEAN.DUPONT@MAIL.COM "
}# identity-coherence-engine
User-side identity data normalization and audit engine
