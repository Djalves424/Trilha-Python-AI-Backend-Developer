contato = {"nome": "Diego", "telefone": "4444-1645"}

contato.setdefault("nome", "Giovanna")  # "Diego"
print(contato)  # {'nome': 'Diego', 'telefone': '4444-1645'}

contato.setdefault("idade", 30)  # 30
print(contato)  # {'nome': 'Diego', 'telefone': '3333-2221', 'idade': 30}
