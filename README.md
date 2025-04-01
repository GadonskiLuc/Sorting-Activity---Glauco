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
- 10.000 elementos.

Os tempos de execução foram medidos utilizando `time.time()` e representados graficamente.

### 5.2 Resultados Obtidos

- **Bubble Sort** foi o mais lento devido à sua complexidade O(n²);
- **Quick Sort** apresentou o melhor desempenho em média, graças à abordagem de divisão e conquista;
- **Heap Sort** teve um desempenho competitivo, próximo ao Quick Sort.

### 5.3 Discussão

O Quick Sort teve vantagem devido à sua estratégia de divisão e conquista, reduzindo o número de comparações e movimentações. O paradigma **Dividir e Conquistar** se mostrou eficiente para grandes volumes de dados.

## 6. Ferramenta de Logs e Análise dos Resultados

Para melhor compreensão do comportamento dos algoritmos e identificação de possíveis gargalos, foi implementado um sistema de logs utilizando **OpenTelemetry**.

### 6.1 Instrumentação dos Algoritmos

Cada algoritmo foi instrumentado para registrar tempos de execução e métricas detalhadas sobre seu desempenho, utilizando o [**Jaeger**](https://github.com/jaegertracing/jaeger-client-python). Isso permite o rastreamento distribuído e a coleta de dados essenciais para a avaliação dos KPIs de desempenho, como tempo de execução, número de comparações realizadas e uso de recursos. A instrumentação também oferece uma visão aprofundada de como cada algoritmo se comporta, destacando aspectos como a quantidade de comparações feitas, a eficiência em cada operação e as variações de desempenho entre diferentes execuções.

### 6.2 Ferramentas de Visualização

Os logs gerados durante a execução dos algoritmos são coletados e analisados em ferramentas open-source, permitindo o monitoramento e a visualização detalhada dos KPIs de desempenho, como:

- **Jaeger**: Para rastreamento distribuído e visualização dos tempos de execução de cada operação, facilitando a análise do tempo gasto por cada algoritmo em cada etapa;
- **Prometheus + Grafana**: Para coleta de métricas como tempo de execução, número de comparações e utilização de recursos, apresentando gráficos que permitem comparar o comportamento de diferentes algoritmos e identificar gargalos;
- **Elasticsearch + Kibana**: Para análise detalhada dos logs, possibilitando a consulta e visualização dos dados de execução, o que ajuda a identificar padrões de comportamento, otimizações potenciais e diferenças de desempenho entre os algoritmos.

## 7. Conclusão

A análise confirmou que **Quick Sort** foi o mais eficiente na maioria dos casos, seguido pelo **Heap Sort**. O uso de algoritmos com complexidade **O(n log n)** é recomendado para grandes volumes de dados, enquanto algoritmos quadráticos como o **Bubble Sort** se tornam impraticáveis.

# Documentação do HeapSort com Threading

## 1. Introdução

Esta documentação descreve as alterações feitas no algoritmo HeapSort para implementar a paralelização usando a biblioteca `threading` em Python. A implementação tem como objetivo demonstrar como a paralelização pode ser aplicada para otimizar a construção do heap no algoritmo.

## 2. Modificações no Código

### Classe `HeapSort` com Threading

- **`self.lock` para Threadsafety**: Introduzimos um objeto de bloqueio (`threading.Lock`) para assegurar que modificações nas variáveis compartilhadas (`trocas` e `comparacoes`) sejam feitas de maneira segura, evitando race conditions durante a execução de múltiplas threads.

- **Método `heapify`**:
  - Adaptação para o uso de `lock` ao acessar e modificar `trocas` e `comparacoes`.
  - Mantém a lógica principal do HeapSort, que é reorganizar o array em um heap.

- **Paralelização com `threading`**:
  - Criação de threads para chamar o método `heapify` durante a fase de construção do heap. Cada subárvore principal é processada em uma thread separada.
  - Uso do método `join()` para garantir que o processo principal aguarde a conclusão de todas as threads.

### Desempenho

- **Fase de Construção do Heap**: Utiliza threads para otimizar a fase de construção inicial do heap, onde cada subárvore pode ser processada simultaneamente.
- **Fase de Saída (Heap Sort Sequence)**: Permanece sequencial devido à necessidade de acesso ordenado e em sequência ao heap construído.

## 3. Comparação de Desempenho

Foram realizadas comparações de desempenho entre as versões sequencial e paralelizada do HeapSort para avaliar o impacto da paralelização.

### Metodologia

- Ambos os algoritmos foram executados em datasets de diferentes tamanhos sob as mesmas condições de hardware e software.
- O tempo de execução (em milissegundos), número de trocas e comparações foram registrados.

### Resultados Esperados

- **Versão Sequencial**: Fornece um baseline de desempenho sem overhead de criação e gerenciamento de threads.
  
- **Versão Paralelizada**:
  - **Vantagens**: Potencialmente reduzido o tempo de construção do heap em casos onde as árvores são grandes o suficiente para justificar o overhead de criação de threads.
  - **Desvantagens**: O `threading` em Python, devido ao Global Interpreter Lock (GIL), pode não apresentar vantagens de desempenho significativas para tarefas CPU-bounded.

### Observações

- Para tamanhos menores de arrays, o overhead de gerenciamento de threads pode superar os ganhos, tornando a versão sequencial mais rápida em prática.

## 4. Considerações Finais

A implementação de `threading` no HeapSort demonstra uma abordagem fundamental para a paralelização, especialmente em um ambiente educacional ou de desenvolvimento. Os usuários devem considerar o contexto específico de uso e os trade-offs entre desempenho e complexidade na escolha da implementação de paralelização mais apropriada para suas necessidades.