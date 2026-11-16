def usar_la_fuerza(mochila, objetos_sacados=0):
    if not mochila:
        return "No se encontró ningún sable de luz en la mochila."
    elif mochila[0] == "sable de luz":
        return f"Se encontró un sable de luz en la mochila después de sacar {objetos_sacados+1} objetos."
    else:
        return usar_la_fuerza(mochila[1:], objetos_sacados+1)
