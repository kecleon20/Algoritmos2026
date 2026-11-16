from arbol_binario import BinaryTree

arbol = BinaryTree()

datos = [
    {'nombre': 'Ceto', 'derrotado':None},
    {'nombre': 'Tifon', 'derrotado': 'Zeus'},
    {'nombre': 'Esquidna', 'derrotado': 'Argos Panoptes'},
    {'nombre': 'Dino', 'derrotado':None},
    {'nombre': 'Pefredo', 'derrotado':None},
    {'nombre': 'Enio', 'derrotado': None},
    {'nombre': 'Escila', 'derrotado': None},
    {'nombre': 'Caribdis', 'derrotado': None},
    {'nombre': 'Euriale', 'derrotado': None},
    {'nombre': 'Esteno', 'derrotado': None},
    {'nombre': 'Medusa', 'derrotado': 'Perseo'},
    {'nombre': 'Ladon', 'derrotado': 'Heracles'},
    {'nombre': 'Aguila del Caucaso ', 'derrotado': None},
    {'nombre': 'Quimera', 'derrotado': 'Belerofonte'},
    {'nombre': 'Hidra de Lerna', 'derrotado': 'Heracles'},
    {'nombre': 'Leon de Nemea', 'derrotado': 'Heracles'},
    {'nombre': 'Esfinge', 'derrotado': 'Edipo'},
    {'nombre': 'Dragon de la Colquida', 'derrotado':None},
    {'nombre': 'Cerbero', 'derrotado': None},
    {'nombre': 'Cerda de Cromion', 'derrotado': 'Teseo'},
    {'nombre': 'Ortro', 'derrotado': 'Heracles'},
    {'nombre': 'Toro de Creta', 'derrotado': 'Teseo'},
    {'nombre': 'Jabali de Calidon', 'derrotado': 'Atalanta'},
    {'nombre': 'Carcinos', 'derrotado': None},
    {'nombre': 'Gerion', 'derrotado': 'Heracles'},
    {'nombre': 'Cloto', 'derrotado': None},
    {'nombre': 'Laquesis', 'derrotado': None},
    {'nombre': 'Atropos', 'derrotado': None},
    {'nombre': 'Minotauro de Creta', 'derrotado': 'Teseo'},
    {'nombre': 'Harpias', 'derrotado': None},
    {'nombre': 'Argos Panoptes', 'derrotado': 'Hermes'},
    {'nombre': 'Talos', 'derrotado': 'Medea'},
    {'nombre': 'Sirenas', 'derrotado': None},
    {'nombre': 'Piton', 'derrotado': 'Apolo'},
    {'nombre': 'Cierva de Cerinea', 'derrotado':None},
    {'nombre': 'Basilisco', 'derrotado':None},
    {'nombre': 'Aves del Estinfalo','derrotado':None},
    {'nombre': 'Jabali de Erimanto', 'derrotado': None}
]

for criatura in datos:
    arbol.insert_node(criatura['nombre'], {'derrotado': criatura['derrotado']})

arbol.inorden_add_field_description()
arbol.inorden_add_field_captured()

# punto a 
arbol.inorden_criatura_defeat_by()

# punto b 
creature_name = input('Criatura ')
pos = arbol.search(creature_name)
if pos is not None:
    descripcion = input('Descripcion ')
    arbol.inorden_add_description(creature_name, descripcion)
else:
    print(f'{creature_name} no esta en el arbol')

# punto c
print('\nInformacion de Talos')
pos = arbol.search('Talos')
if pos:
    print(f'{pos.value} {pos.other_values}')
else:
    print('Talos no esta en el arbol')

# punto d 
print('\nHan derrotado mayor cantidad de criaturas')
dic_ranking = {}
arbol.inorden_ranking(dic_ranking)
def order_by(item):
    return item[1]
ordenado = list(dic_ranking.items())
ordenado.sort(key=order_by, reverse=True)
print(ordenado[:3])

# punto e 
print('\nCriaturas derrotadas por Heracles')
arbol.inorden_defeated_by('Heracles')

# punto f 
print('\nCriaturas que no fueron derrotadas')
arbol.inorden_not_defeated()

# punto g 
capturadores = {
        'Medusa':'Teseo',
        'Tifon':'Heracles',
        'Toro de Creta':'Heracles'
        }
arbol.inorden_add_capturer(capturadores)

# punto h 
print('\nModificando capturadores')
modificar_criaturas = ['Cerbero','Toro de Creta','Cierva de Cerinea','Jabali de Erimanto']
for criatura in modificar_criaturas:
    pos = arbol.search(criatura)
    if pos is not None:
        pos.other_values['capturada'] = 'Heracles'
    else:
        print(f'{criatura} no esta en el arbol')

# punto i
print('\nBusqueda por coincidencia')
arbol.search_by_coincidence('Me')

# punto j 
print('\nSe eliminaran los nodos de Basilisco y Sirenas')
pos = arbol.search('Basilisco')
if pos is not None:
    arbol.delete_node('Basilisco')
else:
    print('Basilisco no esta en el arbol')

pos = arbol.search('Sirenas')
if pos is not None:
    arbol.delete_node('Sirenas')
else:
    print('Sirenas no estan en el arbol')

# punto k
print('\nSe modifico la descripcion de Aves del Estinfalo')
pos = arbol.search('Aves del Estinfalo')
if pos is not None:
    pos.other_values['descripcion'] += ' Heracles derroto a varias'
else:
    print('Aves del Estinfalo no esta en el arbol')
descripcion = pos.other_values['descripcion']
print(f'Descripcion modificada {descripcion}')

# punto l 
print('\nSe modifica el nombre de Ladon')
pos = arbol.search('Ladon')
if pos is not None:
    pos.value = 'Dragon de Ladon'
else:
    print(f'{pos} no esta en el arbol')

# punto m
print('\nListado por nivel del arbol')
arbol.by_level()

# punto n 
print('\nCriaturas capturadas por Heracles')
arbol.inorden_captured_by('Heracles')
