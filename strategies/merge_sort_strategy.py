from strategies.abstract_strategy import AbstractStrategy

from typing import TypeVar

T = TypeVar('T')
R = TypeVar('R')


class MergeSortStrategy(AbstractStrategy):

    _strategy_name = "Merge Sort"

    def sort(self, nums: list[T]):

        self._check_list_or_raise(nums)

        nums_copy = nums[:]
        return self._sort_recursive(nums_copy)

    def _sort_recursive(self, nums: list[T]) -> list[T]:

        if len(nums) <= 1:
            self._comparison_operations += 1
            return nums

        if len(nums) == 2:
            obj1 = nums[0]
            val1 = self._map(obj1)

            obj2 = nums[1]
            val2 = self._map(obj2)

            self._read_operations += 2
            self._comparison_operations += 1

            if not self._predicate(val1, val2):
                nums[0] = obj1
                nums[1] = obj2
            else:
                nums[0] = obj2
                nums[1] = obj1

            self._comparison_operations += 1
            self._write_operations += 2
            return nums

        self._comparison_operations += 2

        middle_index = int(len(nums) / 2)

        left_list = nums[0:middle_index]
        right_list = nums[middle_index:len(nums)]

        self._write_operations += 2

        left_list = self._sort_recursive(left_list)
        right_list = self._sort_recursive(right_list)

        i = 0
        j = 0
        i_max = len(left_list) - 1
        j_max = len(right_list) - 1

        new_list = []

        while i <= i_max and j <= j_max:

            obj1 = left_list[i]
            val1 = self._map(obj1)

            obj2 = right_list[j]
            val2 = self._map(obj2)

            self._read_operations += 2
            self._comparison_operations += 1

            if not self._predicate(val1, val2):
                new_list.append(obj1)
                i += 1
            else:
                new_list.append(obj2)
                j += 1

            self._comparison_operations += 1

        remaining_list = None
        remaining_index = None

        if i <= i_max:
            remaining_list = left_list
            remaining_index = i
            self._comparison_operations += 1

        if j <= j_max:
            remaining_list = right_list
            remaining_index = j
            self._comparison_operations += 1

        if remaining_list is not None:

            for k in range(remaining_index, len(remaining_list), 1):
                new_list.append(remaining_list[k])
                self._read_operations += 1
                self._write_operations += 1

        self._comparison_operations += 1

        return new_list
