#parse into grid
data = open('Day4/data.txt','r').readlines()
H, W = len(data), len(data[0])-1
grid = {(y,x):data[y][x] for y in range(H) for x in range(W)}

def part1():
    TARGET = "XMAS"
    DELTAS = [(dy,dx) for dy in [-1,0,1] for dx in [-1,0,1] if (dx!=0 or dy!=0)]
    count = 0
    for y, x in grid:
        for dy,dx in DELTAS:
            candidate = "".join(grid.get((y+dy*i, x+dx*i),"") for i in range(len(TARGET)))
            count += candidate == TARGET
    return count

def part2():
    count = 0
    for y, x in grid:
        if grid[y,x]=="A":
            lr = grid.get((y-1,x-1),"")+grid.get((y+1,x+1),"")
            rl = grid.get((y-1,x+1),"")+grid.get((y+1,x-1),"")
            count += {lr, rl} <= {"MS", "SM"}
    return count

print('Part 1: ' + str(part1()))
print ('Part 2: ' + str(part2()))