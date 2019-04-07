# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 17:25:50 2019

@author: hp
"""
import pickle

filename = "banner.p"
file = open(filename,"rb")

data = pickle.load(file)

for line in data:
    for part in line:
        for i in range(part[1]):
            print (part[0], end = "")
    print("")