import unittest
from groupby_index import *

class Test(unittest.TestCase):
    def test_padding_array(self):
        self.assertEqual([*map(lambda x:[*x],groupby_index([1,2,3,4],2))],[[1,2],[3,4]])

if __name__ == '__main__':
    unittest.main()