# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 17:33:52 2021

@author: ANIL
"""
import unittest
from employee import Employee


class TestEmployeeClass(unittest.TestCase):
    """Tests for Employee class"""

    def setUp(self):
        self.employee_obj = Employee('Mika', 'Singh', 100000)

    def test_give_default_raise(self):
        self.employee_obj.give_raise()
        self.assertEqual(self.employee_obj.annual_salary, 105000)

    def test_give_custom_raise(self):
        self.employee_obj.give_raise(8000)
        self.assertEqual(self.employee_obj.annual_salary, 108000)


if __name__ == '__main__':
    unittest.main()
