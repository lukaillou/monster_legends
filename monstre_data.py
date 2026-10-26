import json

# 1. Tes données d'origine (Corrigé : une seule liste de dictionnaires)
anciennes_donnees = [
  {"id":1,"nom":"Treezard","role":["support"],"element":"nature","rarity":"common","stats":{"hp":2777,"attack":1125,"speed":1000}},
  {"id":2,"nom":"Firesaur","role":["attacker"],"element":"feu","rarity":"common","stats":{"hp":2480,"attack":1375,"speed":875}},
  {"id":5,"nom":"Rockilla","role":["tank"],"element":"terre","rarity":"common","stats":{"hp":3521,"attack":875,"speed":875}},
  {"id":11,"nom":"Rhynex","role":["attacker"],"element":["nature","foudre"],"rarity":"epic","stats":{"hp":17855,"attack":2280,"speed":2990}},
  {"id":12,"nom":"Rabidex","role":["curser"],"element":["nature","foudre"],"rarity":"epic","stats":{"hp":15899,"attack":2700,"speed":2930}},
  {"id":13,"nom":"Gigram","role":["attacker"],"element":["feu","foudre"],"rarity":"uncommon","stats":{"hp":5041,"attack":1736,"speed":1736}},
  {"id":14,"nom":"Thundenix","role":["attacker"],"element":"feu","rarity":"rare","stats":{"hp":3100,"attack":3600,"speed":320}},
  {"id":17,"nom":"Mersnake","role":["monster"],"element":"eau","rarity":"common","stats":{"hp":2777,"attack":1125,"speed":1000}},
  {"id":26,"nom":"Tyrannoking","role":["attacker"],"element":"ténèbres","rarity":"common","stats":{"hp":2480,"attack":1150,"speed":875}},
  {"id":39,"nom":"Pandalf","role":["support"],"element":["nature","magie"],"rarity":"epic","stats":{"hp":15899,"attack":2600,"speed":2930}},
  {"id":185,"nom":"General Atum","role":["tank"],"element":["magie","terre"],"rarity":"legendary","stats":{"hp":31969,"attack":3454,"speed":3399}},
  {"id":308,"nom":"Stinger S1","role":["attacker"],"element":["métal","magie"],"rarity":"legendary","stats":{"hp":26540,"attack":3454,"speed":3465}},
  {"id":371,"nom":"Chill Bill","role":["attacker"],"element":["magie","eau"],"rarity":"legendary","stats":{"hp":26540,"attack":3509,"speed":3388}},
  {"id":576,"nom":"Warmaster Elvira","role":["support"],"element":["magie","lumière"],"rarity":"legendary","stats":{"hp":41922,"attack":3476,"speed":3498}},
  {"id":579,"nom":"Warmaster Thalassa","role":["controler"],"element":["magie","eau"],"rarity":"legendary","stats":{"hp":40414,"attack":3399,"speed":3542}},
  {"id":606,"nom":"Zameleon","role":["support"],"element":["magie","terre"],"rarity":"legendary","stats":{"hp":33779,"attack":3322,"speed":3531}},
  {"id":613,"nom":"Dunn Ra","role":["tank"],"element":["magie","ténèbres"],"rarity":"legendary","stats":{"hp":46446,"attack":3465,"speed":3388}},
  {"id":626,"nom":"Pierceid","role":["controler"],"element":["magie","ténèbres"],"rarity":"legendary","stats":{"hp":37096,"attack":3355,"speed":3575}},
  {"id":647,"nom":"Ugluk","role":["attacker"],"element":["magie","terre"],"rarity":"legendary","stats":{"hp":34080,"attack":3685,"speed":3476}},
  {"id":660,"nom":"Ursus","role":["attacker"],"element":["magie","eau"],"rarity":"legendary","stats":{"hp":37700,"attack":3619,"speed":3421}},
  {"id":667,"nom":"Grakon","role":["controler"],"element":["magie","nature"],"rarity":"legendary","stats":{"hp":40414,"attack":3465,"speed":3575}},
  {"id":682,"nom":"Arumel","role":["attacker"],"element":"lumière","rarity":"mythic","stats":{"hp":57907,"attack":5951,"speed":4785}},
  {"id":691,"nom":"Tayni","role":["support"],"element":"nature","rarity":"mythic","stats":{"hp":54891,"attack":5489,"speed":4862}},
  {"id":699,"nom":"Dr. Wattz","role":["attacker"],"element":"foudre","rarity":"mythic","stats":{"hp":59716,"attack":5808,"speed":4774}},
  {"id":702,"nom":"Kawthor","role":["attacker","tank"],"element":"eau","rarity":"mythic","stats":{"hp":60320,"attack":5896,"speed":4488}},
  {"id":858,"nom":"Lord Nebotus","role":["attacker"],"element":"ténèbres","rarity":"mythic","stats":{"hp":91686,"attack":8800,"speed":6369}},
  {"id":917,"nom":"Dark VoltaiK","role":["attacker"],"element":"ténèbres","rarity":"mythic","stats":{"hp":112798,"attack":10417,"speed":7480}},
  {"id":930,"nom":"Darmith Khan","role":["attacker"],"element":"feu","rarity":"mythic","stats":{"hp":122148,"attack":10560,"speed":7502}},
  {"id":964,"nom":"Elvira Demonslayer","role":["attacker"],"element":["feu","lumière"],"rarity":"mythic","stats":{"hp":125465,"attack":10758,"speed":7722}},
  {"id":997,"nom":"Roborabbit","role":["attacker"],"element":["foudre","lumière"],"rarity":"mythic","stats":{"hp":131799,"attack":10824,"speed":8151}},
  {"id":1036,"nom":"Calamitabyss","role":["attacker"],"element":"eau","rarity":"mythic","stats":{"hp":142355,"attack":11088,"speed":8206}},
  {"id":1048,"nom":"Goliathess","role":["tank"],"element":"terre","rarity":"mythic","stats":{"hp":149593,"attack":10758,"speed":8184}},
  {"id":1054,"nom":"Darko","role":["attacker"],"element":"feu","rarity":"mythic","stats":{"hp":141752,"attack":11154,"speed":8272}},
  {"id":1171,"nom":"Gloverd","role":["tank"],"element":["eau","nature"],"rarity":"mythic","stats":{"hp":394795,"attack":15697,"speed":11121}},
  {"id":1265,"nom":"Kevlar","role":["support"],"element":["lumière","eau"],"rarity":"mythic","stats":{"hp":555848,"attack":22176,"speed":16280}},
  {"id":1267,"nom":"Rabbapulta","role":["controler"],"element":["foudre","magie"],"rarity":"mythic","stats":{"hp":436716,"attack":17072,"speed":12518}},
  {"id":1269,"nom":"The Chronicler","role":["controler"],"element":["magie","métal"],"rarity":"mythic","stats":{"hp":509100,"attack":20416,"speed":14168}},
  {"id":1333,"nom":"Hexer Alb","role":["support"],"element":["magie","ténèbres"],"rarity":"mythic","stats":{"hp":557367,"attack":22176,"speed":16280}},
  {"id":1361,"nom":"Violentine","role":["tank"],"element":["nature","feu"],"rarity":"mythic","stats":{"hp":564596,"attack":22407,"speed":15719}},
  {"id":1364,"nom":"Sentinella","role":["tank"],"element":["magie","ténèbres"],"rarity":"mythic","stats":{"hp":564595,"attack":22528,"speed":15697}},
  {"id":1378,"nom":"Zeit","role":["support"],"element":["feu","métal"],"rarity":"mythic","stats":{"hp":628836,"attack":24695,"speed":17688}},
  {"id":1488,"nom":"Vipper Prickett","role":["attacker"],"element":["foudre","feu"],"rarity":"mythic","stats":{"hp":773906,"attack":29073,"speed":21439}}
]

# 2. Charge ton fichier JSON existant
try:
    with open('monstres.json', 'r', encoding='utf-8') as f:
        nouveaux_monstres = json.load(f)
except FileNotFoundError:
    print("Erreur : Le fichier 'monstres.json' est introuvable.")
    nouveaux_monstres = []

# 3. Créer le mapping (correspondance)
mapping_roles = {m["nom"]: m["role"] for m in anciennes_donnees}

# 4. Mise à jour des rôles
compteur = 0
for monstre in nouveaux_monstres:
    nom = monstre.get("nom")
    if nom in mapping_roles:
        monstre["role"] = mapping_roles[nom]
        compteur += 1

# 5. Sauvegarde finale propre (corrige les Ã© en é)
with open('monstres_final.json', 'w', encoding='utf-8') as f:
    json.dump(nouveaux_monstres, f, ensure_ascii=False, indent=2)

print(f"Succès ! {compteur} rôles ont été injectés dans 'monstres_final.json'.")