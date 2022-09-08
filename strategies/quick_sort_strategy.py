from typing import TypeVar

from strategies.abstract_strategy import AbstractStrategy

T = TypeVar('T')
R = TypeVar('R')


class QuickSortStrategy(AbstractStrategy):

    _strategy_name = "Quick Sort"

    def sort(self, nums: list[T]):

        self._check_list_or_raise(nums)
        nums_copy = nums[:]
        return self._sort(nums_copy)

    def _sort(self, nums: list[T]):

        if len(nums) <= 1:
            self._comparison_operations += 1
            return nums

        if len(nums) == 2:

            obj1 = nums[0]
            val1 = self._map(obj1)

            obj2 = nums[1]
            val2 = self._map(obj2)

            if self._predicate(val1, val2):
                nums[0] = obj2
                nums[1] = obj1
            else:
                nums[0] = obj1
                nums[1] = obj2

            self._read_operations += 2
            self._write_operations += 2
            self._comparison_operations += 1
            return nums

        self._comparison_operations += 2

        pivot_obj = nums[0]
        pivot_value = self._map(pivot_obj)
        self._read_operations += 1


        left_of_pivot = []
        right_of_pivot = []
        copies_of_pivot = -1

        for i, i_val in enumerate(nums):

            obj = i_val
            val = self._map(obj)

            if self._predicate(pivot_value, val):
                left_of_pivot.append(obj)

            if self._predicate(val, pivot_value):
                right_of_pivot.append(obj)

            if pivot_value == val:
                copies_of_pivot += 1

            self._comparison_operations += 3
            self._read_operations += 1
            self._write_operations += 1

        for i in range(1,copies_of_pivot+1):
            right_of_pivot.append(pivot_obj)
            self._comparison_operations += 1

        left_of_pivot = self._sort(left_of_pivot)
        right_of_pivot = self._sort(right_of_pivot)

        new_list = []
        new_list.extend(left_of_pivot)
        self._write_operations += len(left_of_pivot)
        new_list.append(pivot_obj)
        self._write_operations += 1
        new_list.extend(right_of_pivot)
        self._write_operations += len(right_of_pivot)

        return new_list

