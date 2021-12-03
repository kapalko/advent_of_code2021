import numpy as np

def frequency_digits_place(a):
    """ Find the most frequent number (1 or 0) in a binary digit's place"""
    frequency = np.zeros((len(a[0])))

    for num in a:
        for idx, char in enumerate(num):
            frequency[idx] += int(char)
    
    return frequency


def frequency_in_binary(data):
    freq = frequency_digits_place(data)
    return [1 if val >= len(data)/2 else 0 for val in freq]


def invert_binary(a):
    return [1 if val == 0 else 0 for val in a]


def binary_to_int(a):
    """ Converts a list or array of binary integers into a string and then an integer"""
    a = ''.join([str(v) for v in a])
    return int(a, 2)


def day_3a(data):
    
    gamma = frequency_in_binary(data)
    epsilon = invert_binary(gamma)
    gamma = binary_to_int(gamma)
    epsilon = binary_to_int(epsilon)

    print(gamma*epsilon)
    
def day_3b(data):
    
    # find O2 by iterating through the full array of data
    oxygen_list = data[:]
    i = 0
    while len(oxygen_list) > 1 and i < len(data[0]):

        frequency = frequency_in_binary(oxygen_list)
        tracker = []
        for idx, val in enumerate(oxygen_list):
            if int(val[i]) != frequency[i]:
                tracker.append(idx)
        oxygen_list = np.delete(oxygen_list, tracker)
        i += 1
    
    # find CO2
    co2_list = data[:]
    i = 0
    while len(co2_list) > 1 and i < len(data[0]):

        frequency = frequency_in_binary(co2_list)
        tracker = []
        for idx, val in enumerate(co2_list):
            if int(val[i]) == frequency[i]:
                tracker.append(idx)
        co2_list = np.delete(co2_list, tracker)
        i += 1

    ans = binary_to_int(oxygen_list) * binary_to_int(co2_list)
    print(ans)

data = np.genfromtxt('day_03/data.txt', dtype='str', skip_header=1)
# data = np.genfromtxt('day_03/unit_data.txt', dtype='str', skip_header=1)  # unit test

day_3a(data)
day_3b(data)
