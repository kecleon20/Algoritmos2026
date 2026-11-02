class Cola:
    def __init__(self):
        self.__elementos = []

    def es_vacia(self):
        return len(self.__elementos) == 0

    def arribo(self, item):
        self.__elementos.append(item)

    def atencion(self):
        if self.es_vacia():
            return None
        return self.__elementos.pop(0)

    def tamano(self):
        return len(self.__elementos)

    def en_frente(self):
        if self.es_vacia():
            return None
        return self.__elementos[0]