from pila import Pila

class Personaje():
    def __init__(self,name,films):
        self.name = name
        self.films = films

    def __str__(self):
        return self.name + ' ' + str(self.films)

pila = Pila()

personajes = [
        {'nick':'rocket raccoon','cant':3}, 
        {'nick':'black widow','cant':6},
        {'nick':'iron man','cant':6},
        {'nick':'groot','cant':3},
        {'nick':'captain america','cant':5},
        {'nick':'hulk','cant':5},
        ]

for personaje in personajes:
    pila.apilar(Personaje(personaje['nick'].title(),
                            personaje['cant'],
                          ))

indice = 0
while not pila.es_vacia():
    data = pila.desapilar()
    if data.name == 'groot' or data.name == 'rocket raccoon':
        print('groot esta en la pila')
















