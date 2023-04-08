import json


def read_infocalories():
    with open("app/nutrition/data/infocalories.json", "r") as f:
        return json.load(f)


INFOCALORIES = read_infocalories()

NUTRIENT_DB = [
    {
        "name": "oignon",
        "unit": None,
        "calories": 40.0,
    },
    {
        "name": "beurre",
        "unit": "g",
        "calories": 7.6,
        "glucides": 0.0,
        "lipides": 0.84,
        "proteines": 0.01,
    },
    {"name": "tomate", "unit": None, "calories": 15.0},
    {"name": "tomate", "unit": "g", "calories": 0.15},
    {"name": "coulis de tomate", "unit": "cl", "calories": 2.9},
    {"name": "tortilla", "unit": None, "calories": 122.0},
    {"name": "oeuf", "unit": None, "calories": 87.0},
    {"name": "lait", "unit": "cl", "calories": 5.2},
    {"name": "sucre", "unit": "g", "calories": 3.9},
    {"name": "lait de coco", "unit": "cl", "calories": 2.1},
    {"name": "noix de coco", "unit": "g", "calories": 3.5},
    {"name": "lait concentre", "unit": "g", "calories": 3.2},
    {"name": "pomme de terre", "unit": "g", "calories": 0.7},
    {"name": "creme fraiche", "unit": "cl", "calories": 34.8},
    {"name": "farine", "unit": "g", "calories": 3.6},
    {"name": "chocolat", "unit": "g", "calories": 5.5},
    {"name": "cassonade", "unit": "g", "calories": 3.8},
    {"name": "poivron", "unit": None, "calories": 32},
    {"name": "parmesan", "unit": "g", "calories": 4.3},
    {
        "name": "gousse d'ail",
        "unit": None,
        "calories": 9.1,
        "glucides": 1.75,
        "lipides": 0.035,
        "proteines": 0.49,
    },
    {"name": "potiron", "unit": "g", "calories": 0.14},
    {
        "name": "carotte",
        "unit": "g",
        "calories": 0.3,
        "glucides": 0.064,
        "lipides": 0.003,
        "proteines": 0.01,
    },
    {
        "name": "carotte",
        "unit": None,
        "calories": 37.5,
        "glucides": 8,
        "lipides": 0.375,
        "proteines": 1.25,
    },
    {
        "name": "poireau",
        "unit": "g",
        "calories": 0.246,
        "glucides": 0.03,
        "lipides": 0.002,
        "proteines": 0.011,
    },
    {
        "name": "poireau",
        "unit": None,
        "calories": 36.9,
        "glucides": 4.5,
        "lipides": 0.3,
        "proteines": 1.65,
    },
    {"name": "haricot rouge", "unit": "g", "calories": 3.3},
    {"name": "pomme", "unit": None, "calories": 73.0},
    {"name": "pomme", "unit": "g", "calories": 0.53},
    {"name": "cannelle", "unit": "cas", "calories": 18},
    {"name": "blanc oeuf", "unit": None, "calories": 22},
    {"name": "jaune oeuf", "unit": None, "calories": 52},
    {"name": "citron", "unit": None, "calories": 46.2},
    {"name": "courgette", "unit": None, "calories": 42.5},
    {"name": "courgette", "unit": "g", "calories": 0.17},
    {
        "name": "navet",
        "unit": None,
        "calories": 37.5,
        "glucides": 5.7,
        "lipides": 0.3,
        "proteines": 1.35,
    },
    {
        "name": "navet",
        "unit": "g",
        "calories": 0.25,
        "glucides": 0.038,
        "lipides": 0.002,
        "proteines": 0.009,
    },
    {"name": "poudre d'amande", "unit": "g", "calories": 6.1},
    {"name": "creme liquide", "unit": "cl", "calories": 29.2},
    {"name": "sucre vanille", "unit": "sachet", "calories": 30},
    {"name": "champignon", "unit": "g", "calories": 0.22},
    {"name": "vin blanc", "unit": "cl", "calories": 8.7},
    {"name": "vin rouge", "unit": "cl", "calories": 9.0},
    {"name": "echalotte", "unit": None, "calories": 7},
    {"name": "pate feuilletee", "unit": None, "calories": 874},
    {"name": "pate feuilletee", "unit": "g", "calories": 3.8},
    {
        "name": "pate brisee",
        "unit": "g",
        "calories": 3.8,
        "glucides": 0.428,
        "lipides": 0.2,
        "proteines": 0.066,
    },
    {
        "name": "pate brisee",
        "unit": None,
        "calories": 874,
        "glucides": 98.4,
        "lipides": 46,
        "proteines": 15.2,
    },
    {"name": "aubergine", "unit": None, "calories": 78},
    {"name": "aubergine", "unit": "g", "calories": 0.25},
    {"name": "chapelure", "unit": "g", "calories": 3.95},
    {
        "name": "banane",
        "unit": None,
        "calories": 108,
        "glucides": 25.2,
        "lipides": 0.6,
        "proteines": 1.2,
    },
    {
        "name": "banane",
        "unit": "g",
        "calories": 0.91,
        "glucides": 0.21,
        "lipides": 0.005,
        "proteines": 0.01,
    },
    {"name": "biere", "unit": "cl", "calories": 4.52},
]

FROMAGES_DB = [
    {"name": "tomme", "unit": "g", "calories": 3.61},
    {"name": "comte", "unit": "g", "calories": 4.17},
    {"name": "beaufort", "unit": "g", "calories": 3.95},
    {"name": "emmental", "unit": "g", "calories": 3.67},
    {"name": "mozzarella", "unit": "g", "calories": 2.8},
    {"name": "mascarpone", "unit": "g", "calories": 4.2},
    {"name": "ricotta", "unit": "g", "calories": 1.7},
]

VIANDES_DB = [
    {"name": "gigot de chevreuil", "unit": "g", "calories": 1.74},
    {
        "name": "gigot d'agneau",
        "unit": "g",
        "calories": 2.69,
        "glucides": 0.0,
        "lipides": 0.21,
        "proteines": 0.2,
    },
    {
        "name": "poulet",
        "unit": "g",
        "calories": 2.4,
        "glucides": 0,
        "lipides": 0.018,
        "proteines": 0.262
    },
    {
        "name": "lardon",
        "unit": "g",
        "calories": 3.38,
        "glucides": 0.02,
        "lipides": 0.26,
        "proteines": 0.24,
    },
    {
        "name": "boeuf",
        "unit": "g",
        "calories": 2.5,
    },
    {"name": "crevette", "unit": "g", "calories": 0.94},
    {"name": "filet mignon", "unit": "g", "calories": 1.43},
    {
        "name": "poitrine de porc",
        "unit": "g",
        "calories": 5.18,
        "glucides": 0,
        "lipides": 	0.273,
        "proteines": 0.165
    },
    {"name": "cotelette de porc", "unit": "g", "calories": 2.31},
    {
        "name": "veau",
        "unit": "g",
        "calories": 1.72,
        "glucides": 0,
        "lipides": 	0.04,
        "proteines": 0.21
    },
]

FECULENTS_DB = [
    {"name": "spaghetti", "unit": "g", "calories": 1.6},
    {"name": "lentille", "unit": "g", "calories": 1.2},
    {"name": "riz", "unit": "g", "calories": 1.3},
    {"name": "nouille", "unit": "g", "calories": 1.38},
    {
        "name": "pates",
        "unit": "g",
        "calories": 3.5,
        "glucides": 0.7,
        "lipides": 0.025,
        "proteines": 0.12,
    },
]

NUTRIENT_DB = INFOCALORIES + NUTRIENT_DB + VIANDES_DB + FROMAGES_DB + FECULENTS_DB
