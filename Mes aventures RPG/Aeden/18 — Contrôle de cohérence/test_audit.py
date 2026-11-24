import unittest, tempfile, json
from pathlib import Path
from audit import audit, seuil

class TestAudit(unittest.TestCase):
    def test_seuil(self):
        self.assertEqual(seuil(1),100)
        self.assertEqual(seuil(28),2098)
    def test_fixture(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            # Jeux de données isolés : aucune dépendance à la sauvegarde réelle.
            fixtures = {
                "05 — Inventaire et finances/Données/finances.json": {"schema_version":1,"comptes":[],"transactions":[]},
                "14 — Progression et combats/Données/progression.json": {"schema_version":1,"personnages":[],"evenements":[]},
                "01 — Personnage principal/Données/statut.json": {"schema_version":1},
                "11 — Calendrier et événements/Données/echeances.json": {"schema_version":1,"evenements":[]},
                "00 — Accueil et reprise/Données/reprise.json": {"schema_version":1}
            }
            for rel, data in fixtures.items():
                q=root/rel
                q.parent.mkdir(parents=True,exist_ok=True)
                q.write_text(json.dumps(data),encoding="utf-8")
            p=root/"05 — Inventaire et finances/Données/finances.json"
            f={"schema_version":1,"comptes":[{"id":"A","branche":"test","solde_initial":"10.10","solde_actuel":"9.90"}],"transactions":[{"id":"T","branche":"test","compte_id":"A","ordre":1,"source":"test","montant":"-0.20","statut":"effectue"}]}
            p.write_text(json.dumps(f))
            self.assertEqual(audit(root,root)[0],[])
            f["comptes"][0]["solde_actuel"]="10"
            p.write_text(json.dumps(f))
            self.assertIn("solde incohérent",audit(root,root)[0])
            f["comptes"][0]["solde_actuel"]="9.90"
            f["transactions"].append(f["transactions"][0])
            p.write_text(json.dumps(f))
            self.assertIn("ID transaction absent ou dupliqué",audit(root,root)[0])
if __name__=="__main__": unittest.main()
