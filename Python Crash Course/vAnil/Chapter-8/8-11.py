# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 16:46:58 2021

@author: ANIL
"""


def show_messages(messages):
    sent_msg = []
    while messages:
        message = messages.pop()
        print(message)
        sent_msg.insert(0, message)

    return sent_msg


messages = ['Delhi is capital of India', 'Indian cricket team captain is Virat',
            'Amitabh is film actor.']
msgs = show_messages(messages[:])
print(messages)
print(msgs)
