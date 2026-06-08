from tda_pila import crear_pila, push, pop, is_empty

def reemplazar(pila, viejo, nuevo):
    """Reemplaza todas las ocurrencias de 'viejo' por 'nuevo'. Usa barrido."""
    aux = crear_pila()
    
    # Barrido: desapilar todo hacia aux
    while not is_empty(pila):
        dato = pop(pila)
        push(aux, dato)
    
    # Reconstrucción con reemplazos
    while not is_empty(aux):
        dato = pop(aux)
        if dato == viejo:
            push(pila, nuevo)
        else:
            push(pila, dato)