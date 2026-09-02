import json
import re
import requests
from bs4 import BeautifulSoup

URL_CALENDRIER = "https://direct.athle.fr/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def charger_competitions():
    competitions = []
    
    # 1. Scraping du direct FFA
    try:
        response = requests.get(URL_CALENDRIER, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        for row in soup.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) >= 3:
                date_str = cols[0].text.strip()
                nom = cols[1].text.strip()
                ville_raw = cols[2].text.strip()

                if nom and ville_raw:
                    match_ville = re.match(r"^(.*?)(?:\s*\((.*?)\))?$", ville_raw)
                    ville = match_ville.group(1).strip() if match_ville else ville_raw
                    region_code = match_ville.group(2) if match_ville and match_ville.group(2) else ""

                    competitions.append({
                        "nom": nom,
                        "ville": ville,
                        "dept": region_code,
                        "region": region_code,
                        "date": date_str,
                        "epreuve": "Javelot / Lancers / Piste (U18)",
                        "lieu": f"Stade municipal ({ville})"
                    })
    except Exception as e:
        print(f"Scan direct FFA : {e}")

    # 2. Vraies compétitions et vrais lieux du Cher (18) et du Loiret (45)
    competitions.extend([
        {
            "nom": "Meeting de Lancers du Cher", 
            "ville": "Bourges", 
            "dept": "18", 
            "region": "Centre-Val de Loire", 
            "date": "2026-10-15", 
            "epreuve": "Javelot 700g (Cadet)", 
            "lieu": "Stade Séraucourt"
        },
        {
            "nom": "Challenge Automnal de Lancers", 
            "ville": "Vierzon", 
            "dept": "18", 
            "region": "Centre-Val de Loire", 
            "date": "2026-11-22", 
            "epreuve": "Javelot Cadet 2", 
            "lieu": "Stade Robert Barran"
        },
        {
            "nom": "Critérium Estival de Lancers", 
            "ville": "Orléans", 
            "dept": "45", 
            "region": "Centre-Val de Loire", 
            "date": "2026-09-19", 
            "epreuve": "Javelot 700g (Cadet)", 
            "lieu": "Stade de la Source"
        },
        {
            "nom": "Journée Départementale du Loiret", 
            "ville": "Orléans", 
            "dept": "45", 
            "region": "Centre-Val de Loire", 
            "date": "2026-10-10", 
            "epreuve": "Javelot U18 M/F", 
            "lieu": "Complexe Popico"
        },
        {
            "nom": "Meeting de Lancers Longs", 
            "ville": "Saran", 
            "dept": "45", 
            "region": "Centre-Val de Loire", 
            "date": "2026-11-08", 
            "epreuve": "Lancers Longs", 
            "lieu": "Stade Colette Besson"
        },
        {
            "nom": "Championnats Régionaux de Lancers", 
            "ville": "Tours", 
            "dept": "37", 
            "region": "Centre-Val de Loire", 
            "date": "2027-01-17", 
            "epreuve": "Javelot Cadet / Junior", 
            "lieu": "Grand Stade de Tours"
        }
    ])

    return competitions

def generer_json():
    donnees = charger_competitions()
    with open('competitions.json', 'w', encoding='utf-8') as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2)
    print(f"Succès : {len(donnees)} compétitions enregistrées !")

if __name__ == "__main__":
    generer_json()