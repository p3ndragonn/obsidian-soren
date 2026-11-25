---
type: protocole
campagne: Aeden
branche_narrative: null
statut_documentaire: protocole
visibilite: joueur
version: 4
id: null
date_univers: null
derniere_validation: null
sources: []
---

# Protocole de maintenance

1. Lire l’état de reprise unique, les fiches maîtresses concernées et les sources officielles du projet.
2. Vérifier acteur, branche, chronologie, connaissances, ressources et contraintes. Le temps est figé en Mode Fondateur.
3. Résoudre l’action sans décider à la place du joueur. Séparer faits, hypothèses et secrets.
4. Attribuer des IDs stables aux nouveaux faits et conserver la source jouée ; mettre à jour transactions, progression, agenda et fiches touchées.
5. Contrôler les dépendances, soldes, EXP, liens, versions, visibilité et chronologie. Les anomalies ne sont jamais corrigées sans preuve.
6. Enregistrer les changements significatifs ensemble, idéalement un commit par scène importante ou bilan ; vérifier le commit et relire les données. En cas d’échec, signaler les changements non sauvegardés.
7. Actualiser [[Mes aventures RPG/Aeden/00 — Accueil et reprise/État de reprise actuel]] ; archiver les anciennes versions datées et conserver les points majeurs réellement enregistrés, avec complément Fondateur séparé.
8. À la reprise, restituer la dernière scène sans action nouvelle et attendre le joueur.

Ne pas faire de commit pour une simple question. Un point de continuité n’est pas forcément un point majeur. Les dossiers documentaires ne constituent pas une séparation technique des droits d’accès.

## Obligation de fin de journée (AED-FON-001)
À chaque coucher/fin de journée, synchroniser toutes les fiches affectées et les nouveaux éléments, index, données structurées, illustrations officielles accessibles, bilan et archive de reprise. Vérifier cohérence et commit avant d'annoncer la réussite ; signaler les exceptions restantes. Ne pas attendre une nouvelle demande du joueur.

## Prévention des erreurs d'audit
Avant chaque sauvegarde GitHub, inclure les dix champs YAML du schéma sur chaque fiche Markdown (hors README.md) ; `derniere_validation: null` si aucune date de validation n'est établie. Une fiche validée doit avoir un ID stable. Respecter les champs JSON, les statuts exacts sans accents et les références de fichiers réelles. Renseigner branche, ordre et source pour chaque transaction ; rapprocher le solde sans créer de mouvement fictif. Renseigner les échéances avec `ordre_creation`, source et statut exact, y compris `conditionnel` si nécessaire. Ne pas transformer une sauvegarde quotidienne en point majeur sans qualification explicite. En local, `python audit.py --details` depuis le dossier de contrôle identifie les fichiers concernés ; les logs GitHub restent agrégés pour ne pas exposer les données confidentielles.

## EXP immédiate (AED-FON-006)
Établir rang et niveau individuels avant résolution, suivre dégâts par participant si groupe. À chaque élimination, appliquer règlement p.6, notifier gain et cumul de classe, inscrire ID spécimen/gain/avant/après au registre de progression et conserver jusqu'à synchronisation. Aucun double crédit, ne pas reporter le calcul à la fin du jour. Si donnée absente, arbitrer explicitement sans changer un fait établi.


## Suivi mana Aedan et EXP profession
AED-FON-007 : 95 MP/min passifs propres à Aedan, plafond effectif, suivre minutes écoulées et débits séparément, jamais de surplus. À l'avenir, créditer activités professionnelles justifiées par règlement p.6 et annexe C art.C.4, selon difficulté/qualité/nouveauté/apprentissage ; consigner IDs, éviter répétitions triviales et double crédit. Convention d'arbitrage documentée au registre, pas de barème universel imposé.
