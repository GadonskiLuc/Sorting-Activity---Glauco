# Sorting Activity

### Membros da Equipe

Por Anna Loz, Lucas Gadonski, Matheus Lofy, Pablo Lopes e Sabine Freiman.

## 1. Objetivo do Código

Este documento descreve a implementação de um sistema para comparar o desempenho de diferentes algoritmos de ordenação. O código permite:

- Gerar dados aleatórios para teste;
- Aplicar diferentes algoritmos de ordenação;
- Comparar os tempos de execução;
- Visualizar os resultados em gráficos comparativos.

## 2. Geração de Dados Aleatórios

O código inclui uma função para criar listas de números aleatórios e armazená-los em arquivos para análise.

### 2.1 Função `gerar_dados`

A função `gerar_dados(tamanho, formato)` gera números aleatórios e os salva em arquivos nos formatos JSON ou binário (BIN):

- **Formato JSON**: Serializa os dados como um arquivo de texto estruturado;
- **Formato BIN**: Usa o módulo `pickle` para armazenar os dados de forma binária.

### 2.2 Exemplo de Arquivos Gerados

- `dados_1000.json` (1.000 números aleatórios);
- `dados_10000.json` (10.000 números aleatórios).

## 3. Ordenação dos Dados

O script `main.py` carrega os dados gerados e aplica três algoritmos de ordenação:

### 3.1 Algoritmos Utilizados

- **Bubble Sort** (`bubble_sort.py`);
- **Quick Sort** (`quick_sort.py`);
- **Heap Sort** (`heap_sort.py`).

### 3.2 Processo de Ordenação

1. Os dados são carregados do arquivo JSON;
2. Três cópias dos dados são criadas para manter a imparcialidade;
3. Cada algoritmo de ordenação é aplicado separadamente;
4. Os primeiros 10 elementos ordenados são exibidos para verificação.

## 4. Implementação do Padrão Strategy

O código segue o **Padrão de Projeto Strategy**, permitindo a substituição dinâmica dos algoritmos de ordenação.

### 4.1 Estrutura do Strategy

- **Classe Abstrata `SortStrategy`**: Define um método abstrato `sort(self, data)` que deve ser implementado pelos algoritmos concretos;
- **Classes Concretas**:
  - `BubbleSort` implementa ordenação por bolha;
  - `QuickSort` implementa ordenação rápida;
  - `HeapSort` implementa ordenação por heap.

## 5. Comparação de Algoritmos de Ordenação

### 5.1 Metodologia

Os algoritmos foram avaliados com três conjuntos de dados de tamanhos diferentes:

- 1.000 elementos;
- 5.000 elementos;
- 10.000 elementos.

Os tempos de execução foram medidos utilizando `time.perf_counter()` e representados graficamente.

### 5.2 Resultados Obtidos

- **Bubble Sort** foi o mais lento devido à sua complexidade O(n²);
- **Quick Sort** apresentou o melhor desempenho em média, graças à abordagem de divisão e conquista;
- **Heap Sort** teve um desempenho competitivo, próximo ao Quick Sort.

### 5.3 Discussão

O Quick Sort teve vantagem devido à sua estratégia de divisão e conquista, reduzindo o número de comparações e movimentações. O paradigma **Dividir e Conquistar** se mostrou eficiente para grandes volumes de dados.

## 6. Ferramenta de Logs e Análise dos Resultados

Para melhor compreensão do comportamento dos algoritmos e identificação de possíveis gargalos, foi implementado um sistema de logs utilizando **OpenTelemetry**.

### 6.1 Instrumentação dos Algoritmos

Cada algoritmo foi instrumentado para registrar seus tempos de execução utilizando o [**Jaeger**](https://github.com/jaegertracing/jaeger-client-python), permitindo rastreamento distribuído detalhado das operações.

### 6.2 Ferramentas de Visualização

Os logs são coletados e analisados em ferramentas open-source como:

- **Jaeger**: Para rastreamento distribuído dos tempos de execução;
- **Prometheus + Grafana**: Para métricas e visualização gráfica;
- **Elasticsearch + Kibana**: Para análise detalhada dos logs.

## 7. Conclusão

A análise confirmou que **Quick Sort** foi o mais eficiente na maioria dos casos, seguido pelo **Heap Sort**. O uso de algoritmos com complexidade **O(n log n)** é recomendado para grandes volumes de dados, enquanto algoritmos quadráticos como o **Bubble Sort** se tornam impraticáveis.
