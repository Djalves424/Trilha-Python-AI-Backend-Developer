nome = "Diego"
idade = 30
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

# dados = {"nome": "Diego", "idade": 30}  # , "profissao": "Programador", "linguagem": "Python"}
dados = {"nome": "Diego", "idade": 30, "profissao": "Programador", "linguagem": "Python"}

print("Olá me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s." % (
    nome, idade, profissao, linguagem))

print("Olá me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(
    nome, idade, profissao, linguagem))

print("Olá me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}.".format(
    linguagem, profissao, idade, nome))

print(
    "Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.".format(
        nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.".format(
    **dados))

print(
    f"Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.")

print("---------------------------------------------------------------------------------------------------------------")

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(nome, idade))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(age=idade, name=nome))
print(f"Nome: {nome} Idade: {idade} Saldo {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo {saldo:10.2f}")
