import unittest
import abc
from strategies.bubble_sort_strategy import BubbleSortStrategy
from attr.validators import disabled

import predicates


class BaseStrategyAbstractTest(abc.ABC, unittest.TestCase):


    # Abstract class is created when testing. thus this abstract check
    _is_abstract = True

    def simple_map(self,x):
        return x

    def test_sort_none(self):
        if not self._is_abstract:
            strategy = self.get_strategy()(self.simple_map,predicates.intAsc)
            length = len(strategy.sort([]))
            self.assertRaises(ValueError,lambda: strategy.sort(None))

    def test_sort_one_element(self):
        if not self._is_abstract:
            stategy = self.get_strategy()(self.simple_map,predicates.intAsc)
            length = len(stategy.sort([1]))
            self.assertTrue(length==1)

    def test_sort_two_elements_asc(self):
        if not self._is_abstract:
            strategy = self.get_strategy()(self.simple_map,predicates.intAsc)
            l = [2,1]
            strategy.sort(l)

            self.assertTrue(l[0]==1)
            self.assertTrue(l[1]==2)

    def test_sort_two_elements_asc(self):
        if not self._is_abstract:
            strategy = self.get_strategy()(self.simple_map,predicates.intDes)
            l = [1,2]
            strategy.sort(l)

            self.assertTrue(l[0]==2)
            self.assertTrue(l[1]==1)

    # supposed to be an abstract method
    # the child classes are supposed to implement this
    def get_strategy(self):
        raise NotImplemented()


