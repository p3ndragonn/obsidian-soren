---
type: conventions
campagne: Aeden
branche_narrative: null
statut_documentaire: protocole
visibilite: joueur
version: 2
id: null
date_univers: null
derniere_validation: null
sources: []
---

# Conventions de continuité et de classement

## Priorité documentaire
Décision explicite validée du Fondateur > référentiels officiels > dernier état canonique validé > fiches actuelles > historique joué > anciennes sauvegardes > propositions. Toute contradiction est signalée ; aucune réécriture silencieuse.

## Référence unique
Une entité = un ID stable et une fiche principale ; les index, récits et bilans renvoient par lien Obsidian complet depuis la racine du coffre. Nommer les fiches « Type — Nom » ou « Nom (qualificatif) » pour les homonymes, les récits « J+NNN — Date », les bilans « J+NNN — Date — Historique », les sauvegardes « Reprise — Branche — ID ». Les modèles sont identifiés par « Modèle — ». Ne pas créer un second dossier de données pour un même fait.

| Domaine | Référence maîtresse |
| --- | --- |
| Identité / biographie | [[Mes aventures RPG/Aeden/01 — Personnage principal/Fiche du personnage principal|Fiche du personnage principal]] |
| Statistiques / ressources | [[Mes aventures RPG/Aeden/01 — Personnage principal/Statistiques et ressources|Statistiques et ressources]] |
| Rang de Classe / Profession, EXP | [[Mes aventures RPG/Aeden/01 — Personnage principal/Classe et Profession|Classe et Profession]] |
| Compétences | [[Mes aventures RPG/Aeden/01 — Personnage principal/Compétences/Index — Compétences|Index — Compétences]] et fiches individuelles |
| Équipement et objets | [[Mes aventures RPG/Aeden/05 — Inventaire et finances/Inventaire actuel|Inventaire actuel]] et fiches objets |
| Flux financiers | [[Mes aventures RPG/Aeden/05 — Inventaire et finances/Transactions|Transactions]] ; soldes par compte |
| Faits joués | [[Mes aventures RPG/Aeden/02 — Journal et chronologie/Chronologie générale|Chronologie générale]] et récit source |
| Relations, lieux, missions, espèces | Fiches individuelles de la section concernée |
| Dernière scène | [[Mes aventures RPG/Aeden/00 — Accueil et reprise/État de reprise actuel|État de reprise actuel]] |

## Métadonnées YAML
Conserver type, campagne, branche_narrative, id, statut_documentaire, visibilite, version, date_univers, derniere_validation, sources. Attribuer un ID pérenne à la création réelle ; null signifie non renseigné. Statuts documentaires : modele, a_definir, propose, valide, archive ; index, reference et protocole pour les documents administratifs. Ne pas confondre validation d'une fiche et rencontre jouée. Dates du monde en chaînes, sources en liste ; liens internes complets pour éviter collisions entre aventures. À définir = non défini ; Inconnu = existe mais non connu ; Sans objet = non applicable ; Secret = réservé. N/A et ? selon affichage officiel.

## Maintenance par ChatGPT
Avant une réponse : lire la reprise, les fiches touchées, les sources, vérifier chronologie, connaissances et contraintes. Après action : noter le fait joué, mettre à jour chaque référence maîtresse et ses dépendances, conserver historique, contrôler argent/EXP/temps, puis enregistrer et relire GitHub. À la fin d'une journée ou chapitre important, préparer l'état et conserver les instantanés nécessaires. Une sauvegarde non enregistrée n'est pas disponible. Une nouvelle branche narrative n'est pas automatiquement une branche Git.

## Confidentialité
Le dossier joueur et le registre Fondateur sont distincts. Les métadonnées ne constituent pas un contrôle d'accès : toute personne ayant accès au dépôt privé peut lire les notes, et Git conserve l'historique. Ne jamais transclure de secrets dans les vues joueur.

## Contrôles complémentaires
[[Mes aventures RPG/Aeden/18 — Contrôle de cohérence/Protocole de maintenance]] · [[Mes aventures RPG/Aeden/18 — Contrôle de cohérence/Schéma des données]]. Les registres structurés sont les seules sources numériques maîtresses. Maintenir des liens qualifiés dans tout le coffre. Ne pas exposer les dossiers Fondateur dans les vues joueur. La date d’effet et la source priment sur la simple date de modification Git.
