from itertools import pairwise

records = []
for line in open('Day2/data.txt','r'):
    records.append([int(x) for x in line.strip().split()])

def determine_diff(record):
    diff = [(y-x) for (x, y) in pairwise(record)]
    decrease = all(x <= 0 for x in diff)
    increase = all(x >= 0 for x in diff)
    diffamount = all(abs(x) <= 3 and abs(x) >=1 for x in diff)
    return decrease, increase, diffamount

def is_safe_with_damper(record):
    for i in range(0, len(record)):
        t = []
        t = record.copy()
        t.pop(i)
        if is_safe(t):
            return True

def is_safe(record):
    decrease, increase, diffamount = determine_diff(record)
    return (decrease or increase) and diffamount

def part1():
    total = 0
    for r in records:
        if is_safe(r):
            total = total+1
    return total

def part2():
    total = 0
    for r in records:
        if is_safe(r):
            total = total+1
        elif is_safe_with_damper(r):
            total = total+1
    return total


print('Part 1: ' + str(part1()))
print ('Part 2: ' + str(part2()))