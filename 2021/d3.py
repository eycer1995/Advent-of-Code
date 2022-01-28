data = open('d3.txt', 'r').read().split('\n')
counters0 = [0,0,0,0,0,0,0,0,0,0,0,0]
counters1 = [0,0,0,0,0,0,0,0,0,0,0,0]
gamma = ''
epsilon = ''


for x in range(len(data)):
    print(data[x])
    for y in range(12):
        if data[x][y] == '0':
            counters0[y]+=1
        else:
            counters1[y]+=1

for z in range(12):
    if counters0[z] > counters1[z]:
        gamma = gamma + '0'
        epsilon = epsilon + '1'
    else:
        gamma = gamma + '1'
        epsilon = epsilon + '0'

print('Day 3 part 1: ' + str(int(gamma, 2) * int(epsilon, 2)))
