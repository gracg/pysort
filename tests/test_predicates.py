import unittest
import predicates

class TestPredicates(unittest.TestCase):

    def test_int_asc_none_params(self):
        self.assertRaises(TypeError,lambda: predicates.intAsc(2,None))
        self.assertRaises(TypeError,lambda: predicates.intAsc(None,1))

    def test_int_asc_wrong_params_type(self):
        self.assertRaises(TypeError,lambda: predicates.intAsc(2,''))
        self.assertRaises(TypeError,lambda: predicates.intAsc('',1))

    def test_int_asc(self):
        self.assertTrue(predicates.intAsc(2,1))

    def test_int_desc_asc_none_params(self):
        self.assertRaises(TypeError,lambda: predicates.intDes(1,None))
        self.assertRaises(TypeError,lambda: predicates.intDes(None,2))

    def test_int_desc_wrong_params_type(self):
        self.assertRaises(TypeError,lambda: predicates.intDes(1,''))
        self.assertRaises(TypeError,lambda: predicates.intDes('',2))

    def test_int_desc(self):
        self.assertTrue(predicates.intDes(1,2))

    def test_words_asc_none_params(self):
        self.assertRaises(TypeError,lambda: predicates.strAsc('a',None))
        self.assertRaises(TypeError,lambda: predicates.strAsc(None,'b'))

    def test_words_asc_wrong_params_type(self):
        self.assertRaises(TypeError,lambda: predicates.strAsc(1,''))
        self.assertRaises(TypeError,lambda: predicates.strAsc('',2))

    def test_str_asc(self):
        self.assertTrue(predicates.strAsc('b','a'))

    def test_words_desc_none_params(self):
        self.assertRaises(TypeError,lambda: predicates.strDes('a',None))
        self.assertRaises(TypeError,lambda: predicates.strDes(None,'b'))

    def test_words_desc_wrong_params_type(self):
        self.assertRaises(TypeError,lambda: predicates.strDes(1,''))
        self.assertRaises(TypeError,lambda: predicates.strDes('',2))

    def test_str_desc(self):
        self.assertTrue(predicates.strDes('a','b'))
