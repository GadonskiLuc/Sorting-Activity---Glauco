# algorithms/heap_sort.py
from .strategy import SortStrategy

import time
import logging

class HeapSort(SortStrategy):
    def heapify(self, data, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] > data[largest]:
            largest = left
        if right < n and data[right] > data[largest]:
            largest = right
        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            self.heapify(data, n, largest)

    def sort(self, data):
        trocas = 0
        comparacoes = 0
        
        start = time.time()

        n = len(data)
        for i in range(n // 2 - 1, -1, -1):
            result = self.heapify(data, n, i)
            self.heapify(data, n, i)

            if result:
                c, t = result
                comparacoes += c
                trocas += t
        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            trocas += 1
            result = self.heapify(data, i, 0)

            if result:
                c, t = result
                comparacoes += c
                trocas += t

        end = time.time()
        runtime = (end - start) * 1000

        logging.info(" Heap Sort")
        logging.info(f" Runtime: {runtime:.2f} ms")
        logging.info(f" Trocas: {trocas}")
        logging.info(f" Comparações: {comparacoes}")

        return data
