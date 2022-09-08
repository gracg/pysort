from tests.test_strategies.base_strategy_test import BaseStrategyAbstractTest
from strategies.merge_sort_strategy import MergeSortStrategy

class TestMergeSortStrategy(BaseStrategyAbstractTest):

    _is_abstract = False

    def get_strategy(self):
        return MergeSortStrategy