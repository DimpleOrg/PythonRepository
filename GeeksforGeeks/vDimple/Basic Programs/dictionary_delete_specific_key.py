# -*- coding: utf-8 -*-
"""
Created on Wed May 26 23:42:24 2021

@author: dimpl
"""

# Ways to remove a key from dictionary

# Method 1 : Using del
# del keyword can be used to inplace delete the key that is present in the dictionary.
# One drawback that can be thought of using this is that is raises an exception if
# the key is not found and hence non-existence of key has to be handled.

test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 20, "Haritha": 19}
del test_dict["Mani"]
print(test_dict)

# Method 2 : Using pop()

# pop() can be used to delete a key and its value inplace. Advantage over using
# del is that it provides the mechanism to print desired value if tried to remove
#  a non-existing dict. pair. Second, it also returns the value of key that is
#  being removed in addition to performing a simple delete operation.

test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 20, "Haritha": 19}
removed_value = test_dict.pop("Mani")
print(removed_value)
print(test_dict)


# Method 3
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 20, "Haritha": 19}
new_dict = {key: val for key, val in test_dict.items() if key != "Mani"}
print(new_dict)
