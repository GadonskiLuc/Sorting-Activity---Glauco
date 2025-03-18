# algorithms/bubble_sort.py
from .strategy import SortStrategy

import time
import logging
class BubbleSort(SortStrategy):
    def sort(self, data):
        trocas = 0
        comparacoes = 0
        start = time.time()

        n = len(data)
        for i in range(n):
            comparacoes += 1

            for j in range(0, n - i - 1):
                comparacoes += 1

                if data[j] > data[j + 1]:
                    trocas += 1
                    data[j], data[j + 1] = data[j + 1], data[j]  # Troca os elementos

        end = time.time()
        runtime = (end - start) * 1000

        logging.info(" Bubble Sort")
        logging.info(f" Runtime: {runtime:.2f} ms")
        logging.info(f" Trocas: {trocas}")
        logging.info(f" Comparações: {comparacoes} \n")

        return data
