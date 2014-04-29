import a1_meli
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1_meli.swap_k here.
    def test_swap_k_ex1 (self):
        '''If list contains even number of items. '''
        nums = [1, 2, 3, 4, 5, 6]
        a1_meli.swap_k(nums, 2)
        expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(nums, expected)

    def test_swap_k_ex2 (self):
        '''If list contains odd number of items. '''
        nums = [1, 'tak', 3, 'gg', 4, 'b', 6]
        a1_meli.swap_k(nums, 3)
        expected = [4, 'b', 6, 'gg', 1, 'tak', 3]
        self.assertEqual(nums, expected)

    def test_swap_k_ex3 (self):
        '''If list is empty '''
        nums = []
        a1_meli.swap_k(nums, 0)
        expected = []
        self.assertEqual(nums, expected)

    def test_swap_k_ex4 (self):
        '''If list contains 2 items '''
        nums = [1, 'got']
        a1_meli.swap_k(nums, 1)
        expected = ['got', 1]
        self.assertEqual(nums, expected)
        


if __name__ == '__main__':
    unittest.main(exit=False)
