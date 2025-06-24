'''
A3. Saudacao personalizada com **kwargs

Crie uma funcao saudar(**kwargs) que aceita os argumentos nome, idade e cidade, e monta uma mensagem personalizada.
Exemplo: "Ola, Joao de 30 anos, morador de Sao Paulo!"

'''

def saudar (**kwargs):
    nome = kwargs.get('nome')
    idade = kwargs.get('idade')
    cidade = kwargs.get('cidade')
    print(f'Olá, {nome} de {idade} anos, morador de {cidade}')
    
    

infos = {
    'nome': input('Digite seu nome: '), 
    'idade': int(input('Digite sua idade: ')), 
    'cidade': input('Digite sua cidade: ')
    }

saudar(**infos)
