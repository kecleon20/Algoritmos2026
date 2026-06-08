

class nodoCola(object):
    """Clase nodo para la cola."""
    def __init__(self):
        self.info = None
        self.sig = None


class Cola(object):
    """Clase que representa la estructura Cola."""
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamano = 0


def crear_cola():
    """Crea y devuelve una nueva cola vacía."""
    return Cola()


def arribo(cola, dato):
    """Arriba el dato al final de la cola."""
    nodo = nodoCola()
    nodo.info = dato
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamano += 1


def atencion(cola):
    """Atiende el elemento en el frente de la cola y lo devuelve."""
    if cola_vacia(cola):
        raise IndexError("No se puede atender de una cola vacía")
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = None
    cola.tamano -= 1
    return dato


def cola_vacia(cola):
    """Devuelve True si la cola está vacía."""
    return cola.frente is None


def en_frente(cola):
    """Devuelve el valor almacenado en el frente de la cola."""
    if cola_vacia(cola):
        return None
    return cola.frente.info


def tamanio(cola):
    """Devuelve el número de elementos en la cola."""
    return cola.tamano


def mover_al_final(cola):
    """Mueve el elemento del frente de la cola al final."""
    dato = atencion(cola)
    arribo(cola, dato)
    return dato


def barrido(cola):
    """
    Muestra el contenido de una cola sin perder datos.
    Usa mover_al_final -> O(n)
    """
    i = 0
    while i < tamanio(cola):
        dato = mover_al_final(cola)
        print(dato)
        i += 1


