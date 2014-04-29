import a1_meli
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1_meli.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_ex1 (self):
        '''Test with a list that contains negative, positive numbers and zero as well'''
        actual = a1_meli.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(actual, expected)
        
    def test_stock_price_summary_ex2 (self):
        '''Test with a list that contains only positive numbers'''
        actual = a1_meli.stock_price_summary([0.01, 0.05, 3, 1, 4.5])
        expected = (8.56, 0) 
        self.assertEqual(actual, expected)

    def test_stock_price_summary_ex3 (self):
        '''Test with a list that contains only negative numbers'''
        actual = a1_meli.stock_price_summary([-0.02, -0.14, -5])
        expected = (0, -5.16)
        self.assertEqual(actual, expected)
        
    def test_stock_price_summary_ex4 (self):
        '''Test with a list that contains only zeros'''
        actual = a1_meli.stock_price_summary([0, 0, 0])
        expected = (0, 0)
        self.assertEqual(actual, expected)
        
    def test_stock_price_summary_ex5 (self):
        '''Test with an empty list'''
        actual = a1_meli.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
