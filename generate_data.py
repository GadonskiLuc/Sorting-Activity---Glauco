import random
import json
import pickle

def gerar_dados(tamanho, formato="json"):
   
    dados = [random.randint(1, 1000000) for _ in range(tamanho)]
    
    if formato == "json":
        with open(f"./data/dados_{tamanho}.json", "w") as f:
            json.dump(dados, f)
    elif formato == "bin":
        with open(f"dados_{tamanho}.bin", "wb") as f:
            pickle.dump(dados, f)
    else:
        raise ValueError("Formato inválido. Escolha 'json' ou 'bin'.")
    
    print(f"Arquivo 'dados_{tamanho}.{formato}' gerado com sucesso!")

# Exemplo de uso
gerar_dados(1000, "json")
gerar_dados(10000, "json")
