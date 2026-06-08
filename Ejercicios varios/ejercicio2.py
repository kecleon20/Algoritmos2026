from tda_pila import crear_pila, push, pop, is_empty, on_top

def eliminar_impares(pila):
    """
    Elimina todos los elementos impares de la pila.
    Deja solo números pares, manteniendo el orden original.
    """
    aux = crear_pila()
    
    # Paso 1 y 2: desapilar y filtrar pares
    while not is_empty(pila):
        elemento = pop(pila)
        if elemento % 2 == 0:  # es par
            push(aux, elemento)
    
    # Paso 3: reconstruir pila original (invertir el orden)
    while not is_empty(aux):
        push(pila, pop(aux))
    
    return pila