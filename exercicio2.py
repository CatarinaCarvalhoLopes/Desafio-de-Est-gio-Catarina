def contar_a(string):
    return string.lower().count('a')

texto = input("Digite uma string: ")
quantidade = contar_a(texto)
print(f"A letra 'a' aparece {quantidade} vezes na string.")
