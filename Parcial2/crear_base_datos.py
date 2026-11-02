import json

def generar_base_datos():
    # Lista de tipos oficiales
    tipos_oficiales = [
        "Normal", "Fuego", "Agua", "Planta", "Eléctrico", "Hielo", 
        "Lucha", "Veneno", "Tierra", "Volador", "Psíquico", "Bicho", 
        "Roca", "Fantasma", "Dragón", "Siniestro", "Acero", "Hada"
    ]
    
    # Debilidades lógicas según el tipo (simplificado para el parcial)
    debilidades_por_tipo = {
        "Normal": ["Lucha"], "Fuego": ["Agua", "Roca", "Tierra"],
        "Agua": ["Planta", "Eléctrico"], "Planta": ["Fuego", "Hielo", "Veneno", "Volador", "Bicho"],
        "Eléctrico": ["Tierra"], "Hielo": ["Fuego", "Lucha", "Roca", "Acero"],
        "Lucha": ["Psíquico", "Volador", "Hada"], "Veneno": ["Psíquico", "Tierra"],
        "Tierra": ["Agua", "Planta", "Hielo"], "Volador": ["Eléctrico", "Hielo", "Roca"],
        "Psíquico": ["Bicho", "Fantasma", "Siniestro"], "Bicho": ["Fuego", "Volador", "Roca"],
        "Roca": ["Agua", "Planta", "Lucha", "Tierra", "Acero"], "Fantasma": ["Fantasma", "Siniestro"],
        "Dragón": ["Hielo", "Dragón", "Hada"], "Siniestro": ["Lucha", "Bicho", "Hada"],
        "Acero": ["Fuego", "Lucha", "Tierra"], "Hada": ["Veneno", "Acero"]
    }

    # Nombres base para que no se vea tan "generico" (algunos nombres reales)
    nombres_reales = [
        "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
        "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree",
        "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot",
        "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok",
        "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran", "Nidorina",
        "Nidoqueen", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix",
        "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish",
        "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth",
        "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck",
        "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl",
        "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke",
        "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel",
        "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke",
        "Slowbro", "Magnemite", "Magneton", "Farfetchd", "Doduo", "Dodrio",
        "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster",
        "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno",
        "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor",
        "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing",
        "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan",
        "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie",
        "MrMime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir",
        "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee",
        "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar",
        "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos",
        "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"
    ]

    pokemons_json = []

    # Generamos los 1025
    for i in range(1, 1026):
        # Nombre: Si es menor a 151 usamos el nombre real, si no, un nombre compuesto
        if i <= len(nombres_reales):
            nombre = nombres_reales[i-1]
        else:
            nombre = f"Pokemon_{i}"

        # Tipos: Usamos matemática modular para que varíen de forma predecible (no aleatoria)
        tipo1_idx = (i * 3) % len(tipos_oficiales)
        tipo2_idx = (i * 7) % len(tipos_oficiales)
        
        tipos = [tipos_oficiales[tipo1_idx]]
        if tipo1_idx != tipo2_idx and i % 2 == 0: # 50% tienen doble tipo
            tipos.append(tipos_oficiales[tipo2_idx])
            
        # Debilidades: Basadas en el tipo 1
        debilidades = debilidades_por_tipo[tipos[0]][:]

        # Booleanos: Megas y Gigamax (Asignación determinista)
        mega = (i % 100 == 0) or (i % 150 == 0)
        gigamax = (i % 200 == 0)

        # Generación (Aunque la consigna no la pide explícitamente, es buena para los datos)
        if i <= 151: gen = 1
        elif i <= 251: gen = 2
        elif i <= 386: gen = 3
        elif i <= 493: gen = 4
        elif i <= 649: gen = 5
        elif i <= 721: gen = 6
        elif i <= 809: gen = 7
        elif i <= 905: gen = 8
        else: gen = 9

        # Creamos el diccionario para el JSON
        pokemon = {
            "nombre": nombre,
            "numero": i,
            "tipos": tipos,
            "debilidades": debilidades,
            "mega": mega,
            "gigamax": gigamax
        }
        pokemons_json.append(pokemon)

    # Guardamos el archivo
    with open('pokemons_1025.json', 'w', encoding='utf-8') as archivo:
        json.dump(pokemons_json, archivo, indent=4, ensure_ascii=False)
    
    print("¡Archivo 'pokemons_1025.json' creado exitosamente con 1025 Pokémons!")

if __name__ == "__main__":
    generar_base_datos()