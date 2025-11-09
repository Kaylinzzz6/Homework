# Lesson 34
def converty(string):
    converted = string.split(",")
    a_list = []
    for nums in converted:
        a_list.append(int(nums))
    
    return a_list

from random import randrange
def rando_list(start, end, frequency):
    if start < end and frequency > 0:
    a_list = []
    for _ in range(frequency):
        randonums = randrange(start, end + 1)
        a_list.append(randonums)
    return a_list
    else:
        return []
