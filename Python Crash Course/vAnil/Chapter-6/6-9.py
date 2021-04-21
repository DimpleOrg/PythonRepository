# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:36:00 2021

@author: ANIL
"""
favorite_places = {
    'siddharth': ['taiwan', 'punjab', 'kashmir'],
    'gautam': ['america', 'guragaon', 'chandigarh'],
    'tapojoy': ['kolkata', 'delhi', 'bangalore'],
}
for data in favorite_places:
    print(f"Name:\t\t\t{data.title()}")
    print('Favorite Places:')
    for place in favorite_places[data]:
        print(f"\t\t\t\t{place.title()}")
    print('\n')
