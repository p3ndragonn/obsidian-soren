"""Audit documentaire en lecture seule ; ne jamais afficher les données confidentielles."""
import json, re, sys
from pathlib import Path
from decimal import Decimal, InvalidOperation
from urllib.parse import unquote
from collections import defaultdict
import yaml

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT.parents[1]
STAT = ("FOR","VIT","END","AGI","SAG","PER")
RANKS = "F E D C B A S SS SSS EX MY LG Demi-dieu Divinité".split()
RARITIES = RANKS[:12] + ["Semi-unique","Unique"]
KEYS = ("type","campagne","branche_narrative","statut_documentaire","visibilite","version","id","date_univers","derniere_validation","sources")
STATUS = {"modele","a_definir","propose","valide","archive","index","reference","protocole"}
def seuil(n):
    return 100 + 20*(n-1) + 2*(n-1)**2

def decimal(v):
    if v is None: return None
    if not isinstance(v,str): raise ValueError("montant non textuel")
    x=Decimal(v)
    if not x.is_finite(): raise ValueError("montant non fini")
    return x

def audit(root=ROOT, vault=VAULT, details=None):
    errors=[]; warnings=[]
    context=None
    def err(code):
        errors.append(code)
        if details is not None: details.append((code, context))
    def warn(code): warnings.append(code)
    def load(p):
        try:
            d=json.loads((root/p).read_text(encoding="utf-8"))
            if not isinstance(d,dict) or d.get("schema_version") != 1: raise ValueError()
            return d
        except (OSError,ValueError): err("JSON absent ou invalide"); return {}
    def unique(rows, code):
        seen=set()
        for row in rows:
            key=row.get("id")
            if not isinstance(key,str) or not key or key in seen: err(code)
            else: seen.add(key)
        return seen
    all_files=[p for p in vault.rglob("*") if p.is_file() and ".git" not in p.parts]
    lookup=defaultdict(list)
    for p in all_files:
        rel=p.relative_to(vault).as_posix()
        for key in {rel,p.name,rel[:-3] if rel.endswith(".md") else rel,p.stem if p.suffix==".md" else p.name}:
            lookup[key].append(p)
    ids=set()
    for p in sorted(root.rglob("*.md")):
        context=p.relative_to(root).as_posix()
        s=p.read_text(encoding="utf-8")
        if p.name!="README.md":
            try:
                m=re.match(r"\A---\s*\n(.*?)\n---\s*\n",s,re.S)
                if not m: raise ValueError()
                d=yaml.safe_load(m.group(1))
                if not isinstance(d,dict) or not all(k in d for k in KEYS): raise ValueError()
                if d["campagne"]!="Aeden" or d["statut_documentaire"] not in STATUS or d["visibilite"] not in {"joueur","fondateur","public","prive","secret"} or not isinstance(d["version"],int) or not isinstance(d["sources"],list): err("métadonnées non conformes")
                if d["statut_documentaire"]=="valide" and not d["id"]: err("ID de fiche validée absent")
                if d["id"]:
                    key=(d["branche_narrative"],d["id"])
                    if key in ids and d["statut_documentaire"]!="archive": err("ID de fiche dupliqué")
                    if d["statut_documentaire"]!="archive": ids.add(key)
            except (ValueError,TypeError,yaml.YAMLError): err("YAML invalide ou incomplet")
        for target in re.findall(r"\[\[([^\]\n]+)\]\]",s):
            t=target.split("|")[0].split("#")[0].strip()
            if not t: continue
            candidates=lookup.get(t,[])
            if not candidates: err("lien Obsidian introuvable")
            elif len(candidates)>1: err("lien Obsidian ambigu")
        for target in re.findall(r"\]\(([^)\n]+)\)",s):
            t=unquote(target.split("#")[0].strip())
            if not t or "://" in t or t.startswith(("mailto:","data:")): continue
            # Les chemins avec espaces doivent être encodés ou entre chevrons.
            if not (p.parent/t.strip("<>")).is_file(): err("lien Markdown local ou média introuvable")
    # Les fichiers actuels utilisent des liens qualifiés à la racine du coffre.
    context="05 — Inventaire et finances/Données/finances.json"
    f=load("05 — Inventaire et finances/Données/finances.json")
    comptes=f.get("comptes",[]); tx=f.get("transactions",[])
    unique(comptes,"ID compte absent ou dupliqué"); unique(tx,"ID transaction absent ou dupliqué")
    by={(c.get("branche"),c.get("id")):c for c in comptes}
    sums=defaultdict(Decimal); unknown=set(); transfers=defaultdict(list)
    for t in tx:
        try:
            key=(t.get("branche"),t.get("compte_id"))
            if key not in by or not t.get("source") or not isinstance(t.get("ordre"),int): err("transaction non rattachée ou non sourcée")
            if t.get("statut") not in {"effectue","prevu","annule"}: err("statut transaction invalide")
            if t.get("statut")!="effectue": continue
            n=decimal(t.get("montant"))
            if n is None: unknown.add(key); warn("montant effectif inconnu")
            else: sums[key]+=n
            if t.get("transfert_id"): transfers[(key[0],t["transfert_id"])].append((key,n))
        except (ValueError,InvalidOperation,TypeError): err("montant transaction invalide")
    for key,c in by.items():
        try:
            a,b=decimal(c.get("solde_initial")),decimal(c.get("solde_actuel"))
            if a is None or key in unknown:
                if b is not None: warn("solde non reconstituable")
            elif b is None: warn("solde actuel non renseigné")
            elif a+sums[key]!=b: err("solde incohérent")
        except (ValueError,InvalidOperation): err("solde invalide")
    for rows in transfers.values():
        if len(rows)!=2 or rows[0][0]==rows[1][0] or any(n is None for _,n in rows) or sum(n for _,n in rows)!=0: err("transfert non équilibré")
    context="14 — Progression et combats/Données/progression.json"
    g=load("14 — Progression et combats/Données/progression.json")
    chars=g.get("personnages",[]); events=g.get("evenements",[])
    unique(chars,"ID progression absent ou dupliqué"); unique(events,"ID événement progression absent ou dupliqué")
    states={(c.get("branche"),c.get("id"),domain): (c.get(domain,{}).get("niveau"),c.get(domain,{}).get("exp")) for c in chars for domain in ("classe","profession")}
    if any(not isinstance(e.get("ordre"),int) for e in events): err("ordre progression invalide")
    for e in sorted(events,key=lambda e:e.get("ordre") if isinstance(e.get("ordre"),int) else -1):
        key=(e.get("branche"),e.get("personnage_id"),e.get("domaine"))
        before=(e.get("niveau_avant"),e.get("exp_avant")); after=(e.get("niveau_apres"),e.get("exp_apres"))
        if key not in states or not e.get("source"): err("progression sans personnage ou source")
        if key in states and all(x is not None for x in (*states[key],*before)) and states[key]!=before: err("rupture de continuité EXP")
        if e.get("type")=="exp":
            n,x=before; gain=e.get("gain_exp")
            if all(isinstance(a,int) and not isinstance(a,bool) for a in (n,x,gain,*after)) and 1<=n<=100 and x>=0 and gain>=0:
                x+=gain
                while n<100 and x>=seuil(n): x-=seuil(n); n+=1
                if (n,x)!=after and not e.get("exception"): err("calcul EXP incohérent")
            else: warn("EXP non calculable ou invalide")
        elif e.get("type") not in {"ascension","correction"} or not e.get("exception"): err("évolution spéciale sans référence")
        states[key]=after
    context="01 — Personnage principal/Données/statut.json"
    st=load("01 — Personnage principal/Données/statut.json")
    if st.get("rang_personnel") is not None and st["rang_personnel"] not in RANKS: err("rang personnel invalide")
    for domain in ("classe","profession"):
        d=st.get(domain,{}); n=d.get("niveau"); x=d.get("exp")
        if d.get("rarete") is not None and d["rarete"] not in RARITIES: err("rareté invalide")
        if n is not None and (not isinstance(n,int) or not 1<=n<=100): err("niveau invalide")
        if x is not None and (not isinstance(x,int) or x<0 or isinstance(n,int) and 1<=n<100 and x>=seuil(n)): err("EXP courante invalide")
        key=(st.get("branche"),st.get("personnage_id"),domain)
        if key in states and all(v is not None for v in (*states[key],n,x)) and states[key]!=(n,x): err("statut et journal EXP divergent")
    perm=st.get("permanentes",{}); eq=st.get("equipement",{})
    for k in STAT:
        p,b=perm.get(k),eq.get(k)
        if p is not None and (not isinstance(p,int) or p<0): err("statistique permanente invalide")
        if b is not None and (not isinstance(b,int) or b<0 or isinstance(p,int) and b>p*12//100): err("bonus équipement hors plafond")
    for r,k in (("HP","VIT"),("MP","SAG"),("EP","END")):
        d=st.get("ressources",{}).get(r,{}); a,b,m=(d.get(i) for i in ("actuelle","base","maximum")); p=perm.get(k)
        if isinstance(p,int) and b is not None and b!=10*p: err("maximum de base incohérent")
        if any(v is not None and (not isinstance(v,(int,float)) or v<0) for v in (a,b,m)): err("ressource invalide")
        if isinstance(a,(int,float)) and isinstance(m,(int,float)) and a>m: err("ressource actuelle supérieure au maximum")
    titles=st.get("titres_actifs",[])
    if len(titles)>5 or len(set(titles))!=len(titles): err("titres actifs invalides")
    context="11 — Calendrier et événements/Données/echeances.json"
    agenda=load("11 — Calendrier et événements/Données/echeances.json").get("evenements",[])
    unique(agenda,"ID échéance absent ou dupliqué")
    for e in agenda:
        a,b=e.get("ordre_creation"),e.get("ordre_realisation")
        if e.get("statut") not in {"prevu","conditionnel","realise","annule","reporte"} or not e.get("source") or not isinstance(a,int): err("échéance invalide")
        if e.get("statut")=="realise" and (not isinstance(b,int) or not isinstance(a,int) or b<a): err("chronologie échéance incohérente")
    context="00 — Accueil et reprise/Données/reprise.json"
    r=load("00 — Accueil et reprise/Données/reprise.json")
    if r.get("sauvegarde_id"):
        if any(r.get(k) is None for k in ("branche","ordre","date_univers","lieu","source_scene")): err("reprise incomplète")
        for k in ("source_scene","point_majeur"):
            v=r.get(k)
            if v and not (vault/v).is_file(): err("référence reprise introuvable")
    elif any(r.get(k) is not None for k in ("point_majeur","source_scene","ordre")): err("reprise sans identifiant")
    return errors,warnings

if __name__=="__main__":
    from collections import Counter
    import argparse, os
    parser=argparse.ArgumentParser(description="Audit en lecture seule")
    parser.add_argument("--details", action="store_true", help="Chemins des erreurs, uniquement en local")
    args=parser.parse_args()
    details=[] if args.details and not os.getenv("GITHUB_ACTIONS") else None
    try:
        e,w=audit(details=details)
    except Exception:
        print("ERREUR : structure inattendue ; vérifier localement sans publier les données.")
        sys.exit(2)
    for kind,rows in (("ERREUR",e),("VIGILANCE",w)):
        for code,count in sorted(Counter(rows).items()): print(f"{kind} : {code} ({count})")
    if details is not None:
        for code, context in details: print(f"{context}: {code}")
    print(f"Audit : {len(e)} erreur(s), {len(w)} vigilance(s). Aucune modification.")
    sys.exit(1 if e else 0)
