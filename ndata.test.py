import unittest
from ndata import *
import io

class Testing(unittest.TestCase):
    def testcase(self):
        text = """id\tdocument\tlabel
20\t사랑해요\t1"""
        textfile = io.StringIO(text)
        datas = readNsmcRawData(textfile)
        i = datas[0]
        self.assertEqual(i.id,20)
        self.assertEqual(i.document,"사랑해요")
        self.assertEqual(i.label,1)

if __name__ == "__main__":
    unittest.main()