from pila import *
import random
from random import choice 
import string


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







