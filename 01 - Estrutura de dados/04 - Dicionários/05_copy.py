contatos = {"diego@gmail.com": {"nome": "Diego", "telefone": "4444-1645"}}

copia = contatos.copy()
copia["diego@gmail.com"] = {"nome": "Dinho"}

print(contatos["diego@gmail.com"])  # {"nome": "diego", "telefone": "4444-1645"}

print(copia["diego@gmail.com"])  # {"nome": "Dinho"}
