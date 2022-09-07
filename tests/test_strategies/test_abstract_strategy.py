from strategies.bubble_sort_strategy import BubbleSortStrategy
import unittest
import predicates


class TestAbstractStrategy(unittest.TestCase):
    _child_class_func = BubbleSortStrategy

    _valid_map = lambda x: x
    _valid_predicate = predicates.intAsc

    def test_abstract_constructor(self):
        predicate = predicates.intAsc
        map_func = lambda x: x
        strategy = self._child_class_func(map_func, predicate)

    def test_abstract_constructor_params_are_none(self):
        wrong_map_param = None
        wrong_predicate_param = None
        self.assertRaises(TypeError, lambda: self._child_class_func(wrong_map_param, wrong_predicate_param))

    def test_abstract_constructor_params_are_not_funcs(self):
        wrong_map_param = 1
        wrong_predicate_param = 1
        self.assertRaises(TypeError, lambda: self._child_class_func(wrong_map_param, wrong_predicate_param))

    def test_clear_statistics(self):
        strategy = self._child_class_func(self._valid_map, self._valid_predicate)

        reads = strategy._read_operations = 100
        writes = strategy._write_operations = 100
        comparisons = strategy._comparison_operations = 100

        strategy.clear_statistics()

        self.assertTrue(reads, 0)
        self.assertTrue(writes, 0)
        self.assertTrue(comparisons, 0)

    def test_get_result(self):
        strategy = self._child_class_func(self._valid_map, self._valid_predicate)

        strategy._read_operations = 100
        strategy._write_operations = 100
        strategy._comparison_operations = 100

        result = strategy.get_result(10)

        self.assertTrue(result.read_operations == 100)
        self.assertTrue(result.write_operations == 100)
        self.assertTrue(result.comparison_operations == 100)
        self.assertTrue(result.size==10)
