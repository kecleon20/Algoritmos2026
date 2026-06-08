from copy import copy, deepcopy
from typing import Any


def crear_pila():
    """Crea y devuelve una nueva pila vacía."""
    return {
        'elements': []
    }


def push(pila, value: Any) -> None:
    """Apila un elemento en la cima de la pila."""
    pila['elements'].append(value)


def pop(pila) -> Any:
    """Desapila y devuelve el elemento de la cima."""
    if is_empty(pila):
        raise IndexError("No se puede desapilar de una pila vacía")
    return pila['elements'].pop()


def show(pila) -> None:
    """Muestra todos los elementos de la pila sin perderlos."""
    paux = crear_pila()
    
    # Vaciamos la pila original en paux mientras mostramos
    while size(pila) > 0:
        value = pop(pila)
        print(value)
        push(paux, value)
    
    # Reconstruimos la pila original desde paux
    while size(paux) > 0:
        value = pop(paux)
        push(pila, value)


def size(pila) -> int:
    """Devuelve la cantidad de elementos en la pila."""
    return len(pila['elements'])


def on_top(pila) -> Any:
    """Devuelve el elemento de la cima sin eliminarlo."""
    if is_empty(pila):
        return None
    return pila['elements'][-1]


def is_empty(pila) -> bool:
    """Devuelve True si la pila está vacía, False en caso contrario."""
    return size(pila) == 0


def copy_pila(pila):
    """Devuelve una copia superficial de la pila."""
    nueva = crear_pila()
    nueva['elements'] = copy(pila['elements'])
    return nueva


def deepcopy_pila(pila):
    """Devuelve una copia profunda de la pila."""
    nueva = crear_pila()
    nueva['elements'] = deepcopy(pila['elements'])
    return nueva