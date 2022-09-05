import os.path

import generators
import unittest


class TestGenerator(unittest.TestCase):
    _words_file_path = os.path.join("..", "words.txt")

    def test_ints_not_none(self):
        l = generators.ints(0, 0, 0)
        self.assertIsNotNone(l)

    def test_ints_none_paramaters(self):
        self.assertRaises(TypeError,lambda: generators.ints(None,1,1))
        self.assertRaises(TypeError,lambda: generators.ints(1,None,1))
        self.assertRaises(TypeError,lambda: generators.ints(1,1,None))

    def test_ints_wrong_parameter_type(self):
        self.assertRaises(TypeError,lambda: generators.ints('',1,1))
        self.assertRaises(TypeError,lambda: generators.ints(1,'',1))
        self.assertRaises(TypeError,lambda: generators.ints(1,1,''))

    def test_ints_length(self):
        l = generators.ints(0, 10, 10)
        self.assertTrue(len(l), 10)

    def test_ints_length_negative(self):
        l = generators.ints(0,10,-1)
        self.assertTrue(len(l)==0)

    def test_ints_length_zero(self):
        l = generators.ints(0,10,0)
        self.assertTrue(len(l)==0)

    def test_ints_min(self):
        l = generators.ints(5, 6, 100)
        min_val = list(filter(lambda x: x < 5, l))
        self.assertTrue(len(min_val) == 0)

    def test_ints_max(self):
        l = generators.ints(5, 6, 100)
        min_val = list(filter(lambda x: x > 6, l))
        self.assertTrue(len(min_val) == 0)

    def test_words_test_path_not_a_string(self):
        self.assertRaises(TypeError,generators.words(0,testPath=12))

    def test_words_file_found(self):
        generators.words(1, testPath=self._words_file_path)

    def test_words_none_length(self):
        self.assertRaises(TypeError,lambda: generators.words(None,testPath=self._words_file_path))

    def test_words_length_not_a_number(self):
        self.assertRaises(TypeError,lambda: generators.words('zero',testPath=self._words_file_path))

    def test_words_not_none(self):
        l = generators.words(0, testPath=self._words_file_path)
        self.assertIsNotNone(l)

    def test_words_length(self):
        l = generators.words(10, testPath=self._words_file_path)
        self.assertTrue(len(l), 10)

    def test_words_length_negative(self):
        l = generators.words(-1,testPath=self._words_file_path)
        print(len(l))
        self.assertTrue(len(l)==0)

    def test_words_length_zero(self):
        l = generators.words(0,testPath=self._words_file_path)
        self.assertTrue(len(l)==0)
