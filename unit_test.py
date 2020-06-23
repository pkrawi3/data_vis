# Imports
import graphical_tools as tools
import unittest
import numpy as np
import pandas as pd

class TestStringMethods(unittest.TestCase):

    """
    Tests basic reading of a CSV file
    """
    def test_csv_good(self):
        table, error = tools.read_table('tests/unit_1.csv')
        self.assertTrue(pd.DataFrame(np.array([[1,2,3],[4,5,6]]), columns=['a','b','c'], dtype='int64').equals(table))
        self.assertEqual(error, 0)

    """
    Tests basic reading of an XLSX file
    """
    def test_xlsx_good(self):
        table, error = tools.read_table('tests/unit_2.xlsx')
        self.assertTrue(pd.DataFrame(np.array([[1,2,3],[4,5,6]]), columns=['a','b','c'], dtype='int64').equals(table))
        self.assertEqual(error, 0)

    """
    Tests basic reading of a XLS file
    """
    def test_xls_good(self):
        table, error = tools.read_table('tests/unit_3.xls')
        self.assertTrue(pd.DataFrame(np.array([[1,2,3],[4,5,6]]), columns=['a','b','c'], dtype='int64').equals(table))
        self.assertEqual(error, 0)

    """
    Tests basic reading of a bad excel file
    """
    def test_txt_bad(self):
        table, error = tools.read_table('tests/unit_4.txt')
        self.assertFalse(pd.DataFrame(np.array([[1,2,3],[4,5,6]]), columns=['a','b','c'], dtype='int64').equals(table))
        self.assertEqual(error, 1)

    """
    Tests the creation of Scatter Plot of test file 1
    """
    def test_scatter_one(self):
        tools.main_table, error = tools.read_table('tests/unit_1.csv')
        current_figure = tools.create_scatter()


if __name__ == '__main__':
    unittest.main()