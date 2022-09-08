from tests.test_strategies.base_strategy_test import BaseStrategyAbstractTest
from strategies.quick_sort_strategy import QuickSortStrategy

class TestQuickSortStrategy(BaseStrategyAbstractTest):

    _is_abstract = False

    def get_strategy(self):
        return QuickSortStrategy