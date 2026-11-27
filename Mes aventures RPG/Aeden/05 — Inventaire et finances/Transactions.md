---
type: transactions
campagne: Aeden
branche_narrative: null
statut_documentaire: a_definir
visibilite: joueur
version: 3
id: null
date_univers: null
derniere_validation: null
sources: []
---

# Transactions

Journal maître des mouvements en Pièces, sans solde initial inventé.

| ID unique | Branche | Date/heure | Compte | Contrepartie | Nature | Entrée P | Sortie P | Statut | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AED-T001 | principale | J1 12:43 | Aedan | Blackwell Défense Arcanotech | Expertise et restauration | 25000 | 0 | effectué | Bilan J1 |
| AED-T002 | principale | J1 16:31 | Aedan | Les Délices d’Ambre | Dessert | 0 | 68 | effectué | Bilan J1 |
| AED-T003 | principale | J1 avant 18:48 | Aedan | Edric Valmont | Automate et plaques | 0 | 32000 | effectué | Bilan J1 |

Seuls les mouvements effectivement encaissés ou payés modifient la trésorerie. Prévisions et promesses restent dans les engagements. Un transfert entre comptes comporte deux écritures reliées par un même identifiant de transfert ; ne pas le compter comme revenu global. Un solde inconnu reste inconnu ; relever les écarts sans correction inventée.

## Référence numérique
[Registre structuré des finances](Données/finances.json) : source maîtresse des montants, comptes et soldes. Enregistrer le solde résultant par compte, calculable depuis la base et les écritures, ou inconnu. La table ci-dessus est une vue narrative liée aux IDs, non un second journal indépendant.


## AED-J7-008 — état actualisé
19:08 AED-T004 −85 P, solde342847 ;22:23 AED-T005 −9600 P vers entreprise, solde333247. Eryan−60 P,49526 ; entreprise +9600 P référence999600 hors frais non chiffrés.
[[Mes aventures RPG/Aeden/02 — Journal et chronologie/Récits/Jour 7 — Bilan.md]]

## J8 — 22 Doréal jusqu'à14:26
| ID | Compte | Heure | Nature | Montant P | Solde après |
|---|---|---|---|---:|---:|
| AED-T006 | Aedan | 11:21–29 | Frais constitution | -3000 | 330247 |
| AED-T007 | Aedan | 12:27 | Apport capital | -100000 | 230247 |
| AED-T007-C | Arche Industries | 12:27 | Contrepartie AED-T007 | +100000 | 100000 |
| AED-T008 | Aedan | 13:29–34 | Déjeuner | -48 | 230199 |
| AED-T009 | Aedan | 13:53 | Contrat spectral intégral | -9680 | 220519 |
Transfert capital interne au périmètre patrimonial, ni charge ni chiffre d'affaires.
[[Mes aventures RPG/Aeden/02 — Journal et chronologie/Récits/Jour 8 — Bilan intermédiaire.md]]
