#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:50:33 2020

@author: augustinjose
"""

with open("dataset.txt", "r+") as file:
    text = file.readlines()
who = []   
what = []
when = []
affirmation = []
unknown = []
for i in range(len(text)):
    line = text[i].split(",,,")
    if line[1] ==" who\n":
        who.append(line[0])
    if line[1] ==" what\n":
        what.append(line[0])
    if line[1] ==" when\n":
        when.append(line[0])
    if line[1] ==" affirmation\n":
        affirmation.append(line[0])
    if line[1] ==" unknown\n":
        unknown.append(line[0])

from eywa.nlu import Classifier

clf = Classifier()
clf.fit(who, 'who')
clf.fit(what, 'what')
clf.fit(when, 'when')
clf.fit(affirmation, 'affirmation')
clf.fit(unknown, 'unknown')
x = input("Enter string :")
print(clf.predict(str(x)))  