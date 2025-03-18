# algorithms/quick_sort.py
from .strategy import SortStrategy

import time
import logging
class QuickSort:
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
            self.comparacoes += 1
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                middle.append(x)
                
        self.trocas += len(left) + len(right) 
        
        return self._quick_sort(left) + middle + self._quick_sort(right)
    
    def sort_with_metrics(self, data):
        start = time.time()
        sorted_data = self.sort(data)
        end = time.time()
        runtime = (end - start) * 1000  # Convertendo para ms
        
        logging.info(" Quick Sort")
        logging.info(f" Runtime: {runtime:.2f} ms")
        logging.info(f" Trocas: {self.trocas}")
        logging.info(f" Comparações: {self.comparacoes} \n")
        
        return sorted_data
