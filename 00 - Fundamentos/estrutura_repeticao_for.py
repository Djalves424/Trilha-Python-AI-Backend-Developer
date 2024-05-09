texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

#exemplo com a função iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print()
print("Executa no final do laço")

#exemplo com a função built-in range
for nulero in range(0, 51, 5):
    print(nulero, end=" ")
