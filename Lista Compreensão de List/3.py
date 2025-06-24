'''
Inverter palavras
Usando compreens˜ao de lista, inverta cada palavra de uma lista de strings.
Exemplo: ["casa", "gato"] → ["asac", "otag"]


'''

lista = ['casa', 'gato']

resultado = [palavra[::-1] for palavra in lista]
print(resultado)