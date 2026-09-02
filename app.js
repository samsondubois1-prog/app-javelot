async function searchCompetitions() {
  const query = document.getElementById("cityInput").value.toLowerCase().trim();
  const resultsContainer = document.getElementById("results");
  resultsContainer.innerHTML = "<p>Recherche en cours...</p>";

  if (query === "") {
    resultsContainer.innerHTML = "<p>Veuillez entrer une ville ou un numéro de département (ex: Bourges, Orléans, 18, 45...).</p>";
    return;
  }

  try {
    // Lecture du fichier JSON généré par Python (avec paramètre anti-cache)
    const response = await fetch('competitions.json?v=' + Date.now());
    
    if (!response.ok) {
      throw new Error("Fichier competitions.json introuvable.");
    }
    
    const competitions = await response.json();

    // Filtre par ville OU département
    const filtered = competitions.filter(comp => {
      const matchVille = comp.ville && comp.ville.toLowerCase().includes(query);
      const matchDept = comp.dept && comp.dept.toString().toLowerCase() === query;
      return matchVille || matchDept;
    });

    resultsContainer.innerHTML = "";

    if (filtered.length === 0) {
      resultsContainer.innerHTML = `<p>Aucune compétition trouvée pour "${query}".</p>`;
      return;
    }

    // Affichage des cartes de compétition
    filtered.forEach(comp => {
      const card = document.createElement("div");
      card.className = "card";
      card.innerHTML = `
        <h3>${comp.nom}</h3>
        <p><strong>Lieu :</strong> ${comp.lieu || comp.ville} (${comp.ville})</p>
        <p><strong>Date :</strong> ${comp.date}</p>
        <span class="badge">${comp.epreuve}</span>
      `;
      resultsContainer.appendChild(card);
    });

  } catch (error) {
    resultsContainer.innerHTML = "<p style='color: red;'>Erreur : impossible de charger 'competitions.json'. Assure-toi que le script Python a bien été exécuté et que le serveur local tourne.</p>";
  }
}