# This is a simple Pokedex implemented in Python
# The Pokedex is a dictionary that maps Pokemon names to their properties

Pokedex = {
    "Bulbasaur": {
        "type": "grass, poison",
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "special_attack": 65,
        "special_defense": 65,
        "speed": 45
    },
    "Ivysaur": {
        "type": "grass, poison",
        "hp": 60,
        "attack": 62,
        "defense": 63,
        "special_attack": 80,
        "special_defense": 80,
        "speed": 60
    },
    "Venusaur": {
        "type": "grass, poison",
        "hp": 80,
        "attack": 82,
        "defense": 83,
        "special_attack": 100,
        "special_defense": 100,
        "speed": 80
    },
    "Charmander": {
        "type": "fire",
        "hp": 39,
        "attack": 52,
        "defense": 43,
        "special_attack": 60,
        "special_defense": 50,
        "speed": 65
    },
    "Charmeleon": {
        "type": "fire",
        "hp": 58,
        "attack": 64,
        "defense": 58,
        "special_attack": 80,
        "special_defense": 65,
        "speed": 80
    },
    "Charizard": {
        "type": "fire, flying",
        "hp": 78,
        "attack": 84,
        "defense": 78,
        "special_attack": 109,
        "special_defense": 85,
        "speed": 100
    },
    "Squirtle": {
        "type": "water",
        "hp": 44,
        "attack": 48,
        "defense": 65,
        "special_attack": 50,
        "special_defense": 64,
        "speed": 43
    },
    "Wartortle": {
        "type": "water",
        "hp": 59,
        "attack": 63,
        "defense": 80,
        "special_attack": 65,
        "special_defense": 80,
        "speed": 58
    },
    "Blastoise": {
        "type": "water",
        "hp": 79,
        "attack": 83,
        "defense": 100,
        "special_attack": 85,
        "special_defense": 105,
        "speed": 78
    },
    "Caterpie": {
        "type": "bug",
        "hp": 45,
        "attack": 30,
        "defense": 35,
        "special_attack": 20,
        "special_defense": 20,
        "speed": 45
    },
    "Metapod": {
        "type": "bug",
        "hp": 50,
        "attack": 20,
        "defense": 55,
        "special_attack": 25,
        "special_defense": 25,
        "speed": 30
    },
    "Butterfree": {
        "type": "bug, flying",
        "hp": 60,
        "attack": 45,
        "defense": 50,
        "special_attack": 90,
        "special_defense": 80,
        "speed": 70
    },
    "Weedle": {
        "type": "bug, poison",
        "hp": 40,
        "attack": 35,
        "defense": 30,
        "special_attack": 20,
        "special_defense": 20,
        "speed": 50
    },
    "Kakuna": {
        "type": "bug, poison",
        "hp": 45,
        "attack": 25,
        "defense": 50,
        "special_attack": 25,
        "special_defense": 25,
        "speed": 35
    },
    "Beedrill": {
        "type": "bug, poison",
        "hp": 65,
        "attack": 90,
        "defense": 40,
        "special_attack": 45,
        "special_defense": 80,
        "speed": 75
    },
    "Pidgey": {
        "type": "normal, flying",
        "hp": 40,
        "attack": 45,
        "defense": 40,
        "special_attack": 35,
        "special_defense": 35,
        "speed": 56
    },
    "Pidgeotto": {
        "type": "normal, flying",
        "hp": 63,
        "attack": 60,
        "defense": 55,
        "special_attack": 50,
        "special_defense": 50,
        "speed": 71
    },
    "Pidgeot": {
        "type": "normal, flying",
        "hp": 83,
        "attack": 80,
        "defense": 75,
        "special_attack": 70,
        "special_defense": 70,
        "speed": 101
    },
    "Rattata": {
        "type": "normal",
        "hp": 30,
        "attack": 56,
        "defense": 35,
        "special_attack": 25,
        "special_defense": 35,
        "speed": 72
    },
    "Raticate": {
        "type": "normal",
        "hp": 55,
        "attack": 81,
        "defense": 60,
        "special_attack": 50,
        "special_defense": 70,
        "speed": 97
    },
    "Spearow": {
        "type": "normal, flying",
        "hp": 40,
        "attack": 60,
        "defense": 30,
        "special_attack": 31,
        "special_defense": 31,
        "speed": 70
    },
    "Fearow": {
        "type": "normal, flying",
        "hp": 65,
        "attack": 90,
        "defense": 65,
        "special_attack": 61,
        "special_defense": 61,
        "speed": 100
    },
    "Ekans": {
        "type": "poison",
        "hp": 35,
        "attack": 60,
        "defense": 44,
        "special_attack": 40,
        "special_defense": 54,
        "speed": 55
    },
    "Arbok": {
        "type": "poison",
        "hp": 60,
        "attack": 85,
        "defense": 69,
        "special_attack": 65,
        "special_defense": 79,
        "speed": 80
    },
    "Pikachu": {
        "type": "electric",
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "special_attack": 50,
        "special_defense": 50,
        "speed": 90
    },
    "Raichu": {
        "type": "electric",
        "hp": 60,
        "attack": 90,
        "defense": 55,
        "special_attack": 90,
        "special_defense": 80,
        "speed": 110
    },
    "Sandshrew": {
        "type": "ground",
        "hp": 50,
        "attack": 75,
        "defense": 85,
        "special_attack": 20,
        "special_defense": 30,
        "speed": 40
    },
    "Sandslash": {
        "type": "ground",
        "hp": 75,
        "attack": 100,
        "defense": 110,
        "special_attack": 45,
        "special_defense": 55,
        "speed": 65
    },
    "Nidoran♀": {
        "type": "poison",
        "hp": 55,
        "attack": 47,
        "defense": 52,
        "special_attack": 40,
        "special_defense": 40,
        "speed": 41
    },
    "Nidorina": {
        "type": "poison",
        "hp": 70,
        "attack": 62,
        "defense": 67,
        "special_attack": 55,
        "special_defense": 55,
        "speed": 56
    },
    "Nidoqueen": {
        "type": "poison, ground",
        "hp": 90,
        "attack": 92,
        "defense": 87,
        "special_attack": 75,
        "special_defense": 85,
        "speed": 76
    },
    "Nidoran♂": {
        "type": "poison",
        "hp": 46,
        "attack": 57,
        "defense": 40,
        "special_attack": 40,
        "special_defense": 40,
        "speed": 50
    },
    "Nidorino": {
        "type": "poison",
        "hp": 61,
        "attack": 72,
        "defense": 57,
        "special_attack": 55,
        "special_defense": 55,
        "speed": 65
    },
    "Nidoking": {
        "type": "poison, ground",
        "hp": 81,
        "attack": 102,
        "defense": 77,
        "special_attack": 85,
        "special_defense": 75,
        "speed": 85
    },
    "Clefairy": {
        "type": "fairy",
        "hp": 70,
        "attack": 45,
        "defense": 48,
        "special_attack": 60,
        "special_defense": 65,
        "speed": 35
    },
    "Clefable": {
        "type": "fairy",
        "hp": 95,
        "attack": 70,
        "defense": 73,
        "special_attack": 95,
        "special_defense": 90,
        "speed": 60
    },
    "Vulpix": {
        "type": "fire",
        "hp": 38,
        "attack": 41,
        "defense": 40,
        "special_attack": 50,
        "special_defense": 65,
        "speed": 65
    },
    "Ninetales": {
        "type": "fire",
        "hp": 73,
        "attack": 76,
        "defense": 75,
        "special_attack": 81,
        "special_defense": 100,
        "speed": 100
    },
    "Jigglypuff": {
        "type": "normal, fairy",
        "hp": 115,
        "attack": 45,
        "defense": 20,
        "special_attack": 45,
        "special_defense": 25,
        "speed": 20
    },
    "Wigglytuff": {
        "type": "normal, fairy",
        "hp": 140,
        "attack": 70,
        "defense": 45,
        "special_attack": 85,
        "special_defense": 50,
        "speed": 45
    },
    "Zubat": {
        "type": "poison, flying",
        "hp": 40,
        "attack": 45,
        "defense": 35,
        "special_attack": 30,
        "special_defense": 40,
        "speed": 55
    },
    "Golbat": {
        "type": "poison, flying",
        "hp": 75,
        "attack": 80,
        "defense": 70,
        "special_attack": 65,
        "special_defense": 75,
        "speed": 90
    },
    "Oddish": {
        "type": "grass, poison",
        "hp": 45,
        "attack": 50,
        "defense": 55,
        "special_attack": 75,
        "special_defense": 65,
        "speed": 30
    },
    "Gloom": {
        "type": "grass, poison",
        "hp": 60,
        "attack": 65,
        "defense": 70,
        "special_attack": 85,
        "special_defense": 75,
        "speed": 40
    },
    "Vileplume": {
        "type": "grass, poison",
        "hp": 75,
        "attack": 80,
        "defense": 85,
        "special_attack": 110,
        "special_defense": 90,
        "speed": 50
    },
    "Paras": {
        "type": "bug, grass",
        "hp": 35,
        "attack": 70,
        "defense": 55,
        "special_attack": 45,
        "special_defense": 55,
        "speed": 25
    },
    "Parasect": {
        "type": "bug, grass",
        "hp": 60,
        "attack": 95,
        "defense": 80,
        "special_attack": 60,
        "special_defense": 80,
        "speed": 30
    },
    "Venonat": {
        "type": "bug, poison",
        "hp": 60,
        "attack": 55,
        "defense": 50,
        "special_attack": 40,
        "special_defense": 55,
        "speed": 45
    },
    "Venomoth": {
        "type": "bug, poison",
        "hp": 70,
        "attack": 65,
        "defense": 60,
        "special_attack": 90,
        "special_defense": 75,
        "speed": 90
    },
    "Diglett": {
        "type": "ground",
        "hp": 10,
        "attack": 55,
        "defense": 25,
        "special_attack": 35,
        "special_defense": 45,
        "speed": 95
    },
    "Dugtrio": {
        "type": "ground",
        "hp": 35,
        "attack": 100,
        "defense": 50,
        "special_attack": 50,
        "special_defense": 70,
        "speed": 120
    },
    "Meowth": {
        "type": "normal",
        "hp": 40,
        "attack": 45,
        "defense": 35,
        "special_attack": 40,
        "special_defense": 40,
        "speed": 90
    },
    "Persian": {
        "type": "normal",
        "hp": 65,
        "attack": 70,
        "defense": 60,
        "special_attack": 65,
        "special_defense": 65,
        "speed": 115
    },
    "Psyduck": {
        "type": "water",
        "hp": 50,
        "attack": 52,
        "defense": 48,
        "special_attack": 65,
        "special_defense": 50,
        "speed": 55
    },
    "Golduck": {
        "type": "water",
        "hp": 80,
        "attack": 82,
        "defense": 78,
        "special_attack": 95,
        "special_defense": 80,
        "speed": 85
    },
    "Mankey": {
        "type": "fighting",
        "hp": 40,
        "attack": 80,
        "defense": 35,
        "special_attack": 35,
        "special_defense": 45,
        "speed": 70
    },
    "Primeape": {
        "type": "fighting",
        "hp": 65,
        "attack": 105,
        "defense": 60,
        "special_attack": 60,
        "special_defense": 70,
        "speed": 95
    },
    "Growlithe": {
        "type": "fire",
        "hp": 55,
        "attack": 70,
        "defense": 45,
        "special_attack": 70,
        "special_defense": 50,
        "speed": 60
    },
    "Arcanine": {
        "type": "fire",
        "hp": 90,
        "attack": 110,
        "defense": 80,
        "special_attack": 100,
        "special_defense": 80,
        "speed": 95
    },
    "Poliwag": {
        "type": "water",
        "hp": 40,
        "attack": 50,
        "defense": 40,
        "special_attack": 40,
        "special_defense": 40,
        "speed": 90
    },
    "Poliwhirl": {
        "type": "water",
        "hp": 65,
        "attack": 65,
        "defense": 65,
        "special_attack": 50,
        "special_defense": 50,
        "speed": 90
    },
    "Poliwrath": {
        "type": "water, fighting",
        "hp": 90,
        "attack": 95,
        "defense": 95,
        "special_attack": 70,
        "special_defense": 90,
        "speed": 70
    },
    "Abra": {
        "type": "psychic",
        "hp": 25,
        "attack": 20,
        "defense": 15,
        "special_attack": 105,
        "special_defense": 55,
        "speed": 90
    },
    "Kadabra": {
        "type": "psychic",
        "hp": 40,
        "attack": 35,
        "defense": 30,
        "special_attack": 120,
        "special_defense": 70,
        "speed": 105
    },
    "Alakazam": {
        "type": "psychic",
        "hp": 55,
        "attack": 50,
        "defense": 45,
        "special_attack": 135,
        "special_defense": 95,
        "speed": 120
    },
    "Machop": {
        "type": "fighting",
        "hp": 70,
        "attack": 80,
        "defense": 50,
        "special_attack": 35,
        "special_defense": 35,
        "speed": 35
    },
    "Machoke": {
        "type": "fighting",
        "hp": 80,
        "attack": 100,
        "defense": 70,
        "special_attack": 50,
        "special_defense": 60,
        "speed": 45
    },
    "Machamp": {
        "type": "fighting",
        "hp": 90,
        "attack": 130,
        "defense": 80,
        "special_attack": 65,
        "special_defense": 85,
        "speed": 55
    },
    "Bellsprout": {
        "type": "grass, poison",
        "hp": 50,
        "attack": 75,
        "defense": 35,
        "special_attack": 70,
        "special_defense": 30,
        "speed": 40
    },
    "Weepinbell": {
        "type": "grass, poison",
        "hp": 65,
        "attack": 90,
        "defense": 50,
        "special_attack": 85,
        "special_defense": 45,
        "speed": 55
    },
    "Victreebel": {
        "type": "grass, poison",
        "hp": 80,
        "attack": 105,
        "defense": 65,
        "special_attack": 100,
        "special_defense": 70,
        "speed": 70
    },
    "Tentacool": {
        "type": "water, poison",
        "hp": 40,
        "attack": 40,
        "defense": 35,
        "special_attack": 50,
        "special_defense": 100,
        "speed": 70
    },
    "Tentacruel": {
        "type": "water, poison",
        "hp": 80,
        "attack": 70,
        "defense": 65,
        "special_attack": 80,
        "special_defense": 120,
        "speed": 100
    },
    "Geodude": {
        "type": "rock, ground",
        "hp": 40,
        "attack": 80,
        "defense": 100,
        "special_attack": 30,
        "special_defense": 30,
        "speed": 20
    },
    "Graveler": {
        "type": "rock, ground",
        "hp": 55,
        "attack": 95,
        "defense": 115,
        "special_attack": 45,
        "special_defense": 45,
        "speed": 35
    },
    "Golem": {
        "type": "rock, ground",
        "hp": 80,
        "attack": 120,
        "defense": 130,
        "special_attack": 55,
        "special_defense": 65,
        "speed": 45
    },
    "Ponyta": {
        "type": "fire",
        "hp": 50,
        "attack": 85,
        "defense": 55,
        "special_attack": 65,
        "special_defense": 65,
        "speed": 90
    },
    "Rapidash": {
        "type": "fire",
        "hp": 65,
        "attack": 100,
        "defense": 70,
        "special_attack": 80,
        "special_defense": 80,
        "speed": 105
    },
    "Slowpoke": {
        "type": "water, psychic",
        "hp": 90,
        "attack": 65,
        "defense": 65,
        "special_attack": 40,
        "special_defense": 40,
        "speed": 15
    },
    "Slowbro": {
        "type": "water, psychic",
        "hp": 95,
        "attack": 75,
        "defense": 110,
        "special_attack": 100,
        "special_defense": 80,
        "speed": 30
    },
    "Magnemite": {
        "type": "electric, steel",
        "hp": 25,
        "attack": 35,
        "defense": 70,
        "special_attack": 95,
        "special_defense": 55,
        "speed": 45
    },
    "Magneton": {
        "type": "electric, steel",
        "hp": 50,
        "attack": 60,
        "defense": 95,
        "special_attack": 120,
        "special_defense": 70,
        "speed": 70
    },
    "Farfetch'd": {
        "type": "normal, flying",
        "hp": 52,
        "attack": 90,
        "defense": 55,
        "special_attack": 58,
        "special_defense": 62,
        "speed": 60
    },
    "Doduo": {
        "type": "normal, flying",
        "hp": 35,
        "attack": 85,
        "defense": 45,
        "special_attack": 35,
        "special_defense": 35,
        "speed": 75
    },
    "Dodrio": {
        "type": "normal, flying",
        "hp": 60,
        "attack": 110,
        "defense": 70,
        "special_attack": 60,
        "special_defense": 60,
        "speed": 100
    },
    "Seel": {
        "type": "water",
        "hp": 65,
        "attack": 45,
        "defense": 55,
        "special_attack": 45,
        "special_defense": 70,
        "speed": 45
    },
    "Dewgong": {
        "type": "water, ice",
        "hp": 90,
        "attack": 70,
        "defense": 80,
        "special_attack": 70,
        "special_defense": 95,
        "speed": 70
    },
    "Grimer": {
        "type": "poison",
        "hp": 80,
        "attack": 80,
        "defense": 50,
        "special_attack": 40,
        "special_defense": 50,
        "speed": 25
    },
    "Muk": {
        "type": "poison",
        "hp": 105,
        "attack": 105,
        "defense": 75,
        "special_attack": 65,
        "special_defense": 100,
        "speed": 50
    },
    "Shellder": {
        "type": "water",
        "hp": 30,
        "attack": 65,
        "defense": 100,
        "special_attack": 45,
        "special_defense": 25,
        "speed": 40
    },
    "Cloyster": {
        "type": "water, ice",
        "hp": 50,
        "attack": 95,
        "defense": 180,
        "special_attack": 85,
        "special_defense": 45,
        "speed": 70
    },
    "Gastly": {
        "type": "ghost, poison",
        "hp": 30,
        "attack": 35,
        "defense": 30,
        "special_attack": 100,
        "special_defense": 35,
        "speed": 80
    },
    "Haunter": {
        "type": "ghost, poison",
        "hp": 45,
        "attack": 50,
        "defense": 45,
        "special_attack": 115,
        "special_defense": 55,
        "speed": 95
    },
    "Gengar": {
        "type": "ghost, poison",
        "hp": 60,
        "attack": 65,
        "defense": 60,
        "special_attack": 130,
        "special_defense": 75,
        "speed": 110
    },
    "Onix": {
        "type": "rock, ground",
        "hp": 35,
        "attack": 45,
        "defense": 160,
        "special_attack": 30,
        "special_defense": 45,
        "speed": 70
    },
    "Drowzee": {
        "type": "psychic",
        "hp": 60,
        "attack": 48,
        "defense": 45,
        "special_attack": 43,
        "special_defense": 90,
        "speed": 42
    },
    "Hypno": {
        "type": "psychic",
        "hp": 85,
        "attack": 73,
        "defense": 70,
        "special_attack": 73,
        "special_defense": 115,
        "speed": 67
    },
    "Krabby": {
        "type": "water",
        "hp": 30,
        "attack": 105,
        "defense": 90,
        "special_attack": 25,
        "special_defense": 25,
        "speed": 50
    },
    "Kingler": {
        "type": "water",
        "hp": 55,
        "attack": 130,
        "defense": 115,
        "special_attack": 50,
        "special_defense": 50,
        "speed": 75
    },
    "Voltorb": {
        "type": "electric",
        "hp": 40,
        "attack": 30,
        "defense": 50,
        "special_attack": 55,
        "special_defense": 55,
        "speed": 100
    },
    "Electrode": {
        "type": "electric",
        "hp": 60,
        "attack": 50,
        "defense": 70,
        "special_attack": 80,
        "special_defense": 80,
        "speed": 140
    },
    "Exeggcute": {
        "type": "grass, psychic",
        "hp": 60,
        "attack": 40,
        "defense": 80,
        "special_attack": 60,
        "special_defense": 45,
        "speed": 40
    },
    "Exeggutor": {
        "type": "grass, psychic",
        "hp": 95,
        "attack": 95,
        "defense": 85,
        "special_attack": 125,
        "special_defense": 65,
        "speed": 55
    },
    "Cubone": {
        "type": "ground",
        "hp": 50,
        "attack": 50,
        "defense": 95,
        "special_attack": 40,
        "special_defense": 50,
        "speed": 35
    },
    "Marowak": {
        "type": "ground",
        "hp": 60,
        "attack": 80,
        "defense": 110,
        "special_attack": 50,
        "special_defense": 80,
        "speed": 45
    },
    "Hitmonlee": {
        "type": "fighting",
        "hp": 50,
        "attack": 120,
        "defense": 53,
        "special_attack": 35,
        "special_defense": 110,
        "speed": 87
    },
    "Hitmonchan": {
        "type": "fighting",
        "hp": 50,
        "attack": 105,
        "defense": 79,
        "special_attack": 35,
        "special_defense": 110,
        "speed": 76
    },
    "Lickitung": {
        "type": "normal",
        "hp": 90,
        "attack": 55,
        "defense": 75,
        "special_attack": 60,
        "special_defense": 75,
        "speed": 30
    },
    "Koffing": {
        "type": "poison",
        "hp": 40,
        "attack": 65,
        "defense": 95,
        "special_attack": 60,
        "special_defense": 45,
        "speed": 35
    },
    "Weezing": {
        "type": "poison",
        "hp": 65,
        "attack": 90,
        "defense": 120,
        "special_attack": 85,
        "special_defense": 70,
        "speed": 60
    },
    "Rhyhorn": {
        "type": "ground, rock",
        "hp": 80,
        "attack": 85,
        "defense": 95,
        "special_attack": 30,
        "special_defense": 30,
        "speed": 25
    },
    "Rhydon": {
        "type": "ground, rock",
        "hp": 105,
        "attack": 130,
        "defense": 120,
        "special_attack": 45,
        "special_defense": 45,
        "speed": 40
    },
    "Chansey": {
        "type": "normal",
        "hp": 250,
        "attack": 5,
        "defense": 5,
        "special_attack": 35,
        "special_defense": 105,
        "speed": 50
    },
    "Tangela": {
        "type": "grass",
        "hp": 65,
        "attack": 55,
        "defense": 115,
        "special_attack": 100,
        "special_defense": 40,
        "speed": 60
    },
    "Kangaskhan": {
        "type": "normal",
        "hp": 105,
        "attack": 95,
        "defense": 80,
        "special_attack": 40,
        "special_defense": 80,
        "speed": 90
    },
    "Horsea": {
        "type": "water",
        "hp": 30,
        "attack": 40,
        "defense": 70,
        "special_attack": 70,
        "special_defense": 25,
        "speed": 60
    },
    "Seadra": {
        "type": "water",
        "hp": 55,
        "attack": 65,
        "defense": 95,
        "special_attack": 95,
        "special_defense": 45,
        "speed": 85
    },
    "Goldeen": {
        "type": "water",
        "hp": 45,
        "attack": 67,
        "defense": 60,
        "special_attack": 35,
        "special_defense": 50,
        "speed": 63
    },
    "Seaking": {
        "type": "water",
        "hp": 80,
        "attack": 92,
        "defense": 65,
        "special_attack": 65,
        "special_defense": 80,
        "speed": 68
    },
    "Staryu": {
        "type": "water",
        "hp": 30,
        "attack": 45,
        "defense": 55,
        "special_attack": 70,
        "special_defense": 55,
        "speed": 85
    },
    "Starmie": {
        "type": "water, psychic",
        "hp": 60,
        "attack": 75,
        "defense": 85,
        "special_attack": 100,
        "special_defense": 85,
        "speed": 115
    },
    "Mr. Mime": {
        "type": "psychic, fairy",
        "hp": 40,
        "attack": 45,
        "defense": 65,
        "special_attack": 100,
        "special_defense": 120,
        "speed": 90
    },
    "Scyther": {
        "type": "bug, flying",
        "hp": 70,
        "attack": 110,
        "defense": 80,
        "special_attack": 55,
        "special_defense": 80,
        "speed": 105
    },
    "Jynx": {
        "type": "ice, psychic",
        "hp": 65,
        "attack": 50,
        "defense": 35,
        "special_attack": 115,
        "special_defense": 95,
        "speed": 95
    },
    "Electabuzz": {
        "type": "electric",
        "hp": 65,
        "attack": 83,
        "defense": 57,
        "special_attack": 95,
        "special_defense": 85,
        "speed": 105
    },
    "Magmar": {
        "type": "fire",
        "hp": 65,
        "attack": 95,
        "defense": 57,
        "special_attack": 100,
        "special_defense": 85,
        "speed": 93
    },
    "Pinsir": {
        "type": "bug",
        "hp": 65,
        "attack": 125,
        "defense": 100,
        "special_attack": 55,
        "special_defense": 70,
        "speed": 85
    },
    "Tauros": {
        "type": "normal",
        "hp": 75,
        "attack": 100,
        "defense": 95,
        "special_attack": 40,
        "special_defense": 70,
        "speed": 110
    },
    "Magikarp": {
        "type": "water",
        "hp": 20,
        "attack": 10,
        "defense": 55,
        "special_attack": 15,
        "special_defense": 20,
        "speed": 80
    },
    "Gyarados": {
        "type": "water, flying",
        "hp": 95,
        "attack": 125,
        "defense": 79,
        "special_attack": 60,
        "special_defense": 100,
        "speed": 81
    },
    "Lapras": {
        "type": "water, ice",
        "hp": 130,
        "attack": 85,
        "defense": 80,
        "special_attack": 85,
        "special_defense": 95,
        "speed": 60
    },
    "Ditto": {
        "type": "normal",
        "hp": 48,
        "attack": 48,
        "defense": 48,
        "special_attack": 48,
        "special_defense": 48,
        "speed": 48
    },
    "Eevee": {
        "type": "normal",
        "hp": 55,
        "attack": 55,
        "defense": 50,
        "special_attack": 45,
        "special_defense": 65,
        "speed": 55
    },
    "Vaporeon": {
        "type": "water",
        "hp": 130,
        "attack": 65,
        "defense": 60,
        "special_attack": 110,
        "special_defense": 95,
        "speed": 65
    },
    "Jolteon": {
        "type": "electric",
        "hp": 65,
        "attack": 65,
        "defense": 60,
        "special_attack": 110,
        "special_defense": 95,
        "speed": 130
    },
    "Flareon": {
        "type": "fire",
        "hp": 65,
        "attack": 130,
        "defense": 60,
        "special_attack": 95,
        "special_defense": 110,
        "speed": 65
    },
    "Porygon": {
        "type": "normal",
        "hp": 65,
        "attack": 60,
        "defense": 70,
        "special_attack": 85,
        "special_defense": 75,
        "speed": 40
    },
    "Omanyte": {
        "type": "rock, water",
        "hp": 35,
        "attack": 40,
        "defense": 100,
        "special_attack": 90,
        "special_defense": 55,
        "speed": 35
    },
    "Omastar": {
        "type": "rock, water",
        "hp": 70,
        "attack": 60,
        "defense": 125,
        "special_attack": 115,
        "special_defense": 70,
        "speed": 55
    },
    "Kabuto": {
        "type": "rock, water",
        "hp": 30,
        "attack": 80,
        "defense": 90,
        "special_attack": 55,
        "special_defense": 45,
        "speed": 55
    },
    "Kabutops": {
        "type": "rock, water",
        "hp": 60,
        "attack": 115,
        "defense": 105,
        "special_attack": 65,
        "special_defense": 70,
        "speed": 80
    },
    "Aerodactyl": {
        "type": "rock, flying",
        "hp": 80,
        "attack": 105,
        "defense": 65,
        "special_attack": 60,
        "special_defense": 75,
        "speed": 130
    },
    "Snorlax": {
        "type": "normal",
        "hp": 160,
        "attack": 110,
        "defense": 65,
        "special_attack": 65,
        "special_defense": 110,
        "speed": 30
    },
    "Articuno": {
        "type": "ice, flying",
        "hp": 90,
        "attack": 85,
        "defense": 100,
        "special_attack": 95,
        "special_defense": 125,
        "speed": 85
    },
    "Zapdos": {
        "type": "electric, flying",
        "hp": 90,
        "attack": 90,
        "defense": 85,
        "special_attack": 125,
        "special_defense": 90,
        "speed": 100
    },
    "Moltres": {
        "type": "fire, flying",
        "hp": 90,
        "attack": 100,
        "defense": 90,
        "special_attack": 125,
        "special_defense": 85,
        "speed": 90
    },
    "Dratini": {
        "type": "dragon",
        "hp": 41,
        "attack": 64,
        "defense": 45,
        "special_attack": 50,
        "special_defense": 50,
        "speed": 50
    },
    "Dragonair": {
        "type": "dragon",
        "hp": 61,
        "attack": 84,
        "defense": 65,
        "special_attack": 70,
        "special_defense": 70,
        "speed": 70
    },
    "Dragonite": {
        "type": "dragon, flying",
        "hp": 91,
        "attack": 134,
        "defense": 95,
        "special_attack": 100,
        "special_defense": 100,
        "speed": 80
    },
    "Mewtwo": {
        "type": "psychic",
        "hp": 106,
        "attack": 110,
        "defense": 90,
        "special_attack": 154,
        "special_defense": 90,
        "speed": 130
    },
    "Mew": {
        "type": "psychic",
        "hp": 100,
        "attack": 100,
        "defense": 100,
        "special_attack": 100,
        "special_defense": 100,
        "speed": 100
    }
}

# Get user input
pokemon = input("Enter the name of a Pokemon from Kanto: ")

# Check if the Pokemon exists in the Pokedex
if pokemon in Pokedex:
    # Print the Pokemon's properties
    properties = Pokedex[pokemon]
    for property, value in properties.items():
        print(f"{property}: {value}")
else:
    print("That Pokemon does not exist in the Pokedex.")