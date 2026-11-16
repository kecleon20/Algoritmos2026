from grafo import Grafo

# ==========================================
# Actividad 14
# ==========================================

# Punto a: Definir los vértices (ambientes de la casa)
lista = ['cocina', 'comedor', 'cochera', 'quincho', 'bano1', 'bano2', 
         'hab1', 'hab2', 'sala_estar', 'terraza', 'patio']

grafo_casa = Grafo(dirigido=False)

for vertice in lista:
    grafo_casa.insert_vertice(vertice)

# Punto b: Cargar al menos 3 aristas a cada vértice, 
# a dos de estas darle peso 5.
# NOTA: Como el grafo es no dirigido, solo insertamos la arista una vez.
# El método insert_arist se encarga de crear la bidireccionalidad automáticamente.

# Conexiones desde cocina (3 aristas, dos con peso 5)
grafo_casa.insert_arist("cocina", "comedor", 3, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("cocina", "cochera", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("cocina", "hab1", 5, criterio_vertice='nombre', criterio_arista='vertice')

# Conexiones desde comedor (3 aristas, dos con peso 5)
grafo_casa.insert_arist("comedor", "quincho", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("comedor", "terraza", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("comedor", "sala_estar", 9, criterio_vertice='nombre', criterio_arista='vertice')

# Conexiones desde cochera (3 aristas, dos con peso 5)
grafo_casa.insert_arist("cochera", "quincho", 6, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("cochera", "hab2", 5, criterio_vertice='nombre', criterio_arista='vertice')
# Ya tiene cocina-cochera (5)

# Conexiones desde quincho (3 aristas, dos con peso 5)
grafo_casa.insert_arist("quincho", "sala_estar", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("quincho", "terraza", 7, criterio_vertice='nombre', criterio_arista='vertice')
# Ya tiene comedor-quincho (5) y cochera-quincho (6)

# Conexiones desde baño 1 (3 aristas, dos con peso 5)
grafo_casa.insert_arist("bano1", "hab1", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("bano1", "sala_estar", 6, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("bano1", "terraza", 5, criterio_vertice='nombre', criterio_arista='vertice')

# Conexiones desde baño 2 (3 aristas, dos con peso 5)
grafo_casa.insert_arist("bano2", "terraza", 4, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("bano2", "patio", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("bano2", "comedor", 5, criterio_vertice='nombre', criterio_arista='vertice')

# Conexiones desde hab 1 (3 aristas, dos con peso 5)
grafo_casa.insert_arist("hab1", "bano2", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("hab1", "terraza", 4, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("hab1", "patio", 5, criterio_vertice='nombre', criterio_arista='vertice')
# Ya tiene cocina-hab1 (5) y bano1-hab1 (5)

# Conexiones desde hab 2 (3 aristas, dos con peso 5)
grafo_casa.insert_arist("hab2", "sala_estar", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("hab2", "terraza", 3, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("hab2", "patio", 5, criterio_vertice='nombre', criterio_arista='vertice')
# Ya tiene cochera-hab2 (5)

# Conexiones desde sala de estar (3 aristas, dos con peso 5)
grafo_casa.insert_arist("sala_estar", "terraza", 5, criterio_vertice='nombre', criterio_arista='vertice')
grafo_casa.insert_arist("sala_estar", "patio", 5, criterio_vertice='nombre', criterio_arista='vertice')
# Ya tiene comedor-sala_estar (9), quincho-sala_estar (5), bano1-sala_estar (6), hab2-sala_estar (5)

# Conexiones desde terraza (3 aristas, dos con peso 5)
grafo_casa.insert_arist("terraza", "patio", 4, criterio_vertice='nombre', criterio_arista='vertice')
# Ya tiene comedor-terraza (5), quincho-terraza (7), bano1-terraza (5), bano2-terraza (4), 
# hab1-terraza (4), hab2-terraza (3), sala_estar-terraza (5)

# Conexiones desde patio (3 aristas, dos con peso 5)
grafo_casa.insert_arist("patio", "cochera", 5, criterio_vertice='nombre', criterio_arista='vertice')
# Ya tiene bano2-patio (5), hab1-patio (5), hab2-patio (5), sala_estar-patio (5), terraza-patio (4)

# ==========================================
# Punto c: Árbol de expansión mínima (Kruskal)
# ==========================================
print("=== Punto C: Árbol de Expansión Mínima (Kruskal) ===")
bosque = grafo_casa.kruskal()
longitud_total_cables = 0

for arbol in bosque:
    print('Árbol:')
    for nodo in arbol.split(';'):
        print(f"  {nodo}")
        # El formato del nodo en kruskal es: "vertice_origen-vertice_destino-peso"
        # o contiene múltiples nodos separados por ';'
        # Extraemos el peso de la última arista del string
        try:
            peso = int(nodo.split('-')[-1])
            longitud_total_cables += peso
        except ValueError:
            pass

print(f"\nLongitud total de cables necesaria: {longitud_total_cables} metros.\n")

# ==========================================
# Punto d: Camino más corto (Dijkstra)
# ==========================================
print("=== Punto D: Camino más corto (Dijkstra) ===")
ori = 'hab1'
des = 'sala_estar'

# Llamamos al método dijkstra corregido
# (Ver nota al final sobre la corrección en grafo.py)
resultado = grafo_casa.dijkstra(ori, des, criterio='nombre')

if resultado is not None:
    camino, distancia_total = resultado
    print(f"Camino más corto desde '{ori}' hasta '{des}':")
    print(" -> ".join(camino))
    print(f"Total de metros de cable de red necesarios: {distancia_total} metros.")
else:
    print(f"No existe camino entre '{ori}' y '{des}'.")

# =====================================================================
# ACTIVIDAD 5
# =====================================================================
print("\n\n==================================================")
print("ACTIVIDAD 5")
print("==================================================")

# Clase para almacenar nombre y tipo (Punto a)
class Dispositivo:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

# Punto h: Grafo no dirigido
grafo_red = Grafo(dirigido=False)

# Punto a: Cargar nodos con su tipo
dispositivos = [
    ("Red Hat", "notebook"), ("Debian", "notebook"), ("Arch", "notebook"),
    ("Manjaro", "pc"), ("Fedora", "pc"), ("Ubuntu", "pc"), ("Mint", "pc"), ("Parrot", "pc"),
    ("Guarani", "servidor"), ("MongoDB", "servidor"),
    ("Router 1", "router"), ("Router 2", "router"), ("Router 3", "router"),
    ("Switch 1", "switch"), ("Switch 2", "switch"),
    ("Impresora", "impresora")
]

for nombre, tipo in dispositivos:
    disp = Dispositivo(nombre, tipo)
    grafo_red.insert_vertice(disp, criterio='nombre')

# Cargar aristas según la imagen (Pesos aproximados según lo visible)
grafo_red.insert_arist("Red Hat", "Router 2", 25, criterio_vertice='nombre')
grafo_red.insert_arist("Red Hat", "Guarani", 9, criterio_vertice='nombre')
grafo_red.insert_arist("Guarani", "Router 2", 9, criterio_vertice='nombre')
grafo_red.insert_arist("Guarani", "Router 3", 50, criterio_vertice='nombre')
grafo_red.insert_arist("Router 3", "Router 1", 43, criterio_vertice='nombre')
grafo_red.insert_arist("Router 3", "Switch 2", 61, criterio_vertice='nombre')
grafo_red.insert_arist("Router 2", "Switch 1", 37, criterio_vertice='nombre')
grafo_red.insert_arist("Router 1", "Switch 1", 29, criterio_vertice='nombre')
grafo_red.insert_arist("Router 1", "Mint", 80, criterio_vertice='nombre')
grafo_red.insert_arist("Switch 1", "Debian", 17, criterio_vertice='nombre')
grafo_red.insert_arist("Switch 1", "Ubuntu", 18, criterio_vertice='nombre')
grafo_red.insert_arist("Switch 1", "Impresora", 22, criterio_vertice='nombre')
grafo_red.insert_arist("Switch 2", "Manjaro", 40, criterio_vertice='nombre')
grafo_red.insert_arist("Switch 2", "Parrot", 12, criterio_vertice='nombre')
grafo_red.insert_arist("Switch 2", "MongoDB", 5, criterio_vertice='nombre')
grafo_red.insert_arist("Switch 2", "Fedora", 56, criterio_vertice='nombre')
grafo_red.insert_arist("Switch 2", "Arch", 56, criterio_vertice='nombre')

# Punto b: Barrido en profundidad y amplitud desde las notebooks
print("\n--- Punto B: Barridos desde Notebooks ---")
notebooks = ["Red Hat", "Debian", "Arch"]

for nb in notebooks:
    print(f"\n>>> Barrido desde: {nb}")
    
    # Barrido en profundidad
    print("Profundidad:")
    grafo_red.mark_as_not_visited()
    pos = grafo_red.search_vertice(nb, criterio='nombre')
    if pos is not None:
        grafo_red.deep_list(poscion=pos)
        
    # Barrido en amplitud
    print("Amplitud:")
    grafo_red.mark_as_not_visited()
    if pos is not None:
        grafo_red.amplitude_list(posicion=pos)

# Punto c: Camino más corto de PCs a Impresora
print("\n--- Punto C: Camino más corto a Impresora ---")
pcs_a_imprimir = ["Manjaro", "Red Hat", "Fedora"]

for pc in pcs_a_imprimir:
    print(f"\nDesde {pc} hasta Impresora:")
    resultado = grafo_red.dijkstra(pc, "Impresora", criterio='nombre')
    if resultado:
        camino, distancia = resultado
        print(" -> ".join(camino))
        print(f"Distancia: {distancia} metros")
    else:
        print("No hay camino.")

# Punto d: Árbol de expansión mínima
print("\n--- Punto D: Árbol de Expansión Mínima ---")
bosque_red = grafo_red.kruskal()
for arbol in bosque_red:
    print("Árbol:")
    for nodo in arbol.split(';'):
        print(f"  {nodo}")

# Punto e: PC más cercano a Servidor Guarani
print("\n--- Punto E: PC más cercano a Guarani ---")
pcs = ["Manjaro", "Fedora", "Ubuntu", "Mint", "Parrot"]
mejor_pc = None
mejor_distancia = float('inf')
mejor_camino = []

for pc in pcs:
    resultado = grafo_red.dijkstra(pc, "Guarani", criterio='nombre')
    if resultado:
        camino, distancia = resultado
        if distancia < mejor_distancia:
            mejor_distancia = distancia
            mejor_pc = pc
            mejor_camino = camino

if mejor_pc:
    print(f"La PC más cercana es {mejor_pc} con una distancia de {mejor_distancia} metros.")
    print(f"Camino: {' -> '.join(mejor_camino)}")
else:
    print("No se encontró camino.")

# Punto f: PC más cercana al servidor MongoDB desde el Switch 01
print("\n--- Punto F: PC más cercana a MongoDB desde Switch 1 ---")
# Primero, necesitamos saber cuáles PCs están conectadas al Switch 1
# Según el grafo, al Switch 1 están conectadas Debian(Notebook), Ubuntu(PC) y Impresora
# Pero la consigna pide "desde que computadora del switch 01". 
# Asumiremos que se refiere a las PCs (no notebooks) conectadas al Switch 1.
# Si no hay PCs directas, evaluamos todas las PCs del grafo.

pcs_switch1 = ["Ubuntu"] # La única PC (no notebook) conectada directamente al Switch 1
mejor_pc_f = None
mejor_dist_f = float('inf')
mejor_camino_f = []

for pc in pcs_switch1:
    resultado = grafo_red.dijkstra(pc, "MongoDB", criterio='nombre')
    if resultado:
        camino, distancia = resultado
        if distancia < mejor_dist_f:
            mejor_dist_f = distancia
            mejor_pc_f = pc
            mejor_camino_f = camino

if mejor_pc_f:
    print(f"La PC más cercana a MongoDB desde Switch 1 es {mejor_pc_f} a {mejor_dist_f} metros.")
    print(f"Camino: {' -> '.join(mejor_camino_f)}")
else:
    print("No se encontró camino.")

# Punto g: Cambiar conexión de Impresora a Router 02
print("\n--- Punto G: Cambiar Impresora a Router 2 ---")
# Eliminar conexión vieja (Switch 1 - Impresora)
grafo_red.delete_arista("Switch 1", "Impresora")
# Crear conexión nueva (Router 2 - Impresora) con un peso estimado de 25
grafo_red.insert_arist("Impresora", "Router 2", 25, criterio_vertice='nombre')

print("Conexión actualizada. Volviendo a resolver Punto B (barridos):")
for nb in notebooks:
    print(f"\n>>> Barrido desde: {nb}")
    
    # Barrido en profundidad
    print("Profundidad:")
    grafo_red.mark_as_not_visited()
    pos = grafo_red.search_vertice(nb, criterio='nombre')
    if pos is not None:
        grafo_red.deep_list(poscion=pos)
        
    # Barrido en amplitud
    print("Amplitud:")
    grafo_red.mark_as_not_visited()
    if pos is not None:
        grafo_red.amplitude_list(posicion=pos)