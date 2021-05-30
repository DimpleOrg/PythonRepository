# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:57:50 2021

@author: ANIL
"""

'''
Dictionary and counter in Python to find winner of election
Input :  votes[] = {"john", "johnny", "jackie", 
                    "johnny", "john", "jackie", 
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny", 
                    "john"};
Output : John
We have four Candidates with name as 'John', 
'Johnny', 'jamie', 'jackie'. The candidates
John and Johny get maximum votes. Since John
is alphabetically smaller, we print it.
'''
from collections import Counter 

votes = ['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john'] 

dic = Counter(votes)
newDic = {}
for value in dic.values():
    newDic[value] = []

for key,value in dic.items():
    newDic[value].append(key)
    
maxVote = sorted(newDic.keys(),reverse=True)[0] 

answer = sorted(newDic[maxVote])[0]

print(answer)
    


