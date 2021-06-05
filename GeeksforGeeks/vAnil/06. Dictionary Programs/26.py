# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 00:49:34 2021

@author: ANIL
"""

'''
Scraping And Finding Ordered Words In A Dictionary using Python
'''
import requests

url = "https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt"
fetchData = requests.get(url)

words = fetchData.content.decode('utf-8').split('\n')


for word in words:
    if "".join(sorted(word)) == word:
        print('Ordered word:', word)
        
    