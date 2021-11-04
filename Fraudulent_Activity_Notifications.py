""" If the amount spent by a client on a particular day is greater than or equal to
twice the client's median spending for a trailing number of days, they send the client a
notification about potential fraud. The bank doesn't send the client any notifications
until they have at least that trailing number of prior days' transaction data.

"""
import math
import os
import random
import re
import sys
import statistics

def activityNotifications(ex, k):
    d =k+1
    trailing = 0
    for i in range(0,len(ex)):
        val = ex[i:d+i-1]
        if len(val)== d-1 :
            med = statistics.median(val)
            if (i+d)<= len(ex):
                if ex[i+d-1] >= 2*med:
                    trailing = trailing +1

            else:
                break
        else:
            break
    return trailing

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
