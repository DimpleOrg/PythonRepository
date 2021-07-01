# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 06:05:00 2021

@author: dimpl
"""
import requests

# contains about 2500 words
url = "https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt"
fetchData = requests.get(url)

# extracts the content of the webpage
wordList = fetchData.content

# decodes the UTF-8 encoded text and splits the
# string to turn it into a list of words
wordList = wordList.decode("utf-8").split()
print(wordList)

for word in wordList:
    if "".join(sorted(word)) == word:
        print(word)
