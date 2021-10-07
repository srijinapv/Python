#Condition  :A string to be valid if all characters of the string appear the same number of times.

import math
import os
import random
import re
import sys


def isValid(s):
    length_s = len(s)
    all_freq = {}

    for i in s:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    return all_freq

s = input("Enter string:")
out = isValid(s)
print(out)
# list out keys and values separately
key_list = list(out.keys())
val_list = list(out.values())
# print key with value index 1
#position = val_list.index(1)
#print(val_list[position])

if len(s) %2 == 0 :
    for i in range(1,len(s)+1):
        if val_list[i] == 2:
            i = i + 1
        elif val_list[i] == 1:
            i=i+1
        else:
            print("not valid")
    print("valid")

else:
    for i in range(1,len(s)+1):
        if val_list[i] == 1 :
            i = i + 1
        else:
            print("not valid")
print("valid")



