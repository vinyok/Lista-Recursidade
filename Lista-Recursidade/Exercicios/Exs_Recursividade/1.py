'''
Contagem regressiva com atraso

Implemente uma funcao recursiva contagem regressiva(n) que imprime uma contagem de n ate 0. Ao chegar a 0, deve imprimir "Boom!".
(Opcional: usar time.sleep(1) para simular contagem real.)

'''
import time

def cont_regressiva(n):
    if n < 0:
        return
    print(n)
    time.sleep(1)
    cont_regressiva(n - 1)
    if n == 0:
        print('Boom!')

user_choice = int(input('Escolha de onde começar a contagem regressiva: '))
cont_regressiva(user_choice)
