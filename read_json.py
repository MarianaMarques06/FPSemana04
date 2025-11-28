import json
import os

arquivo = input()

if not os.path.exists(arquivo):
    print("Erro: Ficheiro Não Encontrado!")
else:
    with open(arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read().strip()

    try:
        dados = json.loads(conteudo)
    except:
        print("Erro: Ficheiro Não Contém JSON Válido!")
        print("Processo Concluído!")
        exit()

    if dados == {}:
        print("Erro: Ficheiro Vazio!")

    elif isinstance(dados, dict):
        campos = ["nome", "idade", "localização"]
        faltam = False
        for c in campos:
            if c not in dados:
                faltam = True
                break

        if faltam:
            print("Erro: Campos Obrigatórios em Falta!")
        else:

            print(dados)
    else:

        print("Erro: Ficheiro Não Contém JSON Válido!")


print("Processo Concluído!")
