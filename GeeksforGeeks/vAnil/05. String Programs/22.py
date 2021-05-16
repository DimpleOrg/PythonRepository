# -*- coding: utf-8 -*-
"""
Created on Sun May 16 09:24:47 2021

@author: ANIL
"""

'''
Python – Replace duplicate Occurrence in String
'''

test_str = 'Gfg is best . Gfg also has Classes now.\
             Classes help understand better . '

repl_dict = {'Gfg' :  'It', 'Classes' : 'They' }


wordDict = {}

words = test_str.split()

for word in words:
    wordDict[word] = wordDict.get(word,0)+1
    
for key in repl_dict.keys():
    if wordDict[key] > 1:
        count = 0
        for i in range(len(words)):
            if words[i] == key:
                if count == 0:
                    count = 1
                else:
                    words[i] = repl_dict[key]
                    
                    
print(*words)
                
            