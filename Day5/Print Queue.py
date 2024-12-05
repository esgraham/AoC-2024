data = open('Day5/data.txt','r').readlines()

i = {}
pn = []

for line in data:
    if '|' in line:
        r = line.strip().split('|')
        if r[0] in i.keys(): i[r[0]].append(r[1])
        else: i.update({r[0]:[r[1]]})
    else:
        if ',' in line:
            pn.append(line.strip().split(','))

def evaluate_rules(p):
    rules = [(n, a, p.index(n), p.index(a)) for n in p for a in p if n in i.keys() and a in i[n]]
    wrules = [(t, False) for t in rules if t[2]>t[3]]
    return wrules

def part1():
    total = 0
    for p in pn:
        wrules = evaluate_rules(p)
        if (len(wrules)==0):
            total += int(p[len(p)//2])
    return total

def part2():
    total = 0
    for p in pn:
        wrules = evaluate_rules(p)
        while len(wrules)>0:
            for w in wrules:
                first_index = p.index(w[0][0])
                second_index = p.index(w[0][1])
                p[first_index]= w[0][1]
                p[second_index]=w[0][0]
            wrules = evaluate_rules(p)
            if len(wrules)==0:
                total += int(p[len(p)//2])
    return total



#print('Part 1: ' + str(part1()))
print ('Part 2: ' + str(part2()))
