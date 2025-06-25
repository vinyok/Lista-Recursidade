'''
Soma dos digitos de um numero
Escreva uma funcao recursiva que retorna a soma dos digitos de um numero inteiro
positivo.
Exemplo: soma digitos(1234) → 10


'''

def soma_digitos (n):
    if n == 0:
        return n
    return (n % 10) + soma_digitos (n // 10)

print(soma_digitos(1234))