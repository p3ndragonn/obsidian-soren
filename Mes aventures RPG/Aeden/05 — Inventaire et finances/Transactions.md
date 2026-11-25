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
