'''
Funcao de filtro com *args e **kwargs

Escreva uma funcao que aceita uma lista de numeros via *args e usa **kwargs para
aplicar filtros, como min=10, max=50.


'''

def filtrar_numeros(*args, **kwargs):
    minimo = kwargs.get('min', float('-inf'))
    maximo = kwargs.get('max', float('inf'))
    numeros_filtrados = [num for num in args if minimo <= num <= maximo]

    return numeros_filtrados

min_user = int(input('Digite o limite mínimo: '))
max_user = int(input('Digite o limite máximo: '))

resultado = filtrar_numeros(5, 15, 25, 35, 45, 55, min=min_user, max=max_user)
print(resultado) 
