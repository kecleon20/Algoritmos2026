from lista import Lista 

class Superheroe:
    def __init__(self,nombre,aparicion,casa,biografia):
        self.nombre = nombre
        self.aparicion = aparicion
        self.casa = casa
        self.biografia = biografia
    
    def __str__(self):
        return f'{self.nombre} {self.aparicion} {self.casa}, {self.biografia}' 

superheroes = [
        {'name':'batman','year':1939,'comic':'dc','bio':'el caballero de la noche'},
        {'name':'linterna verde','year':1940,'comic':'dc','bio':'orden de las linternas'},
        {'name':'wolverine','year':1974,'comic':'marvel','bio':'garras de adamantium'},
        {'name':'dr. strange','year':1963,'comic':'dc','bio':'cirujano hechicero maestro'},
        {'name':'star lord','year':1986,'comic':'marvel','bio':'...'},
        {'name':'flash','year':1940,'comic':'dc','bio':'el velocista escarlata'},
        {'name':'mujer maravilla','year':1941,'comic':'dc','bio':'guerrera de las amazonas'},
        {'name':'deadpool','year':1991,'comic':'marvel','bio':'...'},
        {'name':'capitana marvel','year':1968,'comic':'marvel','bio':'traje azul y rojo'}, 
        {'name':'iron man','year':1963,'comic':'marvel','bio':'armadura de alta tecnologia'},
        ]

lista = Lista()
for valor in superheroes:
    lista.insertar(Superheroe(valor['name'].title(),
                              valor['year'],
                              valor['comic'],
                              valor['bio']),'nombre')

lista.barrido()
print('')
# punto a 
lista.eliminar_superheroe('Linterna Verde')
# punto b 
data = lista.mostrar_aparicion('Wolverine')
if data is not None:
    print(f'Wolverine aparecio en {data}')
else:
    print('Wolverine no esta en la lista')
# punto c 
data = lista.cambiar_casa('Dr. Strange','marvel')
if data:
    print('se cambio la casa de Dr. Strange a marvel')
else:
    print('Dr. Strange no esta en la lista')
# punto d 
nombres = lista.mostrar_en_bio()
if nombres:
    print('\nsuperheroes que con la palabra traje o armadura en la bio')
    for nombre in nombres:
        print(nombre)
# punto e 
nombres = lista.aparicion_superior(1963)
if nombres:
    print('\nsuperheroes con aparicion superior a 1963')
    for nombre in nombres:
        print(nombre)
# punto f 
data = lista.casa_personaje('Capitana Marvel')
if data is not None:
    print(f'\nCapitana Marvel es de {data}')
else:
    print('Capitana Marvel no esta en la lista')
data = lista.casa_personaje('Mujer Maravilla')
if data is not None:
    print(f'Mujer Maravilla es de {data}')
else:
    print('Mujer Maravilla no esta en la lista')
# punto g 
data = lista.mostrar_info('Flash')
if data is not None:
    print(data)
else:
    print('Flash no esta en la lista')
data = lista.mostrar_info('Star Lord')
if data is not None:
    print(data)
else:
    print('Star Lord no esta en la lista')
# punto h 
data = lista.superheroes_por_letra_inicial()
print('\nsuperheroes cuyo nombre comienza con la letras B M o S')
for superheroe in data:
    print(superheroe)
# punto i 
count_dc, count_marvel = lista.contar_por_casa()
print(f'\nsuperheroes de dc {count_dc}')
print(f'superheroes de marvel {count_marvel}')
