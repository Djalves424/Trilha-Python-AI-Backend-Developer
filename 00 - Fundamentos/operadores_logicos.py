print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

balance = 1000
withdraw = 250
limit = 200
conta_especial = True

exp = balance >= withdraw and withdraw <= limit or conta_especial and balance >= withdraw
print(exp)

exp2 = (balance >= withdraw and withdraw <= limit) or (conta_especial and balance >= withdraw)
print(exp2)

conta_normal_com_saldo_suficiente = balance >= withdraw and withdraw <= limit
conta_especial_com_saldo_suficiente = conta_especial and balance >= withdraw

exp3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp3)
