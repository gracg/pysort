from tests.test_strategies.base_strategy_test import BaseStrategyAbstractTest
from strategies.selection_sort_strategy import SelectionSortStrategy

class TestSelectionSortStrategy(BaseStrategyAbstractTest):

    _is_abstract = False

    def get_strategy(self):
        return SelectionSortStrategy