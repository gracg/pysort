from abc import ABC

from strategies.abstract_strategy import AbstractStrategy
from typing import TypeVar

T = TypeVar('T')
R = TypeVar('R')


class InsertionSortStrategy(AbstractStrategy):

    _strategy_name = "Insertion Sort"

    def sort(self, nums: list[T]):

        for i in range(1,len(nums)):

            current_obj: T = nums[i]
            current_val: R = self._map(current_obj)

            previous_obj: T = nums[i-1]
            previous_val: R = self._map(previous_obj)

            self._read_operations += 2

            if self._predicate(previous_val,current_val):

                for j in range(i-1,-1,-1):

                    other_obj = nums[j]
                    other_val = self._map(other_obj)
                    self._read_operations += 1

                    if not self._predicate(other_val,current_val):
                        del nums[i]
                        nums.insert(j+1,current_obj)
                        self._write_operations += 2
                        break

                    if j==0:
                        nums.insert(0,current_obj)
                        del nums[i+1]
                        self._write_operations += 2
                        break

                    self._comparison_operations += 2

            self._comparison_operations += 2

        return nums

