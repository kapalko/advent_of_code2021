import numpy as np

def day_2a(data):
    movement = 0
    depth = 0

    for mv in data:
        if mv[0] == 'forward':
            movement += int(mv[1])
        elif mv[0] == 'down':
            depth += int(mv[1])
        else:
            depth -= int(mv[1])

    print(movement*depth)

def day_2b(data):
    movement = 0
    depth = 0
    aim = 0

    for mv in data:
        if mv[0] == 'forward':
            movement += int(mv[1])
            depth += aim*int(mv[1])
        elif mv[0] == 'down':
            aim += int(mv[1])
        else:
            aim -= int(mv[1])

    print(movement*depth)


data = np.genfromtxt('data.csv', dtype='str', delimiter=' ', skip_header=1)

if __name__ == '__main__':
    print('2a:')
    day_2a(data)
    print('2b:')
    day_2b(data)