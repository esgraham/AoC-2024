data = open('Day6/data.txt','r').readlines()
H, W = len(data), len(data[0])-1
grid = {(y,x):data[y][x] for y in range(H) for x in range(W)}
guardTurn= {'^':'>', '>':'V', 'V':'<', '<':'^'}
guard = ''

def turn_or_outofbounds(y, x):
    global guard
    n = grid.get((y, x), "")
    if n=="":
        guard = 'Out'
        return True
    elif n=="#":
         guard = guardTurn[guard]
         return True
    else:
        return False

def moveup(y, x):
    while not turn_or_outofbounds(y-1, x):
        y = y-1
        grid.update({(y, x):'X'})
    return y, x

def moveright(y, x):
    while not turn_or_outofbounds(y, x+1):
        x = x+1
        grid.update({(y, x):'X'})
    return y, x

def movedown(y, x):
    while not turn_or_outofbounds(y+1, x):
        y = y+1
        grid.update({(y, x):'X'})
    return y, x

def moveleft(y, x):
    while not turn_or_outofbounds(y, x-1):
        x = x-1
        grid.update({(y, x):'X'})
    return y, x

def find_start():
    global guard
    guard, y, x = [(grid[y,x], y, x) for y, x in grid if grid[y,x]=='^' or grid[y,x]=='<' or grid[y,x]=='>' or grid[y,x]=='V'][0]
    return y, x

def move_guard(y, x):
    turns=[]
    while guard=='^' or guard=='<' or guard=='>' or guard=='V':
        turns.append((y,x))
        match guard:
            case '^':
                y, x = moveup(y, x)
            case '>':
                y, x = moveright(y, x)
            case 'V':
                y, x = movedown(y, x)
            case '<':
                y, x = moveleft(y, x)
            case _:
                break
        indices = [i for i, c in enumerate(turns) for yx in turns if c == yx and turns.count(yx)>=2]
        if len(indices)>=16:
            return True
        
    return False


def part1():
    y, x = find_start()
    grid.update({(y, x):'X'})
    move_guard(y, x)

    return ['X' for y, x in grid if grid[y,x]=='X'].count('X')

def part2():
    total = 0
    #Refresh grid 
    global grid
    grid = {(y,x):data[y][x] for y in range(H) for x in range(W)}
    refresh_grid = grid.copy()
    y, x = find_start()

    for pos in [(y, x) for y, x in grid if grid.get((y, x), "") == '.']:
        print(pos)
        grid.update({pos:'#'})
        if (move_guard(y,x)):
            total = total + 1
        grid = refresh_grid.copy()
        find_start()

    return total

print('Part 1: ' + str(part1()))
#not performant.  Takes around 10 minutes.  Need to change so to jump to next block versus looking at each square.
print('Part 2: ' + str(part2()))