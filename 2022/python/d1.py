data = open('./inputs/d1.txt', 'r').read().split("\n\n")

number_of_elves = len(data)
calories = []

for i in range(number_of_elves):
    current_elf = data[i].split("\n")
    sum = 0
    for j in range(len(current_elf)):
        if current_elf[j] == "":
            continue
        else:
            sum = sum + int(current_elf[j])
    calories.append(sum)    

calories.sort()

top_three = calories[-1] + calories[-2] + calories[-3]

print("The elf with the biggest amount of calories has:  " + str(calories[-1]))

print("The total calories for top three is:  " + str(top_three))
