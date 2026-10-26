const fs = require('fs');
const axios = require('axios');
const cheerio = require('cheerio');

// ========== CONFIG ==========
const INPUT_FILE = './monstres.json';
const OUTPUT_FILE = './monstres_avec_skills.json';
const DELAY_MS = 2000; // Délai pour éviter le ban
const MAX_RETRIES = 3;

// ========== FONCTIONS ==========
function formatWikiUrl(nom) {
  return nom
    .replace(/[^\w\s-]/g, '')
    .replace(/\s+/g, '_')
    .toLowerCase();
}

async function fetchWikiPage(nom) {
  const url = `https://monsterlegends.fandom.com/wiki/${formatWikiUrl(nom)}`;
  try {
    const response = await axios.get(url, {
      headers: { 'User-Agent': 'Mozilla/5.0' } // Évite le blocage
    });
    return response.data;
  } catch (error) {
    console.error(`❌ Erreur pour ${nom} : ${error.message}`);
    return null;
  }
}

function extractSkills(html, nom) {
  const $ = cheerio.load(html);
  const skills = [];

  // Sélecteur principal : tableau "Skills"
  const skillTables = $('h2:contains("Skills"), h2:contains("Compétences")');
  if (skillTables.length > 0) {
    const table = skillTables.first().nextAll('table').first();
    table.find('tr').each((i, row) => {
      const cells = $(row).find('td, th');
      if (cells.length >= 2) {
        const name = $(cells[0]).text().trim();
        const desc = $(cells[1]).text().trim();
        if (name && desc && !name.includes('Level') && !name.includes('Cooldown')) {
          skills.push({ name, desc });
        }
      }
    });
  }

  // Sélecteur alternatif : listes à puces
  if (skills.length === 0) {
    $('div.mw-parser-output ul').each((i, ul) => {
      const prevText = $(ul).prev().text().toLowerCase();
      if (prevText.includes('skill') || prevText.includes('compétence')) {
        $(ul).find('li').each((j, li) => {
          const text = $(li).text().trim();
          if (text) {
            const match = text.match(/^([^—–:]+)[—–:]\s*(.+)$/);
            if (match) {
              skills.push({ name: match[1].trim(), desc: match[2].trim() });
            } else {
              skills.push({ name: text, desc: '' });
            }
          }
        });
      }
    });
  }

  // Sélecteur pour les monstres avec des infobox (ex: Pandaken)
  if (skills.length === 0) {
    const infobox = $('table.infobox');
    infobox.find('tr').each((i, row) => {
      const th = $(row).find('th').text().toLowerCase();
      if (th.includes('skill') || th.includes('active skill') || th.includes('compétence')) {
        const td = $(row).find('td');
        const skillText = td.text().trim();
        if (skillText) {
          skills.push({ name: nom, desc: skillText }); // Nom par défaut si non trouvé
        }
      }
    });
  }

  return skills;
}

async function scrapeMonsterSkills(monstre, retries = MAX_RETRIES) {
  const { nom, id } = monstre;
  console.log(`🔍 Scraping : ${nom} (ID: ${id})...`);

  const html = await fetchWikiPage(nom);
  if (!html) {
    if (retries > 0) {
      console.log(`↻ Réessai (${retries} tentative(s) restante(s))...`);
      await new Promise(resolve => setTimeout(resolve, DELAY_MS));
      return scrapeMonsterSkills(monstre, retries - 1);
    }
    return null;
  }

  const skills = extractSkills(html, nom);
  console.log(`✅ ${skills.length} compétence(s) trouvées pour ${nom}.`);
  return skills;
}

// ========== SCRIPT PRINCIPAL ==========
async function main() {
  // Lire le fichier JSON
  let monstres;
  try {
    const data = fs.readFileSync(INPUT_FILE, 'utf-8');
    monstres = JSON.parse(data);
    console.log(`📄 Fichier chargé : ${monstres.length} monstres à traiter.`);
  } catch (error) {
    console.error(`❌ Impossible de lire ${INPUT_FILE} : ${error.message}`);
    process.exit(1);
  }

  // Traiter chaque monstre
  const monstresAvecSkills = [];
  for (const monstre of monstres) {
    const skills = await scrapeMonsterSkills(monstre);
    monstresAvecSkills.push({
      ...monstre,
      skills: skills || []
    });
    await new Promise(resolve => setTimeout(resolve, DELAY_MS));
  }

  // Sauvegarder le résultat
  fs.writeFileSync(OUTPUT_FILE, JSON.stringify(monstresAvecSkills, null, 2), 'utf-8');
  console.log(`💾 Résultat sauvegardé dans ${OUTPUT_FILE}.`);

  const avecSkills = monstresAvecSkills.filter(m => m.skills.length > 0).length;
  console.log(`📊 ${avecSkills}/${monstres.length} monstres ont des compétences.`);
}

main().catch(error => {
  console.error('❌ Erreur fatale :', error);
  process.exit(1);
});