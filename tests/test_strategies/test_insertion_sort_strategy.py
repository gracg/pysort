from tests.test_strategies.base_strategy_test import BaseStrategyAbstractTest
from strategies.insertion_sort_strategy import InsertionSortStrategy

class TestInsertionSortStrategy(BaseStrategyAbstractTest):

    _is_abstract = False

    def get_strategy(self):
        return InsertionSortStrategy