class Pila:
    def __init__(self):
        self.__elementos = []

    def es_vacia(self):
        return len(self.__elementos) == 0

    def apilar(self, item):
        self.__elementos.append(item)

    def desapilar(self):
        if self.es_vacia():
            return None
        return self.__elementos.pop()

    def tamano(self):
        return len(self.__elementos)

    def cima(self):
        if self.es_vacia():
            return None
        return self.__elementos[-1]