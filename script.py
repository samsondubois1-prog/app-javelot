import json
import re
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Liste des liens vers les calendriers des Ligues Régionales
SOURCES_LIGUES = [
    {"region": "Centre-Val de Loire", "url": "https://centrevaldeloire.athle.fr/"},
    {"region": "Île-de-France", "url": "https://lifa.athle.fr/"},
    {"region": "Nouvelle-Aquitaine", "url": "https://lanouvelleaquitaine.athle.fr/"},
    {"region": "Auvergne-Rhône-Alpes", "url": "https://aura.athle.fr/"},
    {"region": "Hauts-de-France", "url": "https://nordpasdecalais.athle.fr/"},
    {"region": "Occitanie", "url": "https://licoroc.athle.fr/"},
    {"region": "Grand Est", "url": "https://lgesta.athle.fr/"},
    {"region": "Bretagne", "url": "https://bretagne.athle.fr/"},
    {"region": "Normandie", "url": "https://normandie.athle.fr/"},
    {"region": "Pays de la Loire", "url": "https://liguepaysdelaloire.athle.fr/"},
    {"region": "Bourgogne-Franche-Comté", "url": "https://lbfc.athle.fr/"},
    {"region": "PACA", "url": "https://paca.athle.fr/"}
]

def charger_toutes_les_competitions():
    competitions = []

    # 1. Exemple de base nationale couvrant plusieurs régions
    base_nationale = [
        # Centre-Val de Loire
        {"nom": "Meeting de Lancers du Cher", "ville": "Bourges", "dept": "18", "region": "Centre-Val de Loire", "date": "2026-10-15", "epreuve": "Javelot 700g (Cadet)", "lieu": "Stade Séraucourt"},
        {"nom": "Challenge Automnal de Lancers", "ville": "Vierzon", "dept": "18", "region": "Centre-Val de Loire", "date": "2026-11-22", "epreuve": "Javelot Cadet 2", "lieu": "Stade Robert Barran"},
        {"nom": "Critérium Estival de Lancers", "ville": "Orléans", "dept": "45", "region": "Centre-Val de Loire", "date": "2026-09-19", "epreuve": "Javelot 700g (Cadet)", "lieu": "Stade de la Source"},
        {"nom": "Meeting de Châteauroux", "ville": "Châteauroux", "dept": "36", "region": "Centre-Val de Loire", "date": "2026-10-04", "epreuve": "Javelot U18", "lieu": "Stade Tissier"},
        
        # Île-de-France
        {"nom": "Critérium Francilien de Lancers", "ville": "Paris", "dept": "75", "region": "Île-de-France", "date": "2026-10-25", "epreuve": "Javelot U18", "lieu": "Stade Charléty"},
        {"nom": "Meeting des Jeunes du 91", "ville": "Evry", "dept": "91", "region": "Île-de-France", "date": "2026-11-15", "epreuve": "Javelot 700g", "lieu": "Complexe Sportif"},

        # Auvergne-Rhône-Alpes
        {"nom": "Meeting Automnal de Lyon", "ville": "Lyon", "dept": "69", "region": "Auvergne-Rhône-Alpes", "date": "2026-10-18", "epreuve": "Javelot Cadet M/F", "lieu": "Stade de Balmont"},
        
        # Nouvelle-Aquitaine
        {"nom": "Journée Lancers Longs", "ville": "Poitiers", "dept": "86", "region": "Nouvelle-Aquitaine", "date": "2026-11-01", "epreuve": "Javelot U18", "lieu": "Stade Rebeilleau"},
        
        # Hauts-de-France
        {"nom": "Meeting Nord Lancers", "ville": "Lille", "dept": "59", "region": "Hauts-de-France", "date": "2026-10-11", "epreuve": "Javelot 700g", "lieu": "Complexe Lery"}
    ]

    competitions.extend(base_nationale)
    return competitions

def generer_json():
    donnees = charger_toutes_les_competitions()
    with open('competitions.json', 'w', encoding='utf-8') as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2)
    print(f"Succès : {len(donnees)} compétitions nationales enregistrées !")

if __name__ == "__main__":
    generer_json()
import json

def charger_toutes_les_competitions():
    # Base de données nationale des épreuves de lancers U18
    return [
        # Centre-Val de Loire (18, 36, 45, 37)
        {"nom": "Meeting de Lancers du Cher", "ville": "Bourges", "dept": "18", "region": "Centre-Val de Loire", "date": "2026-10-15", "epreuve": "Javelot 700g (Cadet)", "lieu": "Stade Séraucourt"},
        {"nom": "Challenge Automnal de Lancers", "ville": "Vierzon", "dept": "18", "region": "Centre-Val de Loire", "date": "2026-11-22", "epreuve": "Javelot Cadet 2", "lieu": "Stade Robert Barran"},
        {"nom": "Meeting de Châteauroux", "ville": "Châteauroux", "dept": "36", "region": "Centre-Val de Loire", "date": "2026-10-04", "epreuve": "Javelot U18 M/F", "lieu": "Stade Tissier"},
        {"nom": "Critérium Estival de Lancers", "ville": "Orléans", "dept": "45", "region": "Centre-Val de Loire", "date": "2026-09-19", "epreuve": "Javelot 700g (Cadet)", "lieu": "Stade de la Source"},
        {"nom": "Championnats Régionaux", "ville": "Tours", "dept": "37", "region": "Centre-Val de Loire", "date": "2027-01-17", "epreuve": "Javelot Cadet / Junior", "lieu": "Grand Stade de Tours"},
        
        # Île-de-France (75, 91, 77)
        {"nom": "Critérium Francilien de Lancers", "ville": "Paris", "dept": "75", "region": "Île-de-France", "date": "2026-10-25", "epreuve": "Javelot U18", "lieu": "Stade Charléty"},
        {"nom": "Meeting des Jeunes du 91", "ville": "Evry", "dept": "91", "region": "Île-de-France", "date": "2026-11-15", "epreuve": "Javelot 700g", "lieu": "Complexe Jean Bouin"},

        # Auvergne-Rhône-Alpes (69, 38)
        {"nom": "Meeting Automnal de Lyon", "ville": "Lyon", "dept": "69", "region": "Auvergne-Rhône-Alpes", "date": "2026-10-18", "epreuve": "Javelot Cadet M/F", "lieu": "Stade de Balmont"},
        
        # Nouvelle-Aquitaine (86, 33)
        {"nom": "Journée Lancers Longs", "ville": "Poitiers", "dept": "86", "region": "Nouvelle-Aquitaine", "date": "2026-11-01", "epreuve": "Javelot U18", "lieu": "Stade Rebeilleau"},
        {"nom": "Meeting de Bordeaux", "ville": "Bordeaux", "dept": "33", "region": "Nouvelle-Aquitaine", "date": "2026-10-20", "epreuve": "Javelot 700g", "lieu": "Stade Chaban-Delmas"},
        
        # Hauts-de-France (59)
        {"nom": "Meeting Nord Lancers", "ville": "Lille", "dept": "59", "region": "Hauts-de-France", "date": "2026-10-11", "epreuve": "Javelot 700g", "lieu": "Complexe Lery"}
    ]

def generer_json():
    donnees = charger_toutes_les_competitions()
    with open('competitions.json', 'w', encoding='utf-8') as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2)
    print(f"Succès : {len(donnees)} compétitions enregistrées !")

if __name__ == "__main__":
    generer_json()
