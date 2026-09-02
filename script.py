import json

def charger_toutes_les_competitions():
    return [
        # Cher (18)
        {
            "nom": "Meeting de Lancers du Cher", 
            "ville": "Bourges", 
            "dept": "18", 
            "region": "Centre-Val de Loire", 
            "date": "2026-10-15", 
            "epreuve": "Javelot 700g (Cadet)", 
            "lieu": "Stade Séraucourt",
            "lien": "https://centrevaldeloire.athle.fr/"
        },
        {
            "nom": "Challenge Automnal de Lancers", 
            "ville": "Vierzon", 
            "dept": "18", 
            "region": "Centre-Val de Loire", 
            "date": "2026-11-22", 
            "epreuve": "Javelot Cadet 2", 
            "lieu": "Stade Robert Barran",
            "lien": "https://centrevaldeloire.athle.fr/"
        },
        {
            "nom": "Critérium d'Automne de Lancers", 
            "ville": "Saint-Amand-Montrond", 
            "dept": "18", 
            "region": "Centre-Val de Loire", 
            "date": "2026-10-28", 
            "epreuve": "Javelot U18", 
            "lieu": "Stade Municipal",
            "lien": "https://centrevaldeloire.athle.fr/"
        },

        # Voisins proches (36, 41, 45, 58)
        {
            "nom": "Meeting de Châteauroux", 
            "ville": "Châteauroux", 
            "dept": "36", 
            "region": "Centre-Val de Loire", 
            "date": "2026-10-04", 
            "epreuve": "Javelot U18 M/F", 
            "lieu": "Stade Tissier",
            "lien": "https://centrevaldeloire.athle.fr/"
        },
        {
            "nom": "Meeting de Rentrée des Lancers", 
            "ville": "Blois", 
            "dept": "41", 
            "region": "Centre-Val de Loire", 
            "date": "2026-10-11", 
            "epreuve": "Javelot 700g", 
            "lieu": "Stade Alliet",
            "lien": "https://centrevaldeloire.athle.fr/"
        },
        {
            "nom": "Critérium Estival de Lancers", 
            "ville": "Orléans", 
            "dept": "45", 
            "region": "Centre-Val de Loire", 
            "date": "2026-09-19", 
            "epreuve": "Javelot 700g (Cadet)", 
            "lieu": "Stade de la Source",
            "lien": "https://centrevaldeloire.athle.fr/"
        },
        {
            "nom": "Journée Lancers Longs Nivernaise", 
            "ville": "Nevers", 
            "dept": "58", 
            "region": "Bourgogne-Franche-Comté", 
            "date": "2026-11-08", 
            "epreuve": "Javelot U18 M/F", 
            "lieu": "Stade de la Baratte",
            "lien": "https://lbfc.athle.fr/"
        },

        # Autres régions de France
        {
            "nom": "Critérium Francilien de Lancers", 
            "ville": "Paris", 
            "dept": "75", 
            "region": "Île-de-France", 
            "date": "2026-10-25", 
            "epreuve": "Javelot U18", 
            "lieu": "Stade Charléty",
            "lien": "https://lifa.athle.fr/"
        },
        {
            "nom": "Meeting Automnal de Lyon", 
            "ville": "Lyon", 
            "dept": "69", 
            "region": "Auvergne-Rhône-Alpes", 
            "date": "2026-10-18", 
            "epreuve": "Javelot Cadet M/F", 
            "lieu": "Stade de Balmont",
            "lien": "https://aura.athle.fr/"
        }
    ]

def generer_json():
    donnees = charger_toutes_les_competitions()
    with open('competitions.json', 'w', encoding='utf-8') as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2)
    print(f"Succès : {len(donnees)} compétitions enregistrées avec leurs liens !")

if __name__ == "__main__":
    generer_json()
