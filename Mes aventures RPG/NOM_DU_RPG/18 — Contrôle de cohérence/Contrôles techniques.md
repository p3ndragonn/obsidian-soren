---
type: technique
campagne: NOM_DU_RPG
branche_narrative: null
statut_documentaire: protocole
visibilite: joueur
version: 1
id: null
date_univers: null
derniere_validation: null
sources: []
---

# Contrôles techniques

Exécuter depuis la racine du dépôt : `python3 "Mes aventures RPG/NOM_DU_RPG/18 — Contrôle de cohérence/audit.py"` (Python 3.10+, PyYAML : `python3 -m pip install PyYAML`). Tests : `python3 "Mes aventures RPG/NOM_DU_RPG/18 — Contrôle de cohérence/test_audit.py"`.

Le script est en lecture seule. Il vérifie les liens Obsidian et médias locaux, métadonnées, IDs, données financières et progression structurée, cohérence des statistiques et références de reprise. Il n’interprète pas le texte narratif, ne valide pas les exceptions ni les dates fictives sans calendrier/ordre explicite. Les fichiers JSON sont les sources numériques maîtresses ; les notes Markdown les indexent. Une donnée null reste inconnue. Une anomalie doit être arbitrée et tracée. Les rapports automatisés ne doivent pas afficher les contenus confidentiels.

GitHub Actions : exécution à chaque modification du dossier si le workflow et les permissions sont disponibles.
