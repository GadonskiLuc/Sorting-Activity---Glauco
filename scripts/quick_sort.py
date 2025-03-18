# algorithms/quick_sort.py
from .strategy import SortStrategy

import time
class QuickSort(SortStrategy):
    def sort(self, data):
        trocas = 0
        comparacoes = 0

        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]

        # print("\Quick Sort")
        # print(f"Runtime: {runtime:.2f} ms")
        # print(f"Trocas: {trocas}")
        # print(f"Comparações: {comparacoes}")

        return self.sort(left) + middle + self.sort(right)
