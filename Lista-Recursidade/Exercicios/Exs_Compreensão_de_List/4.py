'''
Flatten de lista de listas
A partir de uma lista de listas, crie uma lista plana.
Exemplo: [[1,2], [3,4], [5]] → [1,2,3,4,5]

'''
from itertools import chain

lista_de_listas = [[1, 2], [3, 4], [5]]

lista_plana = list(chain(*lista_de_listas))

print(lista_plana)  