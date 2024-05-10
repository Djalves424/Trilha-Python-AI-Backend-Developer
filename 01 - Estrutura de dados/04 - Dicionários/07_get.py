contatos = {"diego@gmail.com": {"nome": "Diego", "telefone": "4444-1645"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "diego@gmail.com", {}
)  # {"diego@gmail.com": {"nome": "Diego", "telefone": "4444-1645"}
print(resultado)
