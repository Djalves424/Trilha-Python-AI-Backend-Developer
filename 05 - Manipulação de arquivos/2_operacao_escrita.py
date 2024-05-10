arquivo = open(
    "C:/Users/Diego Alves/Documents/Projetos Python/trilha-python-dio/05 - Manipulação de arquivos/teste.txt", "w"
)
arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["/n", "escrevendo", "/n", "um", "/n", "novo", "/n", "texto"])
arquivo.close()
