import json
from arbol_binario import BinaryTree
from cola import Cola

class Pokemon:
    def __init__(self, nombre, numero, tipos, debilidades, mega, gigamax):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos 
        self.debilidades = debilidades 
        self.mega = mega 
        self.gigamax = gigamax 

    def __str__(self):
        return f"#{self.numero:04d} - {self.nombre.ljust(15)} | Tipos: {str(self.tipos).ljust(25)} | Debilidades: {str(self.debilidades).ljust(30)} | Mega: {self.mega} | Giga: {self.gigamax}"

# --- CARGA DE DATOS DESDE JSON ---
ARCHIVO_JSON = "pokemons_1025.json"

def cargar_pokemons_json(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        return [Pokemon(d['nombre'], d['numero'], d['tipos'], d['debilidades'], d['mega'], d['gigamax']) for d in datos]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}. Ejecuta 'crear_base_datos.py' primero.")
        return []

# --- 1. CONSTRUCCIÓN DE ÁRBOLES ---
arbol_numero = BinaryTree()
arbol_nombre = BinaryTree()
arbol_tipo = BinaryTree()

print(f"Cargando datos desde {ARCHIVO_JSON}...")
lista_pokemons = cargar_pokemons_json(ARCHIVO_JSON)

for p in lista_pokemons:
    arbol_numero.insert_node(p.numero, p)
    arbol_nombre.insert_node(p.nombre, p)
    for t in p.tipos:
        clave_compuesta = f"{t.lower()}-{p.nombre.lower()}"
        arbol_tipo.insert_node(clave_compuesta, p)

print(f"¡Carga exitosa! Total: {len(lista_pokemons)} Pokémons.\n")

# ==============================================================================
# --- 2. RESOLUCIÓN DE CONSIGNAS ---
# ==============================================================================

print("="*70)
print("1 y 2. BUSQUEDA POR NUMERO Y POR NOMBRE (PROXIMIDAD)")
print("="*70)
n_buscado = 25
nodo_num = arbol_numero.search(n_buscado)
print(f"\nDatos del Pokémon Nro {n_buscado}:")
if nodo_num:
    print(nodo_num.other_values)
else:
    print("No encontrado.")

prefijo = "char"
print(f"\nBúsqueda por proximidad de nombre: '{prefijo}'")
# Usamos una función recursiva para imprimir los datos completos
def buscar_proximidad(root, prefijo, contador=[0]):
    if root is not None and contador[0] < 100:
        buscar_proximidad(root.left, prefijo, contador)
        if root.value.lower().startswith(prefijo.lower()) and contador[0] < 100:
            print(root.other_values)
            contador[0] += 1
        buscar_proximidad(root.right, prefijo, contador)
buscar_proximidad(arbol_nombre.root, prefijo)


print("\n" + "="*70)
print("3. NOMBRES POR TIPO (FANTASMA, FUEGO, ACERO, ELECTRICO)")
print("="*70)
tipos_buscar = ["fantasma", "fuego", "acero", "eléctrico"]
for t in tipos_buscar:
    print(f"\nTipo {t.capitalize()} (primeros 100):")
    cont = [0] # Usamos una lista para evitar el problema de nonlocal
    
    def buscar_tipo_limitado(root, prefijo):
        if root is not None and cont[0] < 100:
            buscar_tipo_limitado(root.left, prefijo)
            if root.value.startswith(prefijo) and cont[0] < 100:
                nombre_pokemon = root.value.split('-')[1]
                print(f"  - {nombre_pokemon.capitalize()}")
                cont[0] += 1 # Modificamos el primer elemento de la lista
            buscar_tipo_limitado(root.right, prefijo)
            
    buscar_tipo_limitado(arbol_tipo.root, t)


print("\n" + "="*70)
print("4. LISTADO ASCENDENTE POR NUMERO Y POR NOMBRE (Primeros 100)")
print("="*70)
print("\n--- Listado Ascendente por Número ---")
contador = [0]
def mostrar_inorden_limitado(root):
    if root is not None and contador[0] < 100:
        mostrar_inorden_limitado(root.left)
        if contador[0] < 100:
            print(f"#{root.value} - {root.other_values.nombre}")
            contador[0] += 1
        mostrar_inorden_limitado(root.right)
mostrar_inorden_limitado(arbol_numero.root)

print("\n--- Listado Ascendente por Nombre ---")
contador = [0]
def mostrar_inorden_nombres(root):
    if root is not None and contador[0] < 100:
        mostrar_inorden_nombres(root.left)
        if contador[0] < 100:
            print(root.value)
            contador[0] += 1
        mostrar_inorden_nombres(root.right)
mostrar_inorden_nombres(arbol_nombre.root)


print("\n" + "="*70)
print("5. LISTADO POR NIVEL (POR NOMBRE - Primeros 100)")
print("="*70)
def mostrar_por_nivel_limitado(root):
    if root is not None:
        cola = Cola()
        cola.arribo(root)
        cont = 0
        while not cola.es_vacia() and cont < 100:
            nodo = cola.atencion()
            print(nodo.value)
            cont += 1
            if nodo.left: cola.arribo(nodo.left)
            if nodo.right: cola.arribo(nodo.right)
mostrar_por_nivel_limitado(arbol_nombre.root)


print("\n" + "="*70)
print("6. POKÉMONS DÉBILES FRENTE A JOLTEON, LYCANROC Y TYRANTRUM (Primeros 100)")
print("="*70)
tipos_debiles = ["Eléctrico", "Roca", "Dragón"]
cont_debiles = [0]
def buscar_debiles(root):
    if root is not None and cont_debiles[0] < 100:
        buscar_debiles(root.left)
        pokemon = root.other_values
        if any(d in pokemon.debilidades for d in tipos_debiles) and cont_debiles[0] < 100:
            print(pokemon)
            cont_debiles[0] += 1
        buscar_debiles(root.right)
buscar_debiles(arbol_numero.root)


print("\n" + "="*70)
print("7. TODOS LOS TIPOS Y CUÁNTOS HAY DE CADA TIPO")
print("="*70)
def contar_tipos(root):
    if root is not None:
        contar_tipos(root.left)
        tipo = root.value.split('-')[0]
        if tipo not in conteo_tipos:
            conteo_tipos[tipo] = 1
        else:
            conteo_tipos[tipo] += 1
        contar_tipos(root.right)

conteo_tipos = {}
contar_tipos(arbol_tipo.root)
for tipo, cant in sorted(conteo_tipos.items()):
    print(f"{tipo.capitalize()}: {cant}")


print("\n" + "="*70)
print("8 y 9. CANTIDAD DE POKÉMONS CON MEGA Y GIGAMAX")
print("="*70)
def contar_mega_giga(root):
    if root is not None:
        contar_mega_giga(root.left)
        if root.other_values.mega:
            conteo['mega'] += 1
        if root.other_values.gigamax:
            conteo['giga'] += 1
        contar_mega_giga(root.right)

conteo = {'mega': 0, 'giga': 0}
contar_mega_giga(arbol_numero.root)
print(f"Pokémons con Megaevolución: {conteo['mega']}")
print(f"Pokémons con Gigamax: {conteo['giga']}")
print("="*70)