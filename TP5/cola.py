class Cola:
    def __init__(self):
        self.items = []

    def es_vacia(self):
        return len(self.items) == 0

    def arribo(self, item):
        self.items.append(item)

    def atencion(self):
        if self.es_vacia():
            return None
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)

    def en_frente(self):
        if self.es_vacia():
            return None
        return self.items[0]
    
    def mover_al_final(self):
        while not self.es_vacia():
            data = self.atencion()
            self.arribo(data)
            return data