import numpy as np

def day_1a(d):
    """Takes in an array and returns the number of sequences that increase in value in that array"""

    count = 0

    for i in range(1, len(d)):
        if d[i] > d[i-1]:
            count += 1
    print(count)


def day_1b(d):
    """Takes an array and returns the number of 3-sums sequences that increase in value from the array"""
    count = 0
    prev_sum = np.sum(d[:3])

    for i in range(3, len(d)):
        new_sum = np.sum(d[i-2:i+1])
        if new_sum > prev_sum:
            count += 1
        prev_sum = new_sum
    print(count)


data = np.genfromtxt('data.csv', dtype=int, skip_header=1)
# data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]  # unit testing

if __name__ == "__main__":
    print("Day 1a: ")
    day_1a(data)
    print("Day 1b: ")
    day_1b(data)

