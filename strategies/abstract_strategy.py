from abc import ABC, abstractmethod
from typing import TypeVar, Callable
from models.run_result import RunResult

T = TypeVar('T')
R = TypeVar('R')


class AbstractStrategy(ABC):
    _strategy_name = "Abstract"

    @abstractmethod
    def sort(self, nums: list[T]):
        pass

    def __init__(self, mapFunc: Callable[[T], R], biPredicateFunc: Callable[[R, R], bool]):

        if (mapFunc == None):
            raise TypeError("mapping function can't be null")

        if (biPredicateFunc is None):
            raise TypeError("predicate functions can't be null")

        if not callable(mapFunc):
            raise TypeError("mapFunc must be a function")

        if not callable(biPredicateFunc):
            raise TypeError("biPredicateFunc must be a function")

        self._map = mapFunc
        self._predicate = biPredicateFunc

        self._read_operations = 0
        self._write_operations = 0
        self._comparison_operations = 0

    def clear_statistics(self):
        self._read_operations = 0
        self._write_operations = 0
        self._comparison_operations = 0

    def get_result(self, size=0):
        return RunResult(self._strategy_name, size, self._read_operations, self._write_operations,
                         self._comparison_operations)

    def _check_list_or_raise(self,nums: list):
        if nums is None:
            raise ValueError("List cannot be None to sort")