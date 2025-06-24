'''
Quadrados dos numeros pares.

Dada uma lista de numeros, retorne uma nova lista com os quadrados apenas dos
numeros pares.


'''

from random import randint
from functools import reduce


lista = [randint(1,10) for _ in range(5)]

resultado = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, lista)))

print(resultado)