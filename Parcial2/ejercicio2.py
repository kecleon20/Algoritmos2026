import json
from lista import Lista
from heap_min import Heap

# ==============================================================================
# CLASE GRAFO INTEGRADA
# ==============================================================================
class Graph(Lista):
    class _nodeVertex():
        def __init__(self, value, other_values=None):
            self.value = value
            self.other_values = other_values
            self.edges = Lista()
            self.visited = False

        def __str__(self):
            return f"{self.value}"

    class _nodeEdge():
        def __init__(self, weight, destination):
            self.weight = weight
            self.destination = destination

        def __str__(self):
            return f"weight: {self.weight} -> destination: {self.destination}"

    def __init__(self, is_dir=True):
        super().__init__()
        self.is_dir = is_dir

    def add_vertex(self, value, other_values=None):
        node_vertex = self._nodeVertex(value, other_values)
        self.insert(node_vertex, 'value')

    def add_edge(self, weight, origin, destination):
        pos_origin = self.search(origin, 'value')
        if pos_origin is None: return
        pos_destination = self.search(destination, 'value')
        if pos_destination is None: return

        node_edge = self._nodeEdge(weight, destination)
        self[pos_origin].edges.insert(node_edge, 'destination')

        if origin != destination and not self.is_dir:
            node_edge = self._nodeEdge(weight, origin)
            self[pos_destination].edges.insert(node_edge, 'destination')

    def dijkstra(self, origin):
        from math import inf
        no_visited = Heap()
        path = []
        
        for i in range(self.size()):
            vertex = self.get_element_by_index(i)
            distance = 0 if vertex.value == origin else inf
            no_visited.arrive([vertex.value, vertex, None], distance)

        while no_visited.size() > 0:
            vertex_data = no_visited.atention()
            costo_nodo_actual = vertex_data[0]
            path.append([vertex_data[1][0], costo_nodo_actual, vertex_data[1][2]])
            
            edges = vertex_data[1][1].edges
            for j in range(edges.size()):
                edge = edges.get_element_by_index(j)
                
                for k in range(no_visited.size()):
                    if no_visited.vector[k][1][0] == edge.destination:
                        if costo_nodo_actual + edge.weight < no_visited.vector[k][0]:
                            no_visited.vector[k][1][2] = vertex_data[1][0]
                            no_visited.vector[k][0] = costo_nodo_actual + edge.weight
                            no_visited.flotar(k)
                        break
        return path                    

    def kruskal(self, origin_vertex):
        def search_in_forest(forest, value):
            for index, tree in enumerate(forest):
                if value in tree:
                    return index
                
        forest = []
        edges = Heap()
        for i in range(self.size()):
            vertex = self.get_element_by_index(i)
            forest.append(vertex.value)
            for j in range(vertex.edges.size()):
                edge = vertex.edges.get_element_by_index(j)
                edges.arrive([vertex.value, edge.destination], edge.weight)

        while len(forest) > 1 and edges.size() > 0:
            edge = edges.atention()
            origin = search_in_forest(forest, edge[1][0])
            destination = search_in_forest(forest, edge[1][1])
            if origin is not None and destination is not None:
                if origin != destination:
                    if origin > destination:
                        vertex_origin = forest.pop(origin)
                        vertex_destination = forest.pop(destination)
                    else:
                        vertex_destination = forest.pop(destination)
                        vertex_origin = forest.pop(origin)

                    if '-' not in vertex_origin and '-' not in vertex_destination:
                        forest.append(f'{vertex_origin}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_destination:
                        forest.append(vertex_origin+';'+f'{edge[1][0]}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_origin:
                        forest.append(vertex_destination+';'+f'{vertex_origin}-{edge[1][1]}-{edge[0]}')
                    else:
                        forest.append(vertex_origin+';'+vertex_destination+';'+f'{edge[1][0]}-{edge[1][1]}-{edge[0]}')
        
        from_vertex = search_in_forest(forest, origin_vertex)
        return forest[from_vertex] if from_vertex is not None else forest

# ==============================================================================
# CARGA DE DATOS DESDE JSON
# ==============================================================================
ARCHIVO_JSON = "starwars_db.json"

def cargar_datos_starwars(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        return datos['personajes'], datos['aristas']
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}.")
        return [], []

# ==============================================================================
# RESOLUCIÓN DE CONSIGNAS
# ==============================================================================

print("="*70)
print("--- 1. CARGA DEL GRAFO ---")
print("="*70)

PERSONAJES, ARISTAS = cargar_datos_starwars(ARCHIVO_JSON)

if not PERSONAJES:
    print("No se pudieron cargar los datos. Verifica el archivo JSON.")
else:
    grafo_sw = Graph(is_dir=False)

    for personaje in PERSONAJES:
        grafo_sw.add_vertex(personaje)

    for arista in ARISTAS:
        peso, origen, destino = arista
        grafo_sw.add_edge(peso, origen, destino)

    print(f"Grafo cargado exitosamente con {len(PERSONAJES)} personajes y {len(ARISTAS)} relaciones.")


    print("\n" + "="*70)
    print("--- 2. ÁRBOL DE EXPANSIÓN MÍNIMO (AEM) ---")
    print("="*70)
    aem = grafo_sw.kruskal("C-3PO")
    print("Árbol de Expansión Mínimo (Kruskal):")
    peso_total = 0
    if isinstance(aem, str):
        for edge in aem.split(';'):
            if edge:
                partes = edge.split('-')
                if len(partes) == 3:
                    origen, destino, peso = partes
                    peso_total += int(peso)
                    print(f"  - {origen} <-> {destino} (Peso: {peso})")
                else:
                    print(f"  - Nodo: {edge}")
    print(f"Peso total del AEM: {peso_total}")


    print("\n" + "="*70)
    print("--- 3. MÁXIMO DE EPISODIOS COMPARTIDOS ---")
    print("="*70)
    max_peso = -1
    pares_maximos = []

    for i in range(grafo_sw.size()):
        vertice = grafo_sw.get_element_by_index(i)
        for j in range(vertice.edges.size()):
            arista = vertice.edges.get_element_by_index(j)
            if vertice.value < arista.destination:
                if arista.weight > max_peso:
                    max_peso = arista.weight
                    pares_maximos = [(vertice.value, arista.destination)]
                elif arista.weight == max_peso:
                    pares_maximos.append((vertice.value, arista.destination))

    print(f"El número máximo de episodios compartidos es: {max_peso}")
    print("Pares de personajes que coinciden en esa cantidad:")
    for par in pares_maximos:
        print(f"  - {par[0]} y {par[1]}")


    print("\n" + "="*70)
    print("--- 4. CAMINOS MÁS CORTOS (Dijkstra) ---")
    print("="*70)

    def mostrar_camino(origen, destino):
        caminos = grafo_sw.dijkstra(origen)
        encontrado = False
        costo_total = 0
        camino_inverso = []
        
        for paso in caminos:
            if paso[0] == destino:
                encontrado = True
                costo_total = paso[1]
                camino_inverso.append(paso[0])
                predecesor = paso[2]
                break
                
        if encontrado:
            while predecesor is not None:
                camino_inverso.append(predecesor)
                for paso in caminos:
                    if paso[0] == predecesor:
                        predecesor = paso[2]
                        break
            camino_inverso.reverse()
            print(f"Camino más corto de {origen} a {destino}:")
            print(f"  Ruta: {' -> '.join(camino_inverso)}")
            print(f"  Costo (episodios): {costo_total}")
        else:
            print(f"No se encontró camino de {origen} a {destino}.")

    mostrar_camino("C-3PO", "R2-D2")
    print()
    mostrar_camino("Yoda", "Darth Vader")


    print("\n" + "="*70)
    print("--- 5. PERSONAJES QUE APARECIERON EN LOS 9 EPISODIOS ---")
    print("="*70)
    personajes_9_episodios = set()

    for i in range(grafo_sw.size()):
        vertice = grafo_sw.get_element_by_index(i)
        for j in range(vertice.edges.size()):
            arista = vertice.edges.get_element_by_index(j)
            if arista.weight == 9:
                personajes_9_episodios.add(vertice.value)

    if personajes_9_episodios:
        print("Personajes que aparecieron en los 9 episodios:")
        for p in sorted(personajes_9_episodios):
            print(f"  - {p}")
    else:
        print("Ningún personaje apareció en los 9 episodios.")

    print("\n" + "="*70)