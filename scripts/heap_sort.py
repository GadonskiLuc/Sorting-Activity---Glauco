import threading
import time
import logging

from scripts.strategy import SortStrategy


class HeapSort(SortStrategy):
    def __init__(self):
        self.trocas = 0
        self.comparacoes = 0
        self.lock = threading.Lock()

    def heapify(self, data, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        with self.lock:
            if left < n and data[left] > data[largest]:
                self.comparacoes += 1
                largest = left
            if right < n and data[right] > data[largest]:
                self.comparacoes += 1
                largest = right

        if largest != i:
            with self.lock:
                self.trocas += 1
            data[i], data[largest] = data[largest], data[i]
            self.heapify(data, n, largest)

    def sort(self, data):
        self.trocas = 0
        self.comparacoes = 0
        start = time.time()

        n = len(data)

        # Create threads for heap construction
        threads = []
        for i in range(n // 2 - 1, -1, -1):
            thread = threading.Thread(target=self.heapify, args=(data, n, i))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            self.trocas += 1
            self.heapify(data, i, 0)

        end = time.time()
        runtime = (end - start) * 1000

        logging.info("Heap Sort with Threading")
        logging.info(f"Runtime: {runtime:.2f} ms")
        logging.info(f"Trocas: {self.trocas}")
        logging.info(f"Comparações: {self.comparacoes}")

        return data