import string

data = open('./inputs/d3.txt','r').read().split('\n')


alphabet = list(string.ascii_letters)
score = 0
score_2 = 0
count = 0

#print(len(alphabet))

# Part 1
for runstack in range(len(data)):
    # Get each comparment by diving the runstack in hafl
    run_len = len(data[runstack])
    comp1 = data[runstack][0:run_len//2]
    comp2 = data[runstack][run_len//2:]

#    print("for runstack: " + data[runstack])
#    print("comparment 1 is : " + comp1)
#    print("comparment 2 is : " + comp2)
        
    for letter in comp1:
        if letter in comp2:
#            print(f"The letter {letter} is on both")
            for i in range(len(alphabet)):
                if alphabet[i] == letter:
                    score = score + i + 1
            break
#    print("---")

print(f"The priorities for part 1 is: {score}")

# Part 2

group = []
for i in range(len(data)):
    if count == 2:
        group.append(data[i])
        print(group)
        # Here is the 3 runstack for each group
        for j in group[0]:
            if (j in group[1]) and (j in group[2]):
                print(f"The letter {j} is on the 3 runstacks")
                for x in range(len(alphabet)):
                    if alphabet[x] == j:
                        score_2 = score_2 + x + 1
                break

        print("---")
        group = []
        count = 0
    else:
        group.append(data[i])
        count = count + 1

print(f"The priorities for part 2 is: {score_2}")
