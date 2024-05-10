contatos = {"diego@gmail.com": {"nome": "Diego", "telefone": "4444-1645"}}

resultado = contatos.popitem()  # ('diego@gmail.com', {'nome': 'Diego', 'telefone': '4444-1645'})
print(resultado)

# contatos.popitem()  # KeyError
