---
type: schema
campagne: Aeden
branche_narrative: null
statut_documentaire: protocole
visibilite: joueur
version: 1
id: null
date_univers: null
derniere_validation: null
sources: []
---

# Schéma des données

Les fichiers JSON ont schema_version 1. Les identifiants sont stables et les montants des Pièces sont des chaînes décimales exactes. Null = inconnu/non défini, jamais zéro implicite. Les événements disposent d’un ordre entier croissant par branche (ordre narratif, non date réelle).

- finances.json : comptes [{id, branche, solde_initial, solde_actuel, source}] ; transactions [{id, compte_id, branche, ordre, date_univers, montant, statut, source, transfert_id?}]. Montant signé ; statut effectue, prevu ou annule. Deux mouvements de transfert effectue, comptes différents, somme zéro. Si une lacune est établie : solde null, signaler.
- progression.json : personnages [{id, branche, classe:{niveau,exp}, profession:{niveau,exp}}] = état initial de journal ; evenements [{id, personnage_id, branche, ordre, domaine, type, niveau_avant, exp_avant, gain_exp, niveau_apres, exp_apres, source, exception?}]. domaine classe/profession ; type exp, ascension ou correction ; exceptions doivent renvoyer à une décision ou règle officielle. Maîtrises qualitatives dans la fiche compétence et le journal narratif.
- statut.json : valeurs actuelles, stats permanentes, bonus équipement, HP/MP/EP de base et effectifs, titres actifs (IDs), points libres. Les autres effets sont justifiés dans la fiche, sans imposer que le maximum effectif soit identique à la base.
- echeances.json : evenements [{id, branche, ordre_creation, ordre_realisation?, date_univers, heure, statut, source, titre}]. Statut prevu, conditionnel, realise, annule ou reporte. Un engagement conditionnel ne vaut ni confirmation ni réalisation. L’ordre réel n’est pas une conversion de calendrier.
- reprise.json : branche, sauvegarde_id, ordre, date_univers, heure, lieu, source_scene (chemin depuis racine du coffre), point_majeur (chemin ou null). Une sauvegarde réelle renvoie à des fichiers enregistrés. Aucun point majeur fictif.

Les documents Markdown restent maîtres des descriptions et sources narratives, pas une deuxième base numérique indépendante. Une donnée non structurée n’est pas automatiquement vérifiable.
