# main.py
import json
from scripts.bubble_sort import BubbleSort
from scripts.quick_sort import QuickSort
from scripts.heap_sort import HeapSort

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
sorted_quick = quick_sort.sort(data2)
sorted_heap = heap_sort.sort(data3)

# Exibir os resultados (apenas os primeiros 10 valores para visualização)
print("Bubble Sort:", sorted_bubble[:10])
print("Quick Sort:", sorted_quick[:10])
print("Heap Sort:", sorted_heap[:10])
