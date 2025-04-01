import threading
import time
import logging

from scripts.strategy import SortStrategy


class BubbleSort(SortStrategy):
    def sort(self, data):
        def bubble_sort_part(data, start, end):
            trocas = 0
            comparacoes = 0
            logging.info(f"Thread {threading.current_thread().name} sorting from {start} to {end-1}")
            for i in range(start, end):
                for j in range(0, len(data) - 1):
                    comparacoes += 1
                    if data[j] > data[j + 1]:
                        trocas += 1
                        data[j], data[j + 1] = data[j + 1], data[j]  # Troca os elementos
            return trocas, comparacoes

        start = time.time()

        n = len(data)
        num_threads = 2  # Escolha um número de threads
        slice_length = n // num_threads
        threads = []
        results = []

        for i in range(num_threads):
            start_index = i * slice_length
            end_index = (i + 1) * slice_length if i < num_threads - 1 else n
            thread = threading.Thread(target=lambda s, e: results.append(bubble_sort_part(data, s, e)), args=(start_index, end_index))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        end = time.time()
        runtime = (end - start) * 1000

        logging.info("Bubble Sort with Threading")
        logging.info(f"Runtime: {runtime:.2f} ms")
        logging.info(f"Trocas: {sum(result[0] for result in results)}")
        logging.info(f"Comparações: {sum(result[1] for result in results)}\n")

        return data