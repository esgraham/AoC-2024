leftList = []
rightList = []
for line in open('Day1/data.txt','r'):
    split = line.strip().split()
    leftList.append(int(split[0]))
    rightList.append(int(split[1]))

def similarityscore(left):
    similar = rightList.count(left)
    return similar*left

def part1():

    leftList.sort()
    rightList.sort()

    total = 0
    for l, r in zip(leftList, rightList):
        v = abs(r-l)
        total = total + v
    return total

def part2():
    total = 0
    for l in leftList:
        total = total + similarityscore(l)
    return total


print('Part 1: ' + str(part1()))
print ('Part 2: ' + str(part2()))