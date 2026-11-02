# starwars_db.py
# Base de datos de personajes y sus interacciones (episodios juntos)

PERSONAJES = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", 
    "C-3PO", "Leia", "Rey", "Kylo Ren", 
    "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

# Aristas: (Peso = Cantidad de episodios juntos, Personaje 1, Personaje 2)
ARISTAS = [
    # Trilogía Original
    (9, "Luke Skywalker", "Han Solo"),
    (9, "Luke Skywalker", "Leia"),
    (9, "Luke Skywalker", "C-3PO"),
    (9, "Luke Skywalker", "R2-D2"),
    (6, "Luke Skywalker", "Yoda"),
    (9, "Darth Vader", "Leia"),
    (9, "Darth Vader", "C-3PO"),
    (9, "Darth Vader", "R2-D2"),
    (9, "Leia", "Han Solo"),
    (9, "Leia", "C-3PO"),
    (9, "Leia", "R2-D2"),
    (9, "Leia", "Chewbacca"),
    (9, "Han Solo", "Chewbacca"),
    (9, "Han Solo", "C-3PO"),
    (9, "Han Solo", "R2-D2"),
    (9, "C-3PO", "R2-D2"),
    (9, "C-3PO", "Chewbacca"),
    (9, "R2-D2", "Chewbacca"),
    (6, "Yoda", "Chewbacca"),
    (5, "Boba Fett", "Darth Vader"),
    (4, "Boba Fett", "Han Solo"),
    (6, "Boba Fett", "Luke Skywalker"),
    
    # Trilogía Secuela
    (7, "Rey", "BB-8"),
    (7, "Rey", "Kylo Ren"),
    (7, "Rey", "Leia"),
    (7, "Rey", "C-3PO"),
    (7, "Kylo Ren", "Leia"),
    (7, "Kylo Ren", "BB-8"),
    (7, "Kylo Ren", "Han Solo") # Kylo Ren y Han Solo comparten episodio 7
]