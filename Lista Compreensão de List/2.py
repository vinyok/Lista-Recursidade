'''
Filtrar strings com mais de 5 letras.

A partir de uma lista de palavras, retorne apenas as que tem mais de 5 caracteres

'''
from functools import reduce

palavras = ['mesa', 'garfo', 'árvore', 'janela', 'casa']

resultado = list(filter(lambda x: len(x) > 5, palavras))

print(resultado)

