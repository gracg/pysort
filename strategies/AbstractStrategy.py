from abc import ABC, abstractmethod
from typing import TypeVar, Callable

T = TypeVar('T')
R = TypeVar('R')

class AbstractStrategy(ABC):

    @abstractmethod
    def sort(self,nums:list[T]):
        pass


    def __init__(self, mapFunc: Callable[[T], R],biPredicateFunc: Callable[[R,R],bool]):

        if(mapFunc==None):
            raise TypeError("mapping function can't be null")

        if(biPredicateFunc is None):
            raise TypeError("predicate functions can't be null")

        self._mapFunc = mapFunc
        self._predicate = biPredicateFunc

        self._read_operations = 0
        self._write_operations = 0
        self._comparison_operations = 0


    def clearStatistics(self):
        self._read_operations = 0
        self._write_operations = 0
        self._comparison_operations = 0