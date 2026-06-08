from tda_pila import crear_pila, push, pop, size, is_empty, on_top, show

def contar_ocurrencias(pila, elemento_buscado):
    pila_aux = crear_pila()
    contador = 0
    
    while not is_empty(pila):
        dato = pop(pila)
        if dato == elemento_buscado:
            contador += 1
        push(pila_aux, dato)
    
    while not is_empty(pila_aux):
        dato = pop(pila_aux)
        push(pila, dato)
    
    return contador


if __name__ == "__main__":
    pila = crear_pila()
    
    # Cargar datos
    for valor in [3, 7, 3, 2, 3, 8, 1, 3, 5]:
        push(pila, valor)
    
    resultado = contar_ocurrencias(pila, 3)
    print(f"El número 3 aparece {resultado} veces")