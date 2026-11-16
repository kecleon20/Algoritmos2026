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
        if len(self.__elements) == 0 or criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[-1], criterio):
            self.__elements.append(value)
        elif criterio_comparacion(value, criterio) < criterio_comparacion(self.__elements[0], criterio):
            self.__elements.insert(0, value)
        else:
            index = 1
            while criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[index], criterio):
                index += 1
            self.__elements.insert(index, value)

    def buscar(self, search_value, criterio=None):
        position = None
        first = 0
        last = self.tam() - 1
        while (first <= last and position == None):
            middle = (first + last) // 2
            if search_value == criterio_comparacion(self.__elements[middle], criterio):
                position = middle
            elif search_value > criterio_comparacion(self.__elements[middle], criterio):
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
            print(value)

    def reordenar(self, criterio=None, reverse=False):
        dic_atributos = self.__elements[0].__dict__
        if criterio in dic_atributos:
            def func_criterio(valor):
                return valor.__dict__[criterio]

            self.__elements.sort(key=func_criterio, reverse=reverse)
        else:
            print('no se puede ordenar por este criterio')

    # def get_element_by_value(self, value):
    #     return_value = None
    #     pos = self.search(value)

    #     if pos is not None:
    #         return_value = self.__elements[pos]
    #     return return_value

    def elemento_indice(self, index):
        return_value = None
        if index >= 0 and index < self.tam():
            return_value = self.__elements[index]
        return return_value 


    def modificar_valor(self, value, new_value, criterio=None):
        pos = self.buscar(value, criterio)
        if pos is not None:
            value = self.eliminar(value,criterio)
            self.insertar(new_value, criterio)


    # ejercicio 6
    # punto a 
    def eliminar_superheroe(self,nombre):
        self.eliminar(nombre,'nombre')
    # punto b 
    def mostrar_aparicion(self,nombre):
        indice = self.buscar(nombre,'nombre')
        if indice is not None:
            superheroe = self.elemento_indice(indice)
            return superheroe.aparicion
        else:
            return None
    # punto c 
    def cambiar_casa(self,nombre,nueva_casa):
        indice = self.buscar(nombre,'nombre')
        if indice is not None:
            superheroe = self.elemento_indice(indice)
            superheroe.casa = nueva_casa 
            return True
        else:
            return False
    # punto d 
    def mostrar_en_bio(self):
        superheroes = []
        for superheroe in self.__elements:
            if 'traje' in superheroe.biografia.lower() or 'armadura' in superheroe.biografia.lower():
                superheroes.append(superheroe.nombre)
        return superheroes    
    # punto e  
    def aparicion_superior(self,anio):
        superheroes= []
        for superheroe in self.__elements:
            if superheroe.aparicion > anio:
                superheroes.append(superheroe.nombre)
        return superheroes
    # punto f   
    def casa_personaje(self,nombre):
        indice = self.buscar(nombre,'nombre')
        if indice is not None:
            data = self.elemento_indice(indice)
            return data.casa
        else:
            return None
    # punto g 
    def mostrar_info(self,nombre):
        indice = self.buscar(nombre,'nombre')
        if indice is not None:
            data = self.elemento_indice(indice)
            return data
        else:
            return None
    # punto h 
    def superheroes_por_letra_inicial(self):
        superheroes =[]
        for superheroe in self.__elements:
            if superheroe.nombre[0] in ['B','M','S']:
                superheroes.append(superheroe.nombre)
        return superheroes
    # punto i 
    def contar_por_casa(self):
        marvel = 0
        dc = 0 
        for superheroe in self.__elements:
            if superheroe.casa == 'dc':
                dc += 1 
            marvel += 1 
        return dc, marvel