'''
Multiplicacao com *args e verificacao de tipo

Crie uma funcao que multiplica todos os argumentos numericos, ignorando qualquer
argumento que nao seja int ou float.

'''
from functools import reduce

lista_num = [5,5,5]

def multiplicacao (*args):
    return reduce(lambda count, item: count * item if isinstance(item, (int, float)) else 0, args, 1)
        
print(multiplicacao(*lista_num))    