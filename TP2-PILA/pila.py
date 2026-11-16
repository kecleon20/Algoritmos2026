class Pila():

    def __init__(self):
        self.__items = []

    def tam(self):
        return len(self.__items)
    
    def apilar(self,data):
        self.__items.append(data)    
     
    def desapilar(self):
        if not self.es_vacia():
            return self.__items.pop()

    def tope(self):
        if not self.es_vacia():
            return self.__items[-1]
    
    def es_vacia(self):
        return len(self.__items) == 0

    # ejercicio 14
    def apilar_creciente(self,data):
        '''permite recibir valores y que estos queden en orden creciente'''
        pila = Pila()
        while not self.es_vacia() and self.tope()<data:
            pila.apilar(self.desapilar())
        self.apilar(data)
        while not pila.es_vacia():
            self.apilar(pila.desapilar())


