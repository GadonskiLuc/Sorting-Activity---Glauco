# algorithms/sort_strategy.py
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        """Método abstrato para implementação dos algoritmos de ordenação"""
        pass
