import unittest

from tests.test_strategies.base_strategy_test import BaseStrategyAbstractTest
from strategies.bubble_sort_strategy import BubbleSortStrategy
import predicates


class TestBubbleSortStrategy(BaseStrategyAbstractTest):

    _is_abstract = False

    def get_strategy(self):
        return BubbleSortStrategy
