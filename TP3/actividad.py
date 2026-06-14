# ejercicios a entregar 10 16 22 
from cola import Cola 
from pila import Pila
from heap import Heap

# actividad 10 
notificaciones = [
        {'app':'facebook','hora':'14:30','mensaje':'nuevo mensaje de asdasd'},
        {'app':'twitter','hora':'11:30','mensaje':'hola mundo en python'},
        {'app':'telegram','hora':'15:00','mensaje':'asdasda'},
        ]

cola = Cola()
cola1 = Cola()
pila  = Pila()

for notificacion in notificaciones:
    cola.arribo(notificacion)
while not cola.es_vacia():
    data = cola.atencion()
    if data['app'] != 'facebook':
        cola1.arribo(data)
while not cola1.es_vacia():
    cola.arribo(cola1.atencion())
for i in range(cola.tamano()):
    data = cola.mover_al_final()
    if data['app'] == 'twitter' and 'python' in data['mensaje']:
        print(data['hora'],data['app'],data['mensaje'])
for i in range(cola.tamano()):
    data = cola.mover_al_final()
    if data['hora'] >= '11:43' and data['hora'] <= '15:57':
        pila.apilar(data)
print('cantidad de notificaciones en la pila',pila.tam())
while not cola.es_vacia():
    print(cola.atencion())


print('')

# actividad 22 
cola = Cola()
class Superheroe:
    def __init__(self,nombre,personaje,sexo):
        self.nombre = nombre
        self.personaje = personaje 
        self.sexo = sexo

    def __str__(self):
        return f'{self.nombre}  {self.personaje}  {self.sexo}' 

personajes = [
        {'name':'tony stark','nick':'iron man','sex':'m'},
        {'name':'steve rogers','nick':'captian america','sex':'m'},
        {'name':'natasha romanoff','nick':'black widow','sex':'f'},
        {'name':'peter parker','nick':'spiderman','sex':'m'},
        {'name':'scott lang','nick':'ant man','sex':'m'},
        {'name':'carol danvers','nick':'captain marvel','sex':'f'},
        ]

for personaje in personajes:
    cola.arribo(Superheroe(personaje['name'].title(),
                       personaje['nick'].title(),
                       personaje['sex'].title(),
                       ))

encontrado = False
while not cola.es_vacia():
    data = cola.atencion()
    if data.personaje == 'captain marvel'.title():
        print(f'el nombre de {data.personaje} es {data.nombre}')
    if data.sexo == 'F':
        print(f'personaje femenino {data.personaje}')
    if data.sexo == 'M':
        print(f'personaje masculino {data.personaje}')
    if data.nombre == 'scott lang'.title():
        print(f'{data.nombre} es el superheroe {data.personaje}')
    if data.personaje[0] == 'S':
        print(f'comienza con S {data.personaje}')
    if data.nombre == 'carol danvers'.title():
        encontrado = True
        nombre = data.nombre
        superheroe = data.personaje

if encontrado:
    print(f'{nombre} esta en la cola su nombre de superheroe es {superheroe}')
else:
    print('{nombre} no esta en la cola')


print('')

# actividad 16 
cola = Heap()

# punto a
cola.add_element(('doc1',1))
cola.add_element(('doc2',1))
cola.add_element(('doc3',1))

# punto b
print(f'\nprimer documento {cola.remove_element()[0]}')

# punto c
cola.add_element(('doc4', 2))
cola.add_element(('doc5',2))

# punto d
cola.add_element(('doc6', 3))

# punto e
print('\nlos dos primeros documentos')
print(cola.remove_element()[0])
print(cola.remove_element()[0])

# punto f
cola.add_element(('doc7',1))
cola.add_element(('doc8',1))
cola.add_element(('doc9',3))

# punto g
print('\ndocumentos')
while cola.size() > 0:
    print(cola.remove_element()[0])