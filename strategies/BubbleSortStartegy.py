from typing import TypeVar

from strategies.AbstractStrategy import AbstractStrategy

T = TypeVar('T')
R = TypeVar('R')


class BubbleSortStrategy(AbstractStrategy):

    def sort(self,nums: list[T]):

        while True:
            is_sorted = True
            for i in range(len(nums)-1):

                x = self._mapFunc(nums[i])
                y = self._mapFunc(nums[i+1])

                self._read_operations += 2

                if self._predicate(x,y):

                    nums[i] = y
                    nums[i+1] = x
                    is_sorted = False
                    self._write_operations += 2

                self._comparison_operations += 1

            self._comparison_operations += 1
            if is_sorted:
                break


        return nums