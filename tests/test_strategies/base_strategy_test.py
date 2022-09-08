import unittest
import abc
import predicates
import generators
from exeptions.not_sorted_exception import NotSortedException


class BaseStrategyAbstractTest(abc.ABC, unittest.TestCase):
    # Abstract class is created when testing, thus this abstract check
    _is_abstract = True

    def simple_map(self, x):
        return x

    def test_sort_none(self):
        if not self._is_abstract:
            strategy = self.get_strategy()(self.simple_map, predicates.intAsc)
            length = len(strategy.sort([]))
            self.assertRaises(ValueError, lambda: strategy.sort(None))

    def test_sort_one_element(self):
        if not self._is_abstract:
            stategy = self.get_strategy()(self.simple_map, predicates.intAsc)
            length = len(stategy.sort([1]))
            self.assertTrue(length == 1)

    def test_sort_random_elements_asc(self):

        if not self._is_abstract:
            nums = generators.ints(1, 100, 10)

            strategy = self.get_strategy()(self.simple_map, predicates.intAsc)
            l = strategy.sort(nums)

            self.__check_int_sort_asc(nums, l)

    def __check_int_sort_asc(self, original_list, check_list):

        if len(check_list) <= 1:
            return

        for i in range(1, len(check_list), 1):
            x = check_list[i - 1]
            y = check_list[i]

            if (x > y):
                is_sorted = False
                raise NotSortedException(original_list, check_list)

    def test_sort_two_elements_asc(self):
        if not self._is_abstract:
            strategy = self.get_strategy()(self.simple_map, predicates.intAsc)
            l = [2, 1]
            l = strategy.sort(l)

            self.assertTrue(l[0] == 1)
            self.assertTrue(l[1] == 2)

    def test_sort_two_elements_asc(self):
        if not self._is_abstract:
            strategy = self.get_strategy()(self.simple_map, predicates.intDes)
            l = [1, 2]
            l = strategy.sort(l)

            self.assertTrue(l[0] == 2)
            self.assertTrue(l[1] == 1)

    # supposed to be an abstract method
    # the child classes are supposed to implement this
    def get_strategy(self):
        raise NotImplemented()
