# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 18:23:00 2019

@author: hp
"""
import zipfile 

fileroot = "channel.zip"
with zipfile.ZipFile(fileroot,"r") as file:
    Nothing =  "90052" + ".txt"
    for i in range(0,1000):
        temp1 = file.open(Nothing,"r").read()
        
        comment = str(file.getinfo(Nothing).comment)[2:-1]
        if comment.endswith("n"):
            print()
        print(comment, end = "") 
        temp = str(temp1)
        none = "Next nothing is "
        num_index = temp.find(none) + len(none)
        if num_index <= len(none):
            break
        Nothing = str(temp[num_index:-1]) + ".txt"
       
    