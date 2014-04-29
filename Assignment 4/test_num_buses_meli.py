import a1_meli
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1_meli.num_buses. """

    # Add your test methods for a1.num_buses here.

    def test_num_buses_ex1 (self):
        ''' Test for one full bus and an other one that is not full. '''
        actual = a1_meli.num_buses(75)
        expected = 2
        self.assertEqual(actual, expected)

    def test_num_buses_ex2 (self):
        ''' Test num_buses for 0 people, that requires no buses. '''
        actual = a1_meli.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_num_buses_ex3 (self):
        ''' Test num_buses for 1 people, that requires 1 bus. '''
        actual = a1_meli.num_buses(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_ex4 (self):
        ''' Test num_buses for 50 people, that makes 1 full bus. '''
        actual = a1_meli.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_ex5 (self):
        ''' Test num_buses for one full bus and one more person. '''
        actual = a1_meli.num_buses(51)
        expected = 2
        self.assertEqual(actual, expected)

    def test_num_buses_ex6 (self):
        ''' Test num_buses for 110 people, that requires 3 buses. '''
        actual = a1_meli.num_buses(110)
        expected = 3
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
