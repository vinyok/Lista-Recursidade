'''
Funcao de filtro com *args e **kwargs

Escreva uma funcao que aceita uma lista de numeros via *args e usa **kwargs para
aplicar filtros, como min=10, max=50.


'''

def filtrar_numeros(*args, **kwargs):
    return [num for num in args if 10 <= num <= 50]

# Exemplo de uso
resultado = filtrar_numeros(n1 = 1, n2 = 3)

print(resultado)
