# main.py
import json
import logging
import time

from scripts.bubble_sort import BubbleSort
from scripts.quick_sort import QuickSort
from scripts.heap_sort import HeapSort
logging.basicConfig(level=logging.DEBUG)

def getRuntime(name, data, func): # TODO: Extrar para uma classe externa
    start = time.time()

    data = func(data)

    end = time.time()
    tempo_execucao = (end - start) * 1000

    logging.info(f"Algoritmo: {name}, Tempo de execucao:{tempo_execucao:.2f}")
    return data

# Carregar os dados do arquivo JSON(mude o nome do arquivo que sera analisado)
with open("./data/dados_1000.json", "r") as file:
    numbers = json.load(file)

bubble_sort = BubbleSort()
quick_sort = QuickSort()
heap_sort = HeapSort()

data1 = numbers.copy()
data2 = numbers.copy()
data3 = numbers.copy()

# Aplicar os algoritmos
sorted_bubble = bubble_sort.sort(data1)
sorted_quick = getRuntime("Quick Sort", data2, quick_sort.sort)
sorted_heap = getRuntime("Heap", data3, heap_sort.sort)

# Exibir os resultados (apenas os primeiros 10 valores para visualização)
print("\nBubble Sort:", sorted_bubble[:10])
print("Quick Sort:", sorted_quick[:10])
print("Heap Sort:", sorted_heap[:10])
