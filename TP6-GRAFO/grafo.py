from heap_min import Heap
def dijkstra(self, origen, destino, criterio=None):
        from math import inf
        # Diccionario para almacenar las distancias mínimas conocidas
        distancias = {}
        # Diccionario para almacenar el nodo predecesor en el camino óptimo
        predecesores = {}
        
        # Inicializar distancias
        for i in range(self.size()):
            vertice = self.get_element_by_index(i)[0]
            distancias[vertice] = inf
            predecesores[vertice] = None
            
        distancias[origen] = 0

        # Cola de prioridad (usamos el Heap existente)
        no_visitados = Heap()
        no_visitados.arrive(origen, 0)

        while no_visitados.size() > 0:
            # Extraemos el nodo con menor distancia acumulada
            actual = no_visitados.atention()
            vertice_actual = actual[1]
            
            # Si llegamos al destino, podemos detenernos
            if vertice_actual == destino:
                break
            
            # Buscar índice del vértice actual para obtener sus adyacentes
            pos_actual = self.search_vertice(vertice_actual, criterio)
            if pos_actual is not None:
                adyacentes = self.get_element_by_index(pos_actual)[1]
                for i in range(adyacentes.size()):
                    arista = adyacentes.get_element_by_index(i)
                    vecino = arista.vertice
                    peso = arista.peso
                    
                    nueva_dist = distancias[vertice_actual] + peso
                    
                    # Si encontramos un camino más corto hacia el vecino
                    if nueva_dist < distancias[vecino]:
                        distancias[vecino] = nueva_dist
                        predecesores[vecino] = vertice_actual
                        # Agregamos a la cola de prioridad con la nueva distancia
                        no_visitados.arrive(vecino, nueva_dist)

        # Si el destino es inalcanzable
        if distancias[destino] == inf:
            return None

        # Reconstruir el camino desde el destino hacia el origen
        camino = []
        actual = destino
        while actual is not None:
            camino.append(actual)
            actual = predecesores[actual]
        
        camino.reverse() # Invertir para que vaya de origen a destino
        
        return camino, distancias[destino]