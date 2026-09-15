from lista import Lista as ListaSimple

def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        return value
    else:
        dic_atributos = value.__dict__
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            print('no se puede ordenar por este criterio')


class Lista():

    def __init__(self):
        self.__elements = []

    def insertar(self, value, criterio=None):
        # print('criterio de insercion', criterio)
        if len(self.__elements) == 0 or criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[-1][0], criterio):
            self.__elements.append([value, ListaSimple()])
        elif criterio_comparacion(value, criterio) < criterio_comparacion(self.__elements[0][0], criterio):
            self.__elements.insert(0, [value, ListaSimple()])
        else:
            index = 1
            while criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[index][0], criterio):
                index += 1
            self.__elements.insert(index, [value, ListaSimple()])

    def buscar(self, search_value, criterio=None):
        position = None
        first = 0
        last = self.tam() - 1
        while (first <= last and position == None):
            middle = (first + last) // 2
            if search_value == criterio_comparacion(self.__elements[middle][0], criterio):
                position = middle
            elif search_value > criterio_comparacion(self.__elements[middle][0], criterio):
                first = middle + 1
            else:
                last = middle - 1
        return position

    def eliminar(self, value, criterio=None):
        return_value = None
        pos = self.buscar(value, criterio)
        if pos is not None:
            return_value = self.__elements.pop(pos)
        return return_value

    def tam(self):
        return len(self.__elements)

    def barrido(self):
        for value in self.__elements:
            print(value[0])
            value[1].barrido()

    def reordenar(self, criterio=None, reverse=False):
        dic_atributos = self.__elements[0][0].__dict__
        if criterio in dic_atributos:
            def func_criterio(valor):
                return valor.__dict__[criterio]

            self.__elements.sort(key=func_criterio, reverse=reverse)
        else:
            print('no se puede ordenar por este criterio')

    def elemento_indice(self, index):
        return_value = None
        if index >= 0 and index < self.tam():
            return_value = self.__elements[index]
        return return_value

    # def set_value(self, value, new_value, criterio=None):
    #     pos = self.search(value, criterio)
    #     if pos is not None:
    #         value = self.delete(value)
    #         self.insert(new_value, criterio)

    # ejercicio 15
    def barrido_entrenadores(self):
        for value in self.__elements:
            print(value[0])
            print('Lista de Pokemons:')
            value[1].barrido()
            print()
    
    def obtener_cantidad_pokemons(self,nombre_entrenador):
        indice = self.buscar(nombre_entrenador,'nombre')
        if indice is not None:
            cantidad_pokemons = self.elemento_indice(indice)[1].tam()
            return cantidad_pokemons
        else:
            return None
    
    def listado_entrenadores_torneos(self,torneos_ganados):
        for entrenador in self.__elements:
            if entrenador[0].ct_ganados > torneos_ganados:
                print(entrenador[0])
    
    def mostrar_info_entrenador(self,nombre_entrenador):
        indice = self.buscar(nombre_entrenador,'nombre')
        if indice is not None:
            print(f'\ninfo del entrenador {nombre_entrenador}')
            print(self.elemento_indice(indice)[0])
            print('info de sus pokemons')
            self.elemento_indice(indice)[1].barrido()
    
    def porcentaje_batallas_ganadas(self,mi_porcentaje):
        entrenadores = Lista()
        for entrenador in self.__elements:
            total = entrenador[0].cb_ganadas + entrenador[0].cb_perdidas
            if total > 0:
                porcentaje = (entrenador[0].cb_ganadas / total) * 100
                if porcentaje > mi_porcentaje:
                    entrenadores.insertar(entrenador[0].nombre,'nombre')
        entrenadores.barrido()
   
    def pokemon_mayor_nivel(self):
        mayor_cantidad = self.elemento_indice(0)[0].ct_ganados
        pos_mayor = 0

        for i in range(1, self.tam()):
            entrenador = self.elemento_indice(i)[0]
            if entrenador.ct_ganados > mayor_cantidad:
                pos_mayor = i 
                mayor_cantidad = entrenador.ct_ganados 
        valor = self.elemento_indice(pos_mayor)
        entrenador, pokemons = valor[0], valor[1] 
        
        if pokemons.tam() > 0:
            pokemon_mayor = pokemons.elemento_indice(0)
            for i in range(1, pokemons.tam()):
                pokemon = pokemons.elemento_indice(i)
                if pokemon.nivel > pokemon_mayor.nivel:
                    pokemon_mayor = pokemon 
            return f'el pokemon de mayor nivel es {pokemon_mayor.nombre} {pokemon_mayor.nivel} del entrenador {entrenador.nombre}'
    
    def pokemons_por_tipos(self):
        entrenadores = Lista()
        for i in range(self.tam()):
            entrenador = self.elemento_indice(i)[0]
            pokemons = self.elemento_indice(i)[1]
            tiene_tipos = False
            if pokemons.tam() >0:
                for i in range(pokemons.tam()):
                    pokemon = pokemons.elemento_indice(i)
                    if (pokemon.tipo == 'agua' and pokemon.subtipo == 'volador') or (pokemon.tipo == 'fuego' and pokemon.subtipo=='planta'):
                        tiene_tipos = True
                        break
                if tiene_tipos:
                    entrenadores.insertar(entrenador,'nombre')
        return entrenadores.barrido()

    def promedio_nivel(self,nombre_entrenador):
        indice = self.buscar(nombre_entrenador,'nombre')
        if indice is not None:
            for i in range(self.tam()):
                sublista_pokemon = self.elemento_indice(i)[1]
                total_niveles = 0
                if sublista_pokemon.tam()>0:
                    for i in range(sublista_pokemon.tam()):
                        pokemon = sublista_pokemon.elemento_indice(i)
                        cantidad_pokemons = sublista_pokemon.tam()
                        total_niveles += pokemon.nivel
                            
                    if cantidad_pokemons > 0:
                        promedio_niveles = total_niveles / cantidad_pokemons
                        return promedio_niveles
                    else:
                        return 0
        else:
            return None
    
    def entrenador_con_pokemon(self,nombre_pokemon):
        cantidad_pokemons = 0
        for i in range(self.tam()):
            sublista_pokemon = self.elemento_indice(i)[1]
            if sublista_pokemon.buscar(nombre_pokemon,'nombre') is not None:
                cantidad_pokemons += 1 
        return cantidad_pokemons 

    def pokemon_repetido(self):
        entrenadores = Lista()
        pokemon_vistos = {}
        for i in range(self.tam()):
            entrenador = self.elemento_indice(i)[0]
            sublista_pokemon = self.elemento_indice(i)[1]
            tiene_repetidos = False 
            if sublista_pokemon.tam()>0:
                for pokemon in sublista_pokemon.__elements:
                    if pokemon.nombre in pokemon_vistos:
                        tiene_repetidos = True
                        break
                    pokemon_vistos[pokemon.nombre] = True
                if tiene_repetidos:
                    entrenadores.insertar(entrenador,'nombre')
        return entrenadores.barrido()

    def determinado_pokemon(self,nombres_pokemon):
        entrenadores = Lista()
        for i in range(self.tam()):
            entrenador = self.elemento_indice(i)[0]
            sublista_pokemon = self.elemento_indice(i)[1]
            tiene_pokemon = False
            for pokemon in nombres_pokemon:
                if sublista_pokemon.buscar(pokemon,'nombre') is not None:
                    tiene_pokemon = True
                    break
            if tiene_pokemon:
                entrenadores.insertar(entrenador,'nombre')
        return entrenadores.barrido()

    def entrenador_tiene_pokemon(self,nombre_entrenador,nombre_pokemon):
        indice_entrenador = self.buscar(nombre_entrenador,'nombre')
        if indice_entrenador is not None:
            sublista_pokemon = self.elemento_indice(indice_entrenador)[1]
            indice_pokemon = sublista_pokemon.buscar(nombre_pokemon, 'nombre') 
            
            if indice_pokemon is not None:
                entrenador = self.elemento_indice(indice_entrenador)[0]
                sublista_pokemon = sublista_pokemon.elemento_indice(indice_pokemon)
                datos_pokemon = sublista_pokemon
                return entrenador, datos_pokemon
        
        return None
