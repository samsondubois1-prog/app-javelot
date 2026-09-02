let allCompetitions = [];
let favorites = JSON.parse(localStorage.getItem('javelot_favs')) || [];

// Charger les données JSON
fetch('competitions.json')
    .then(response => {
        if (!response.ok) throw new Error("Erreur de chargement");
        return response.json();
    })
    .then(data => {
        allCompetitions = data;
        updateFavCount();
    })
    .catch(err => {
        console.error(err);
        document.getElementById('results').innerHTML = `<p class="error">Impossible de charger les compétitions.</p>`;
    });

document.getElementById('searchBtn').addEventListener('click', searchCompetitions);

function searchCompetitions() {
    const query = document.getElementById('searchInput').value.trim().toLowerCase();
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = '';

    if (!query) return;

    const filtered = allCompetitions.filter(c => 
        (c.dept && c.dept.toLowerCase() === query) ||
        (c.ville && c.ville.toLowerCase().includes(query)) ||
        (c.nom && c.nom.toLowerCase().includes(query))
    );

    if (filtered.length === 0) {
        resultsContainer.innerHTML = '<p>Aucune compétition trouvée pour cette recherche.</p>';
        return;
    }

    filtered.forEach(c => {
        resultsContainer.appendChild(createCard(c));
    });
}

function createCard(c) {
    const card = document.createElement('div');
    card.className = 'card';

    const isFav = favorites.some(f => f.nom === c.nom && f.date === c.date);

    card.innerHTML = `
        <h3>${c.nom}</h3>
        <p><strong>Lieu :</strong> ${c.lieu} (${c.ville})</p>
        <p><strong>Date :</strong> ${c.date}</p>
        <p><strong>Épreuve :</strong> ${c.epreuve}</p>
        <div class="card-actions">
            ${c.lien ? `<a href="${c.lien}" target="_blank" class="link-btn">🔗 Plus d'infos</a>` : ''}
            <button class="fav-btn ${isFav ? 'is-fav' : ''}" onclick="toggleFav('${c.nom}', '${c.date}')">
                ${isFav ? '⭐ Dans ton calendrier' : '☆ Ajouter au calendrier'}
            </button>
        </div>
    `;
    return card;
}

function toggleFav(nom, date) {
    const index = favorites.findIndex(f => f.nom === nom && f.date === date);
    if (index > -1) {
        favorites.splice(index, 1);
    } else {
        const comp = allCompetitions.find(c => c.nom === nom && c.date === date);
        if (comp) favorites.push(comp);
    }

    localStorage.setItem('javelot_favs', JSON.stringify(favorites));
    updateFavCount();

    // Rafraîchir l'affichage
    searchCompetitions();
    renderFavs();
}

function updateFavCount() {
    document.getElementById('favCount').textContent = favorites.length;
}

function showTab(tab) {
    if (tab === 'search') {
        document.getElementById('searchSection').style.display = 'block';
        document.getElementById('favsSection').style.display = 'none';
        document.getElementById('btnSearchTab').classList.add('active');
        document.getElementById('btnFavTab').classList.remove('active');
    } else {
        document.getElementById('searchSection').style.display = 'none';
        document.getElementById('favsSection').style.display = 'block';
        document.getElementById('btnFavTab').classList.add('active');
        document.getElementById('btnSearchTab').classList.remove('active');
        renderFavs();
    }
}

function renderFavs() {
    const favContainer = document.getElementById('favResults');
    favContainer.innerHTML = '';

    if (favorites.length === 0) {
        favContainer.innerHTML = '<p>Tu n\'as encore ajouté aucune compétition à ton calendrier.</p>';
        return;
    }

    // Trier par date croissante
    favorites.sort((a, b) => new Date(a.date) - new Date(b.date));

    favorites.forEach(c => {
        favContainer.appendChild(createCard(c));
    });
}
