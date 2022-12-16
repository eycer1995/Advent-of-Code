# A for Rock
# B for Paper
# C for Scissors

# X for Rock
# Y for Paper
# Z for Scissors

# Scoring
# shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors) 

# outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won)

# Part 2
# X meas to lose
# Y measn to draw
# Z means to win

data = open('./inputs/d2.txt', 'r').read().split("\n")

dic = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

dic_2 = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}


score = 0
score_2 = 0

for i in range(len(data) - 1):
    # My play following the strategy 

    elf_play = dic[data[i][0]]
    my_play = dic[data[i][2]]

    # My play if not following the strategy 
    my_play_2 = dic_2[data[i][2]]

    
    if (elf_play == "Rock") and (my_play == "Paper"):
        score = score + 2 + 6
    elif (elf_play == "Scissors") and (my_play == "Paper"):
        score = score + 2 + 0
    elif (elf_play == "Paper") and (my_play == "Paper"):
        score = score + 2 + 3
    elif (elf_play == "Rock") and (my_play == "Scissors"):
        score = score + 3 + 0
    elif (elf_play == "Scissors") and (my_play == "Scissors"):
        score = score + 3 + 3 
    elif (elf_play == "Paper") and (my_play == "Scissors"):
        score = score + 3 + 6
    elif (elf_play == "Rock") and (my_play == "Rock"):
        score = score + 1 + 3
    elif (elf_play == "Scissors") and (my_play == "Rock"):
        score = score + 1 + 6
    elif (elf_play == "Paper") and (my_play == "Rock"):
        score = score + 1 + 0
    else:
        print("condition error")

    if (elf_play == "Rock") and (my_play_2 == "win"):
        score_2 = score_2 + 2 + 6
    elif (elf_play == "Rock") and (my_play_2 == "lose"):
        score_2 = score_2 + 3 + 0 
    elif (elf_play == "Rock") and (my_play_2 == "draw"):
        score_2 = score_2 + 1 + 3
    elif (elf_play == "Scissors") and (my_play_2 == "win"):
        score_2 = score_2 + 1 + 6
    elif (elf_play == "Scissors") and (my_play_2 == "lose"):
        score_2 = score_2 + 2 + 0
    elif (elf_play == "Scissors") and (my_play_2 == "draw"):
        score_2 = score_2 + 3 + 3
    elif (elf_play == "Paper") and (my_play_2 == "win"):
        score_2 = score_2 + 3 + 6
    elif (elf_play == "Paper") and (my_play_2 == "lose"):
        score_2 = score_2 + 1 + 0
    elif (elf_play == "Paper") and (my_play_2 == "draw"):
        score_2 = score_2 + 2 + 3
    else:
        print("cond 2 error")

print("Following the strategy guide: " + str(score))
print("If not following the strategy: " + str(score_2))
