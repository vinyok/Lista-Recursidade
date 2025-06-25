'''
Inverter string recursivamente

Escreva uma funcao recursiva que recebe uma string e retorna a string invertida.
Exemplo: "python" → "nohtyp"



'''
def inverter_string(s):
    if s == "":
        return s
    return s[-1] + inverter_string(s[:-1])


resultado = inverter_string("python")
print(resultado)