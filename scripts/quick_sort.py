import threading
import time
import logging

from scripts.strategy import SortStrategy

class QuickSort(SortStrategy):
    def __init__(self):
        self.trocas = 0
        self.comparacoes = 0
        self.lock = threading.Lock()

    def sort(self, data):
        self.trocas = 0
        self.comparacoes = 0
        sorted_data = self._quick_sort(data)
        return sorted_data

    def _quick_sort(self, data):
        if len(data) <= 1:
            return data

        pivot = data[len(data) // 2]
        left, middle, right = [], [], []

        for x in data:
            with self.lock:
                self.comparacoes += 1
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                middle.append(x)

        with self.lock:
            self.trocas += len(left) + len(right)

        left_thread = threading.Thread(target=lambda lst: lst.__setitem__(slice(None), self._quick_sort(lst)),
                                       args=(left,))
        right_thread = threading.Thread(target=lambda lst: lst.__setitem__(slice(None), self._quick_sort(lst)),
                                        args=(right,))

        left_thread.start()
        right_thread.start()

        left_thread.join()
        right_thread.join()

        return left + middle + right

    def sort_with_metrics(self, data):
        start = time.time()
        sorted_data = self.sort(data)
        end = time.time()
        runtime = (end - start) * 1000  # Convertendo para ms

        logging.info("Quick Sort with Threading")
        logging.info(f"Runtime: {runtime:.2f} ms")
        logging.info(f"Trocas: {self.trocas}")
        logging.info(f"Comparações: {self.comparacoes} \n")

        return sorted_data