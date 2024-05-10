contatos = {"diego@gmail.com": {"nome": "Diego", "telefone": "4444-1645"}}

resultado = contatos.pop("diego@gmail.com")  # {'nome': 'Diego', 'telefone': '4444-1645'}
print(resultado)

resultado = contatos.pop("diego@gmail.com", {})  # {}
print(resultado)
