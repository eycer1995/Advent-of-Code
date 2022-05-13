elf_directions = open('./2015/d3.txt', 'r').read().replace('\n', '')
# <>^v
directions = {
    '^': [0, 1],
    'v': [0, -1],
    '>': [1, 0],
    '<': [-1, 0]
}

houses = set()
coor_x = coor_y = 0
houses.add(tuple([coor_x, coor_y]))

santa_x = santa_y = 0
santa = set()
santa.add(tuple([coor_x, coor_y]))

robo_x = robo_y = 0
robo = set()
robo.add(tuple([coor_x, coor_y]))

for x in range(len(elf_directions)):
    coor_x += directions[elf_directions[x]][0]
    coor_y += directions[elf_directions[x]][1]
    houses.add(tuple([coor_x, coor_y]))
    if x % 2 == 1:
        santa_x += directions[elf_directions[x]][0]
        santa_y += directions[elf_directions[x]][1]
        santa.add(tuple([santa_x, santa_y]))
    else:
        robo_x += directions[elf_directions[x]][0]
        robo_y += directions[elf_directions[x]][1]
        robo.add(tuple([robo_x, robo_y]))

print("Day 3 part 1: " + str(len(houses)))
print("Day 3 part 2: " + str(len(santa.union(robo))))
