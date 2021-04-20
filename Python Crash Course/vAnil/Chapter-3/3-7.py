# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 16:12:42 2020

@author: ANIL
"""

guests = ['Einstein', 'Tesla', 'Newton']
print(f"Dear {guests[0]}, please come to my dinner.")
print(f"Dear {guests[1]}, please come to my dinner.")
print(f"Dear {guests[2]}, please come to my dinner.\n\n")

print("I just found a bigger dinner table so now more space is available.\n\n")

#begining
guests.insert(0, 'Alan')

#middle
guests.insert(2, 'Goenka')

#end
guests.append('Rahul')

print(f"Dear {guests[0]}, please come to my dinner.")
print(f"Dear {guests[1]}, please come to my dinner.")
print(f"Dear {guests[2]}, please come to my dinner.")
print(f"Dear {guests[3]}, please come to my dinner.")
print(f"Dear {guests[4]}, please come to my dinner.")
print(f"Dear {guests[5]}, please come to my dinner.\n\n")

print("I have space for only two guests.")

guest = guests.pop()
print(f"Dear {guest}, Sorry I couldn't invite you to dinner.")
guest = guests.pop()
print(f"Dear {guest}, Sorry I couldn't invite you to dinner.")
guest = guests.pop()
print(f"Dear {guest}, Sorry I couldn't invite you to dinner.")
guest = guests.pop()
print(f"Dear {guest}, Sorry I couldn't invite you to dinner.\n\n")


print(f"Dear {guests[0]},You are still invited, please come to my dinner.")
print(f"Dear {guests[1]},You are still invited, please come to my dinner.")

del guests[0]
del guests[0]

print(guests)