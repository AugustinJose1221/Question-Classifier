#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:50:33 2020

@author: augustinjose
"""


from eywa.nlu import Classifier


x_hotel = ['book a hotel', 'need a nice place to stay', 'any motels near by']
x_weather = ['what is the weather like', 'is it hot outside']

clf = Classifier()
clf.fit(x_hotel, 'hotel')
clf.fit(x_weather, 'weather')

print(clf.predict('will it rain today'))  # >>> 'weather'
print(clf.predict('find a place to stay'))  # >>> 'hotel'