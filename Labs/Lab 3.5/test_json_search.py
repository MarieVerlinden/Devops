# Fill the Python code in this file
import unittest
from recursive_json_search import *
from test_data import *
class json_search_test(unittest.TestCase):
    '''test module to test search function in `recursive_json_search.py`'''
    #Given an existing key in the JSON object, see if the testing code can find such a key.
    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([]!=json_search(key1,data))
    #Given a non-existent key in the JSON object, see if the testing code confirms that no key can be found.
    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([]==json_search(key2,data))
    #Check if our function returns a list, as it should always do
    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(json_search(key1,data),list)
#makign sure that the unittest.main() method runs only if the script is run directly
if __name__ == '__main__':
    unittest.main()