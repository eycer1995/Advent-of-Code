data = open('d2.txt', 'r').read().split('\n')
directions = []
depth = 0
horizontal = 0
aimdepth = 0

for x in range(len(data)):
    directions.append(data[x].split(" "))

    if (directions[x][0] == 'forward'):
        horizontal = horizontal + int(directions[x][1])
        if (depth > 0):
            aimdepth = aimdepth + (depth * int(directions[x][1]))
    
    if directions[x][0] == 'down':
        depth = depth + int(directions[x][1])
    elif directions[x][0] == 'up':
        depth = depth - int(directions[x][1])
        
print("Day 2 part 1: " + str(horizontal*depth))
print("Day 2 part 2: " + str(horizontal*aimdepth))

