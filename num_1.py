# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:26:54 2019

@author: hp
"""

string ="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

string = "map"

offset = 2
# k --> m
# o --> q
# e --> g


for c in string:
    if (c.isascii):
        print (chr(ord(c) + offset), end = "")
        