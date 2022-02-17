elf_directions = open('./2015/d3.txt', 'r').read()
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

for x in range(len(elf_directions)):
    if elf_directions[x] == '\n':
        continue

    else:
        coor_x += directions[elf_directions[x]][0]
        coor_y += directions[elf_directions[x]][1]
        houses.add(tuple([coor_x, coor_y]))

print(len(houses))
