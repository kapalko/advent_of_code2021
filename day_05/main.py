import numpy as np
from numpy.core.defchararray import count

lines = []
with open('day_05/data.txt') as f:
# with open('day_05/unit_test.txt') as f:
    for l in f:
        line = l.strip()
        x1, y1x2, y2 = line.split(',')
        y1, x2 = y1x2.split(' -> ')
        lines.append([int(x1), int(y1), int(x2), int(y2)])
x_min = min(lines, key=lambda x: x[0])[0]
y_min = min(lines, key=lambda x: x[1])[1]
x_max = max(lines, key=lambda x: x[2])[2]
y_max = max(lines, key=lambda x: x[3])[3]
dim = max(x_min, y_min, x_max, y_max) + 1
counts = np.zeros((dim, dim))

for track in lines:
    x1, y1, x2, y2 = track
    
    # vertical track
    if x1 == x2:
        y1, y2 = min(y1, y2), max(y1, y2)
        for idx in range(y1, y2+1):
            counts[idx, x1] += 1
    
    # horizontal track
    elif y1 == y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        for idx in range(x1, x2+1):
            counts[y1, idx] += 1
    # print(counts)
print(counts)
danger = (counts >= 2).sum()
print("\nPart 1a: \n")
print(danger)  

counts = np.zeros((dim, dim))
for track in lines:
    x1, y1, x2, y2 = track
    
    # vertical track
    if x1 == x2:
        y1, y2 = min(y1, y2), max(y1, y2)
        for idx in range(y1, y2+1):
            counts[idx, x1] += 1
    
    # horizontal track
    elif y1 == y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        for idx in range(x1, x2+1):
            counts[y1, idx] += 1
            
    # diagonal
    # Southeast
    elif (x1 < x2) and (y1 < y2):
        for i in range(x2-x1+1):
            counts[y1+i, x1+i] += 1
    
    # Northwest
    elif (x1 > x2) and (y1 > y2):
        for i in range(x1-x2+1):
            counts[y1-i, x1-i] += 1
    
    # Southwest
    elif (x1 > x2) and (y1 < y2):
        for i in range(x1-x2+1):
            counts[y1+i, x1-i] += 1
    
    # Northeast
    else:
        for i in range(x2-x1+1):
            counts[y1-i, x1+i] += 1
    
        
print(counts)
danger = (counts >= 2).sum()
print(danger)    