# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 23:53:12 2021

@author: dimpl
"""

# =============================================================================
# Given an array A containing n integers. The task is to check whether the array
# is Monotonic or not. An array is monotonic if it is either monotone increasing
# or monotone decreasing.
# An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A
# is monotone decreasing if for all i <= j, A[i] >= A[j].
# Return “True” if the given array A is monotonic else return “False” (without
#                                                                      quotes).
#
# Examples:
#
# Input : 6 5 4 4
# Output : true
#
# Input : 5 15 20 10
# Output : false
# =============================================================================


def isMonotonic(arr):
    result = False
    if len(arr) <= 2:
        return True
    else:
        for i in range(len(arr)-1):
            if arr[i] <= arr[i+1]:
                result = True
            else:
                result = False
                break

        if result == False:
            for i in range(len(arr)-1):
                if arr[i] >= arr[i+1]:
                    result = True
                else:
                    result = False
                    break
    return result


arr = [4, 14, 9, 8]
print(isMonotonic(arr))
