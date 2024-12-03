import re

memory = []
for line in open('Day3/data.txt','r'):
    memory.append(line.strip())


def mulNumbers(matches):
    total = 0
    for mul in matches:
        for m in mul:
            numbers = re.findall(r'\d+', m)
            total = total + (int(numbers[0])*int(numbers[1]))
    return total


def part1():
    matches = []
    for p in memory:
        matches.append(re.findall(r'mul\(\d{1,3},\d{1,3}\)', p))
        
    return mulNumbers(matches)

def part2():
    program = ""
    for p in memory:
            program = program + p


    split = re.split(r'do\(\)', program)

    do = []
    for section in split:
        dont = re.search(r'don\'t\(\)',section)
        if (dont):
            do.append(section[:dont.start()])
        else:
            do.append(section)

    matches = []    
    for d in do:
        matches.append(re.findall(r'mul\(\d{1,3},\d{1,3}\)', d))
    
    return mulNumbers(matches)
    



print('Part 1: ' + str(part1()))
print ('Part 2: ' + str(part2()))
