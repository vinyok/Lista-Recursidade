'''
Funcao de formatacao flexivel
Crie uma funcao que usa **kwargs para formatar strings com placeholders personalizados.

Exemplo: formata("Ola {nome}, seja bem-vindo(a) a {cidade}.", nome="Ana",
cidade="Recife")


'''
def formatacao (string, **kwargs):
    print(string)

    return string.format(**kwargs)


resultado = formatacao ("Olá {nome}, seja bem-vindo(a) a {cidade}.", nome="Ana", cidade="Recife")
print(resultado) 