# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 16:10:27 2021

@author: ANIL
"""
import unittest

from city_functions import fun


class CityFunsTestCase(unittest.TestCase):
    '''test city functions function'''

    def test_city_fun(self):
        formatted_str = fun('Delhi', 'India')
        self.assertEqual(formatted_str, 'Delhi, India')

    def test_city_fun_pop(self):
        formatted_str = fun('Delhi', 'India', '121 Crores')
        self.assertEqual(formatted_str, 'Delhi, India - population 121 Crores')


if __name__ == '__main__':
    unittest.main()
