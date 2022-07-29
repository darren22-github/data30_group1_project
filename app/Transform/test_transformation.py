import unittest

from pandas import read_csv
import transformation
import csv

test_row = ['6','Joel Melmoth','Male','04/02/1994','jmelmoth5@dedecms.com','Manchester','2 Esker Center','M14','+44 860 146 8614','Napier University','02:01','','',]

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

    def test_find_column_number(self):
        print('Testing find_column_number method')
        self.assertEqual(self.dc.find_column_number(test_row, 'Male'), 2)

    def test_clean_name(self):
        print('Testing clean_name method')
        self.assertEqual(self.dc.clean_name("JoHN dOE"), "John Doe")

    def test_clean_phone_number(self):
        print('Testing clean_phone_number method')
        self.assertEqual(self.dc.clean_phone_number("+44 860 146 8614"), "08601468614")

    def test_clean_invite_day(self):
        print('Testing clean_invite_day method')
        self.assertEqual(self.dc.clean_invite_day("3"), "03")

    def test_call_cleaning_function(self):
        print('Testing call_cleaning_function method')
        self.assertEqual(self.dc.call_cleaning_function(8, "+44 860-146 8614"), "08601468614")

    def test_clean_invite_day(self):
        print('Testing clean_invite_day method')
        self.assertEqual(self.dc.clean_invite_day("8"), "08")

    def test_clean_invite_month(self):
        print('Testing clean_invite_month method')
        self.assertEqual(self.dc.clean_invite_month("Apr-19"), "04-19")

    def test_merge_invite_date(self):
        print('Testing merge_invite_date method')
        self.assertEqual(self.dc.merge_invite_date("12", "05-23"), '12-05-23')

    def test_clean_dob(self):
        print('Testing clean_dob method')
        self.assertEqual(self.dc.clean_dob("12/10/21"), "12-10-21")
    

if __name__ == '__main__':
    unittest.main()
