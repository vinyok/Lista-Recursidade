'''
Pares de numeros (produto cartesiano)

Dadas duas listas de numeros, gere todos os pares possiveis entre elementos de uma e de outra.
Exemplo: [1,2] e [3,4] → [(1,3), (1,4), (2,3), (2,4)]

'''

lista1 = [1,2,3]

lista2 = [4,5,6]

resultado = [(x, y) for x in lista1 for y in lista2]

print(resultado)