import unittest

from swap import swap

class SwapTestCase(unittest.TestCase):
    """
    Test functionality of swap ordering
    """
    def test_input_is_instance_of_a_list(self):
        #self.assertIsInstance(object, list)
        pass

    def test_empty_list_fails(self):
        self.assertEqual(swap([]), 'list is empty')

    def test_reverse_works(self):
        self.assertEqual(swap([1,3,7]), [7,3,1])

    def test_upper_case_works(self):
        self.assertEqual(swap(['julius', 'tsofa', 'nyule']), ['JULIUS', 'TSOFA', 'NYULE'])

    def test_if_items_not_either_string_or_integer_works(self):
        self.assertEqual(swap(['nyule', 3]), ['nyule', 3])

if __name__=='__main__':
    unittest.main()
