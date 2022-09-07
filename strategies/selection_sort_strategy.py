from typing import TypeVar
from strategies.abstract_strategy import AbstractStrategy

T = TypeVar('T')


class SelectionSortStrategy(AbstractStrategy):

    _strategy_name = "Selection Sort"

    def sort(self, nums: list[T]):

        self._check_list_or_raise(nums)
        if len(nums) <= 1:
            return nums

        for i, _ in enumerate(nums):

            current_obj = nums[i]
            self._read_operations += 1

            lowest_or_highest_obj = current_obj
            lowest_or_highest_index = i

            for j, _ in enumerate(range(i + 1, len(nums) + 1), start=i):
                obj = nums[j]
                obj_val = self._map(obj)
                self._read_operations += 1

                lowest_or_highest_val = self._map(lowest_or_highest_obj)
                if self._predicate(lowest_or_highest_val, obj_val):
                    lowest_or_highest_obj = obj
                    lowest_or_highest_index = j

                self._comparison_operations += 1

            nums[i] = lowest_or_highest_obj
            nums[lowest_or_highest_index] = current_obj
            self._write_operations += 2

        return nums
