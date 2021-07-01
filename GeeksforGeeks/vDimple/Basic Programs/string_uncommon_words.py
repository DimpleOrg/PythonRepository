# -*- coding: utf-8 -*-
"""
Created on Fri May 14 06:38:44 2021

@author: dimpl
"""

# Python program to find uncommon words from two Strings
# Input : A = "Geeks for Geeks"
#         B = "Learning from Geeks for Geeks"
# Output : ['Learning', 'from']

# Input : A = "apple banana mango"
#         B = "banana fruits mango"
# Output : ['apple', 'fruits']

# Method 1:
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
A = A.split()
B = B.split()
print(set(A).symmetric_difference(set(B)))


# Method 2:
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
count = {}
for word in A.split():
    count[word] = count.get(word, 0) + 1
for word in B.split():
    count[word] = count.get(word, 0) + 1
res = [word for word in count if count[word] == 1]
print(res)


# Method 3:
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
list_a = A.split()
list_b = B.split()
uc = ""
for word in list_a:
    if word not in list_b:
        uc += word + " "
for word in list_b:
    if word not in list_a:
        uc += word + " "

print(uc)
