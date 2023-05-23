# Mean - The average value
# Median - The mid point value
# Mode - The most common value

import math
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86,111,87,87]

def find_mean(list):
    sum = 0
    i = 0
    for x in list:
        sum = sum + x
        i += 1
    return sum / i

def find_median(list):
    list.sort()
    return list[math.floor( len(list) / 2)]

def find_index(list, value):
    try:
        append_index = list.index(value)
        return append_index
    except:
        return -1
    
def find_mode(list):
    props = []
    value = []
    for x in list:
        a_index = find_index(props, x)
        if a_index != -1:
            value[a_index] += 1
        else:
            props.append(x)
            value.append(1)
    
    max_value = value.index(max(value))
    mode = props[max_value]
    return mode




print("mean: ", find_mean(speed))
print("medain: ", find_median(speed))
print("mode: ", find_mode(speed))