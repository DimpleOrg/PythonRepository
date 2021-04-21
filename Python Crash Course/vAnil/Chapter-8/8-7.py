# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:34:06 2021

@author: ANIL
"""


def make_album(name, title, no_songs=None):
    info = {name: title}
    if no_songs:
        info['no_of_songs'] = no_songs
    return info


album_info1 = make_album('Rahman', 'Ma tujhe salam')
print(album_info1)
album_info2 = make_album('Dupa Lipa', 'Future Nostaligia')
print(album_info2)
album_info3 = make_album('Lady Gaga', 'Chromatica')
print(album_info3)
album_info4 = make_album('Lady Gaga', 'Chromatica', 10)
print(album_info4)
