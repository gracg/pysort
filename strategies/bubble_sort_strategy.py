from typing import TypeVar
from strategies.abstract_strategy import AbstractStrategy

T = TypeVar('T')
R = TypeVar('R')


class BubbleSortStrategy(AbstractStrategy):

    _strategy_name = "Bubble Sort"

    def sort(self, nums: list[T]):

        while True:
            is_sorted = True
            for i in range(len(nums) - 1):

                x: T = nums[i]
                x_val: R = self._map(x)

                y: T = nums[i+1]
                y_val: R = self._map(y)

                self._read_operations += 2

                if self._predicate(x_val, y_val):
                    nums[i] = y_val
                    nums[i + 1] = x_val
                    is_sorted = False
                    self._write_operations += 2

                self._comparison_operations += 1

            self._comparison_operations += 1
            if is_sorted:
                break

        return nums
