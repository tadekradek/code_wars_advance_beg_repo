"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

"""

#my solution
from math import floor

def make_readable(seconds):
    if seconds <= 359999:
        return "{}:{}:{}".format('%02d'%floor(seconds/3600),'%02d'%floor((seconds%3600)/60),'%02d'%(seconds - ((floor(seconds/3600)*3600)+ floor((seconds%3600)/60)*60)))
    else:
        return "Error"


##  '%02d'% -> very important, when it comes to defining format of numbers


#another solutions

def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)


def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)