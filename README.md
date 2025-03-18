# Atividade Sorting N1

Por Anna Loz, Lucas Gadonski, Matheus Lofy, Pablo Lopes e Sabine Freiman.

### generate_data.py

```python
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
```

No método é gerada uma lista com um tamanho entre 1 e 1.000.000, ele recebe a quantidade através do parâmetro 'tamanho'. Os dados são salvos em um arquivo `.json` ou `.bin` e trata a exceção caso o formato especificado seja diferente.
