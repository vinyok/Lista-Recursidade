'''
Soma com *args
Escreva uma funcao que aceita qualquer quantidade de argumentos numericos e
retorna a soma deles

'''
lista_num = [5,5,5]

def soma (*args):
    return sum(args)
print(soma(*lista_num))    