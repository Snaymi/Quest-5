def inverte_string(string):
    invertida = ""
    for char in string:
        invertida = char + invertida
    return invertida

# Teste
string = input("Digite uma string: ")
print(inverte_string(string))
