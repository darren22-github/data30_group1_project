import unittest

from pandas import read_csv
import transformation
import csv

test_rows = ['6','Joel Melmoth','Male','04/02/1994','jmelmoth5@dedecms.com','Manchester','2 Esker Center','M14','+44 860 146 8614','Napier University','02:01','','',]

class TestDataCleaner(unittest.TestCase):

    def setUp(self):
        self.dc = transformation.DataCleaner()

    def test_check_if_empty(self):
        print('Testing check_if_empty method')
        self.assertEqual(self.dc.check_if_empty(""), True)
        self.assertEqual(self.dc.check_if_empty("hello"), False)

    def test_empty_to_null(self):
        print('Testing empty_to_null method')
        self.assertEqual(self.dc.empty_to_null(""), "null")

if __name__ == '__main__':
    unittest.main()
