from lista_lista import Lista
from random import randint

class Entrenador():

    def __init__(self, nombre, ct_ganados, cb_perdidas, cb_ganadas):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas

    def __str__(self):
        return f'{self.nombre} --> ctg:{self.ct_ganados} cbg:{self.cb_ganadas} cbp:{self.cb_perdidas}'

class Pokemon():

    def __init__(self, nombre, tipo, nivel, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre} {self.nivel} {self.tipo} {self.subtipo}'


e1 = Entrenador('Ash', ct_ganados=randint(1, 10),cb_ganadas=randint(1,100),cb_perdidas=randint(1,100))
e2 = Entrenador('Brock', ct_ganados=randint(1, 10),cb_ganadas=randint(1,100),cb_perdidas=randint(1,100))
e3 = Entrenador('Misty', ct_ganados=randint(1, 10),cb_ganadas=randint(1,100),cb_perdidas=randint(1,100))
entrenadores = [e1, e2, e3]

lista_entrenadores = Lista()

p1 = Pokemon('pikachu', 'electrico', randint(1, 20),'volador')
p2 = Pokemon('jolteon', 'electrico', randint(1, 20),'tierra')
p3 = Pokemon('vaporeon', 'agua', randint(1, 20),'volador')
p4 = Pokemon('flareon', 'fuego', randint(1, 20),'planta')
p5 = Pokemon('leafeon', 'planta', randint(1, 20),'electrico')
p6 = Pokemon('pikachu', 'electrico', randint(1, 20),'volador')
p7 = Pokemon('tyrantrum', 'roca', randint(1, 20),'volador')
p8 = Pokemon('terrakion', 'volador', randint(1, 20),'roca')
p9 = Pokemon('wingull', 'agua', randint(1, 20),'volador')

pokemons = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

# lista principal
for entrenador in entrenadores:
    lista_entrenadores.insertar(entrenador,'nombre')

# lista secundaria
for pokemon in pokemons:
    indice_entrenador = randint(0,lista_entrenadores.tam()-1)
    entrenador_actual = lista_entrenadores.elemento_indice(indice_entrenador)
    entrenador_actual[1].insertar(pokemon, 'nombre')


lista_entrenadores.barrido_entrenadores()

print()

# punto a 
nombre = 'Ash'
data = lista_entrenadores.obtener_cantidad_pokemons(nombre)
if data is not None:
    print(f'{nombre} tiene {data} pokemons')
else:
    print(f'{nombre} no esta en la lista')
# punto b 
print('\nlistado de entrenadores con mas de 3 torneos ganados')
lista_entrenadores.listado_entrenadores_torneos(3)
# punto c
print()
data = lista_entrenadores.pokemon_mayor_nivel()
print(data)
# punto d
nombre = 'Misty'
lista_entrenadores.mostrar_info_entrenador(nombre)
# punto e
print('\nentrenadores con un porcentaje mayor al 79% de batallas ganadas')
lista_entrenadores.porcentaje_batallas_ganadas(79)
# punto f 
print('\nentrenadores que tengan pokemons del tipo agua y subtipo planta o agua/volador')
lista_entrenadores.pokemons_por_tipos()
# punto g
data = lista_entrenadores.promedio_nivel('Ash')
if data is not None:
    print(f'\npromedio de niveles del entrenador {data}')
else:
    print('el entrenador no esta en la lista')
# punto h 
pokemon = 'pikachu'
data = lista_entrenadores.entrenador_con_pokemon(pokemon)
if data is not None:
    print(f'entrenadores que tienen a {pokemon} {data}')
else:
    print('nadie tiene al pokemon {pokemon}')
# punto i
print('\nentrenadores con pokemons repetidos')
lista_entrenadores.pokemon_repetido()
# punto j 
print('\nentrenadores que tienen a tyrantrum, terrakion, wingull')
pokemons_buscados = ['tyrantrum','terrakion','wingull']
lista_entrenadores.determinado_pokemon(pokemons_buscados)
# punto k
print('')
nombre_entrenador = 'Ash'
nombre_pokemon = 'pikachu' 
resultado = lista_entrenadores.entrenador_tiene_pokemon(nombre_entrenador, nombre_pokemon)
if resultado is not None:
    entrenador, pokemon = resultado
    print(f'el entrenador {nombre_entrenador} tiene el pokemon {nombre_pokemon}')
    print('datos del entrenador')
    print(entrenador)  
    print('datos del pokemon')
    print(f'nombre: {pokemon.nombre}')
    print(f'nivel: {pokemon.nivel}')
    print(f'tipo: {pokemon.tipo}')
    print(f'subtipo: {pokemon.subtipo}')
else:
    print(f'el entrenador {nombre_entrenador} tiene el pokemon {nombre_pokemon}')