---
type: transactions
campagne: Aeden
branche_narrative: null
statut_documentaire: a_definir
visibilite: joueur
version: 2
id: null
date_univers: null
derniere_validation: null
sources: []
---

# Transactions

Journal maître des mouvements en Pièces, sans solde initial inventé.

| ID unique | Branche | Date/heure | Compte | Contrepartie | Nature | Entrée P | Sortie P | Statut | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Seuls les mouvements effectivement encaissés ou payés modifient la trésorerie. Prévisions et promesses restent dans les engagements. Un transfert entre comptes comporte deux écritures reliées par un même identifiant de transfert ; ne pas le compter comme revenu global. Un solde inconnu reste inconnu ; relever les écarts sans correction inventée.

## Référence numérique
[Registre structuré des finances](Données/finances.json) : source maîtresse des montants, comptes et soldes. Enregistrer le solde résultant par compte, calculable depuis la base et les écritures, ou inconnu. La table ci-dessus est une vue narrative liée aux IDs, non un second journal indépendant.
