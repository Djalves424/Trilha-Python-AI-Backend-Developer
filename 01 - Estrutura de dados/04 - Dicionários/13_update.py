contatos = {"diego@gmail.com": {"nome": "Diego", "telefone": "4444-1645"}}

contatos.update({"diego@gmail.com": {"nome": "Dinho"}})
print(contatos)  # {'diego@gmail.com': {'nome': 'Dinho'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'diego@gmail.com': {'nome': 'Dinho'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
