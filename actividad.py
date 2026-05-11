from pila import Pila
import random
pila = Pila()
pila1 = Pila()
for n in range(5):
    pila.apilar(random.randint(1,50))


# Diccionario para mapear direcciones a sus opuestas
DIRECCIONES_OPUESTAS = {
    'norte': 'sur',
    'sur': 'norte',
    'este': 'oeste',
    'oeste': 'este',
    'noreste': 'suroeste',
    'noroeste': 'sureste',
    'sureste': 'noroeste',
    'suroeste': 'noreste'
}


def registrar_movimientos():
    """
    Registra los movimientos del robot usando una pila
    """
    movimientos = Pila()
    
    print("=== REGISTRO DE MOVIMIENTOS DEL ROBOT ===")
    print("Direcciones válidas: norte, sur, este, oeste, noreste, noroeste, sureste, suroeste")
    print("Ingrese 'fin' para terminar el registro\n")
    
    while True:
        try:
            # Ingresar cantidad de pasos
            pasos_input = input("Cantidad de pasos (número positivo): ")
            if pasos_input.lower() == 'fin':
                break
            
            pasos = int(pasos_input)
            if pasos <= 0:
                print("Error: La cantidad de pasos debe ser positiva")
                continue
            
            # Ingresar dirección
            direccion = input("Dirección: ").lower()
            if direccion == 'fin':
                break
            
            # Validar dirección
            if direccion not in DIRECCIONES_OPUESTAS:
                print("Error: Dirección no válida")
                print("Direcciones válidas:", list(DIRECCIONES_OPUESTAS.keys()))
                continue
            
            # Guardar el movimiento como una tupla (pasos, direccion)
            movimiento = (pasos, direccion)
            movimientos.apilar(movimiento)
            print(f"Movimiento registrado: {pasos} pasos hacia {direccion}\n")
            
        except ValueError:
            print("Error: Ingrese un número válido para los pasos")
    
    return movimientos


def generar_camino_regreso(movimientos):
    """
    Genera la secuencia inversa para regresar al punto de partida
    """
    camino_regreso = Pila()
    
    print("\n=== GENERANDO CAMINO DE REGRESO ===")
    
    # Primero, transferimos a otra pila para invertir el orden
    pila_temp = Pila()
    while not movimientos.es_vacia():
        pila_temp.apilar(movimientos.desapilar())
    
    # Ahora pila_temp tiene el orden inverso (último movimiento primero)
    # Generamos los movimientos de regreso (dirección opuesta)
    while not pila_temp.es_vacia():
        pasos, direccion = pila_temp.desapilar()
        direccion_opuesta = DIRECCIONES_OPUESTAS[direccion]
        movimiento_regreso = (pasos, direccion_opuesta)
        camino_regreso.apilar(movimiento_regreso)
    
    return camino_regreso


def mostrar_movimientos(pila, titulo):
    """ Muestra los movimientos almacenados en una pila sin destruirla """
    print(f"\n=== {titulo} ===")
    
    # Para mostrar sin destruir la pila original
    pila_temp = Pila()
    while not pila.es_vacia():
        pila_temp.apilar(pila.desapilar())
    
    # Mostrar en orden y restaurar
    movimientos_lista = []
    while not pila_temp.es_vacia():
        movimientos_lista.append(pila_temp.desapilar())
    
    # Restaurar la pila original
    for movimiento in reversed(movimientos_lista):
        pila.apilar(movimiento)
    
    # Mostrar los movimientos
    if not movimientos_lista:
        print("No hay movimientos registrados")
    else:
        for i, (pasos, direccion) in enumerate(movimientos_lista, 1):
            print(f"{i}. {pasos} pasos hacia {direccion}")


def main():
    """
    Función principal que ejecuta el programa completo
    """
    print("PROGRAMA DE CONTROL DE ROBOT")
    print("=" * 40)
    
    # Registrar movimientos del robot
    movimientos_originales = registrar_movimientos()
    
    if movimientos_originales.es_vacia():
        print("\nNo se registraron movimientos. El programa terminará.")
        return
    
    # Mostrar movimientos registrados
    mostrar_movimientos(movimientos_originales, "MOVIMIENTOS DEL ROBOT (IDA)")
    
    # Generar camino de regreso
    camino_regreso = generar_camino_regreso(movimientos_originales)
    
    # Mostrar camino de regreso
    mostrar_movimientos(camino_regreso, "CAMINO DE REGRESO (VUELTA)")
    
    # Verificar que el robot vuelva al origen
    print("El robot ha regresado a su punto de partida siguiendo el camino inverso")


if __name__ == "__main__":
    main()

# actividad 24
class Personaje:
    def __init__(self,name,films):
        self.name = name
        self.films = films
    
    def __str__(self):
        return f'{self.name} {self.films}'

pila=Pila()

personajes = [
        {'name':'groot','films':3},
        {'name':'doctor strange','films':2},
        {'name':'rocket raccoon','films':3},
        {'name':'iron man','films':10},
        {'name':'captain america','films':9}, 
        {'name':'black widow','films':7},
        {'name':'ant-man','films':4},
        ]

for personaje in personajes:
    pila.apilar(Personaje(personaje['name'].title(),
                          personaje['films'],
                          ))

groot = 1 
rocketraccoon = 1 
while not pila.es_vacia():
    data = pila.desapilar()
    # punto a 
    if data.name == 'groot'.title():
       print(f'{data.name} esta en la posicion {groot}')
    groot+=1 
    if data.name == 'rocket raccoon'.title():
        print(f'{data.name} esta en la posicion {rocketraccoon}')
    rocketraccoon +=1 
    # punto b 
    if data.films>5:
        print(f'{data.name} participo en mas de 5 peliculas {data.films}')
    # punto c 
    if data.name == 'black widow'.title():
        print(f'{data.name} participo en {data.films} peliculas')
    # punto d 
    if data.name[0] == 'C' or data.name[0] == 'G' or data.name[0] == 'D':
        print(f'su nombre comienza con C G o D {data.name}')


























